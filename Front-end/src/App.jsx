import { useState, useRef, useEffect, useCallback } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import ChatMessage from './components/ChatMessage';
import ChatInput from './components/ChatInput';
import TypingIndicator from './components/TypingIndicator';
import WelcomeScreen from './components/WelcomeScreen';
import FeatureModal from './components/FeatureModal';
import {
  suggestions,
  urduSuggestions,
  sindhiSuggestions,
  punjabiSuggestions,
  pashtoSuggestions
} from './data/responses';
import './App.css';

const langMap = {
  en: "english",
  ur: "urdu",
  sd: "sindhi",
  pa: "punjabi",
  ps: "pashto",
};

const suggestionMap = {
  en: suggestions,
  ur: urduSuggestions,
  sd: sindhiSuggestions,
  pa: punjabiSuggestions,
  ps: pashtoSuggestions,
};

export default function App() {

  // 💬 Chat state
  const [messages, setMessages] = useState([]);
  const [activeChatId, setActiveChatId] = useState(null);
  const [chatHistory, setChatHistory] = useState(() => {
    try {
      const saved = localStorage.getItem("agri_chats");
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  // ☁️ Weather state
  const [weather, setWeather] = useState(null);
  const [weatherLoading, setWeatherLoading] = useState(false);
  const [weatherError, setWeatherError] = useState('');

  // 🎛 UI state
  const [isTyping, setIsTyping] = useState(false);
  const [isProcessingVoice, setIsProcessingVoice] = useState(false);
  const [language, setLanguage] = useState(() => localStorage.getItem('agri_lang') || 'en');
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [recordedAudioBlob, setRecordedAudioBlob] = useState(null);
  const [activeFeature, setActiveFeature] = useState(null);

  const isCancelingRef = useRef(false);

  const chatAreaRef = useRef(null);
  const audioRef = useRef(null); // currently playing audio (for Stop)

  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);
  const streamRef = useRef(null);

  const isRTL = ['ur', 'sd', 'pa', 'ps'].includes(language);

  // 🕒 Helpers
  const getTimestamp = () =>
    new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const getCurrentPosition = () =>
    new Promise((resolve, reject) => {
      if (!navigator.geolocation) {
        reject(new Error("Geolocation not supported by this browser."));
        return;
      }
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0,
      });
    });

  const handleGetWeather = useCallback(async () => {
    setWeatherError('');
    setWeather(null);
    setWeatherLoading(true);

    try {
      const position = await getCurrentPosition();
      const { latitude, longitude } = position.coords;

      const url = `http://127.0.0.1:8000/weather?lat=${encodeURIComponent(
        latitude
      )}&lon=${encodeURIComponent(longitude)}`;

      const res = await fetch(url);
      if (!res.ok) {
        let detail = '';
        try {
          const data = await res.json();
          detail =
            typeof data?.detail === 'string'
              ? data.detail
              : JSON.stringify(data?.detail ?? data);
        } catch {
          detail = await res.text();
        }
        console.error("Weather API error:", res.status, detail);
        throw new Error(detail || "Failed to fetch weather. Check backend/API key.");
      }

      const data = await res.json();
      setWeather(data);
    } catch (err) {
      console.error("Weather error:", err);
      const code = err?.code;
      if (code === 1) {
        setWeatherError("Location permission denied. Please allow location access.");
      } else if (code === 2) {
        setWeatherError("Location unavailable. Try again.");
      } else if (code === 3) {
        setWeatherError("Location request timed out. Try again.");
      } else {
        setWeatherError(err?.message || "Could not get weather.");
      }
    } finally {
      setWeatherLoading(false);
    }
  }, []);

  const stopCurrentAudio = useCallback(() => {
    const a = audioRef.current;
    if (!a) return;
    try {
      a.pause();
      a.currentTime = 0;
    } catch {
      // ignore
    }
    audioRef.current = null;
  }, []);

  const handleDeleteAudio = useCallback(async (audioUrl) => {
    if (!audioUrl) return;
    // If the current audio is playing this source, stop it first.
    const a = audioRef.current;
    if (a && a.src && a.src.includes(audioUrl)) {
      stopCurrentAudio();
    }

    try {
      await fetch("http://127.0.0.1:8000/delete-audio", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ audio_url: audioUrl }),
      });
    } catch (err) {
      console.error("Delete audio error:", err);
    } finally {
      // Remove audio from any message that referenced it
      setMessages((prev) =>
        prev.map((m) => (m.audio_url === audioUrl ? { ...m, audio_url: null } : m))
      );
    }
  }, [stopCurrentAudio]);

  // Auto-fetch weather on app load
  useEffect(() => {
    // Avoid eslint react-hooks/set-state-in-effect by deferring the call.
    const t = setTimeout(() => {
      handleGetWeather();
    }, 0);
    return () => clearTimeout(t);
  }, [handleGetWeather]);

  

  // Auto scroll
  useEffect(() => {
    if (chatAreaRef.current) {
      chatAreaRef.current.scrollTo({
        top: chatAreaRef.current.scrollHeight,
        behavior: 'smooth'
      });
    }
  }, [messages, isTyping]);

  // 🎤 TOGGLE RECORDING
  const toggleRecording = async () => {
    if (isRecording) {
      stopRecording();
    } else {
      await startRecording();
    }
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;
      audioChunksRef.current = [];

      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          audioChunksRef.current.push(e.data);
        }
      };

      mediaRecorder.onstop = async () => {
        setIsRecording(false);
        streamRef.current?.getTracks().forEach(t => t.stop());

        if (isCancelingRef.current) {
          isCancelingRef.current = false;
          return;
        }

        const audioBlob = new Blob(audioChunksRef.current, {
          type: "audio/webm"
        });
        setRecordedAudioBlob(audioBlob);
      };

      mediaRecorder.start();
      setIsRecording(true);

    } catch (err) {
      console.error("Mic error:", err);
    }
  };

  const stopRecording = () => {
    const mediaRecorder = mediaRecorderRef.current;
    if (mediaRecorder && mediaRecorder.state === "recording") {
      mediaRecorder.stop();
    }
  };

  const cancelRecording = () => {
    const mediaRecorder = mediaRecorderRef.current;
    if (mediaRecorder && mediaRecorder.state === "recording") {
      isCancelingRef.current = true;
      mediaRecorder.stop();
    }
    setRecordedAudioBlob(null);
  };

  const sendRecordedAudio = async () => {
    if (!recordedAudioBlob) return;
    const blobToSend = recordedAudioBlob;
    setRecordedAudioBlob(null);

    let currentId = activeChatId;
    if (!currentId) {
      currentId = Date.now();
      setActiveChatId(currentId);
    }

    try {
      setIsProcessingVoice(true);
      const formData = new FormData();
      formData.append("file", blobToSend, "voice.webm");

      const currentContext = `Month: ${new Date().toLocaleString('en-US', { month: 'long' })}, Location: ${weather?.city || 'Unknown'}`;
      const response = await fetch(
        `http://127.0.0.1:8000/speech-to-speech-record?target_lang=${langMap[language]}&context_info=${encodeURIComponent(currentContext)}`,
        {
          method: "POST",
          body: formData
        }
      );

      const data = await response.json();

      setMessages(prev => [
        ...prev,
        {
          id: Date.now(),
          role: "user",
          text: data.original_text || "Voice message",
          time: getTimestamp()
        },
        {
          id: Date.now() + 1,
          role: "ai",
          text: data.translated_text || "No response",
          time: getTimestamp(),
          audio_url: data.audio_url || null,
        }
      ]);

      if (data.audio_url) {
        const audio = new Audio(`http://127.0.0.1:8000${data.audio_url}`);
        audioRef.current = audio;
        audio.play().catch(() => {});
      }

    } catch (err) {
      console.error("Voice error:", err);
    } finally {
      setIsProcessingVoice(false);
    }
  };


  // 💬 TEXT SEND
  const handleSend = useCallback(async (text) => {

    if (!text.trim()) return;

    if (!activeChatId) setActiveChatId(Date.now());

    const userMessage = {
      id: Date.now(),
      role: 'user',
      text,
      time: getTimestamp()
    };

    setMessages(prev => [...prev, userMessage]);
    setIsTyping(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/translate-text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text,
          target_lang: langMap[language],
          context_info: `Month: ${new Date().toLocaleString('en-US', { month: 'long' })}, Location: ${weather?.city || 'Unknown'}`
        })
      });

      const data = await response.json();

      const aiMessage = {
        id: Date.now() + 1,
        role: 'ai',
        text: data?.translated_text || "No response",
        time: getTimestamp(),
        audio_url: data?.audio_url || null,
      };

      setMessages(prev => [...prev, aiMessage]);

      if (data?.audio_url) {
        const audio = new Audio(`http://127.0.0.1:8000${data.audio_url}`);
        audioRef.current = audio;
        audio.play().catch(() => {});
      }

    } catch (err) {
      console.error(err);

      setMessages(prev => [
        ...prev,
        {
          id: Date.now(),
          role: "ai",
          text: "Server error. Check backend.",
          time: getTimestamp()
        }
      ]);
    }

    setIsTyping(false);

  }, [language, activeChatId]);

  const handleSuggestionSelect = useCallback((query) => {
    handleSend(query);
  }, [handleSend]);

  const handleLanguageChange = useCallback((lang) => {
    setLanguage(lang);
  }, []);

  const handleSelectChat = useCallback((id) => {
    setActiveChatId(id);
    const selected = chatHistory.find(c => c.id === id);
    if (selected) {
      setMessages(selected.messages || []);
    } else {
      setMessages([]);
    }
  }, [chatHistory]);

  const handleDeleteChat = useCallback((id) => {
    setChatHistory(prev => prev.filter(c => c.id !== id));
    if (activeChatId === id) {
      setMessages([]);
      setActiveChatId(null);
    }
  }, [activeChatId]);

  // Sync messages with chatHistory
  useEffect(() => {
    if (!activeChatId || messages.length === 0) return;

    setChatHistory(prev => {
      const existingIdx = prev.findIndex(c => c.id === activeChatId);
      const dateStr = new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

      if (existingIdx > -1) {
        const updated = [...prev];
        updated[existingIdx] = {
          ...updated[existingIdx],
          messages: messages
        };
        return updated;
      } else {
        const firstUserMsg = messages.find(m => m.role === 'user');
        const firstText = firstUserMsg ? firstUserMsg.text : "Audio Chat";
        const title = firstText.slice(0, 30) + (firstText.length > 30 ? "..." : "");

        return [
          {
            id: activeChatId,
            title,
            date: dateStr,
            messages: messages
          },
          ...prev
        ];
      }
    });
  }, [messages, activeChatId]);

  // Save chatHistory to localStorage
  useEffect(() => {
    localStorage.setItem("agri_chats", JSON.stringify(chatHistory));
  }, [chatHistory]);

  const currentSuggestions = suggestionMap[language] || suggestions;

  return (
    <div className="app" dir={isRTL ? 'rtl' : 'ltr'}>

      <Sidebar
        chatHistory={chatHistory}
        activeChatId={activeChatId}
        language={language}
        onLanguageChange={handleLanguageChange}
        onNewChat={() => {
          setMessages([]);
          setActiveChatId(null);
        }}
        onSelectChat={handleSelectChat}
        onDeleteChat={handleDeleteChat}
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(p => !p)}
      />

      <main className="app__main">

        <Header
          language={language}
          onLanguageChange={handleLanguageChange}
          onMenuToggle={() => setSidebarOpen(p => !p)}
          hasMessages={messages.length > 0}
          weather={weather}
          weatherLoading={weatherLoading}
          weatherError={weatherError}
        />



        <div className="app__chat-area" ref={chatAreaRef}>

          {messages.length === 0 && !isTyping && !isProcessingVoice ? (
            <WelcomeScreen
              language={language}
            />
          ) : (
            <div className="app__messages">

              {messages.map(msg => (
                <ChatMessage
                  key={msg.id}
                  message={msg}
                  language={language}
                  onStopAudio={stopCurrentAudio}
                  onDeleteAudio={handleDeleteAudio}
                />
              ))}

              {(isTyping || isProcessingVoice) && (
                <TypingIndicator language={language} mode={isProcessingVoice ? 'voice' : 'text'} />
              )}

            </div>
          )}

        </div>

        <ChatInput
  onSend={handleSend}
  language={language}
  disabled={isTyping}
  onToggleMic={toggleRecording}
  isRecording={isRecording}
  recordedAudioBlob={recordedAudioBlob}
  onCancelAudio={cancelRecording}
  onSendAudio={sendRecordedAudio}
  contextInfo={`Month: ${new Date().toLocaleString('en-US', { month: 'long' })}, Location: ${weather?.city || 'Unknown'}`}
  onAction={(action) => setActiveFeature(action)}
  onUploadComplete={(data) => {
    let currentId = activeChatId;
    if (!currentId) {
      currentId = Date.now();
      setActiveChatId(currentId);
    }

    setMessages(prev => [
      ...prev,
      {
        id: Date.now(),
        role: "user",
        text: data.original_text || "Audio message",
        time: getTimestamp()
      },
      {
        id: Date.now() + 1,
        role: "ai",
        text: data.translated_text || "No response",
        time: getTimestamp(),
        audio_url: data.audio_url || null,
      }
    ]);

    // audio play
    if (data.audio_url) {
      const audio = new Audio(`http://127.0.0.1:8000${data.audio_url}`);
      audioRef.current = audio;
      audio.play().catch(() => {});
    }
  }}
/>
      </main>
      {activeFeature && (
        <FeatureModal
          feature={activeFeature}
          language={language}
          onClose={() => setActiveFeature(null)}
        />
      )}
    </div>
  );
}