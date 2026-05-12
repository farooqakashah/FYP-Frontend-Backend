import { useState, useEffect, useRef, useCallback } from 'react';
import { placeholderTexts, quickReplyChips } from '../data/responses';
import * as LucideIcons from 'lucide-react';
import { Send, Mic, Square, Paperclip, Trash2 } from 'lucide-react';
import './ChatInput.css';

const UI_TEXT = {
  en: {
    recording: 'Listening...',
    imageNotice: 'Audio uploaded — processing...',
    disclaimer: 'AI Assistant provides general guidance.',
    uploadTitle: 'Upload audio'
  },
  ur: {
    recording: 'سن رہا ہے...',
    imageNotice: 'آڈیو اپلوڈ ہوگئی — پروسیسنگ جاری ہے...',
    disclaimer: 'اے آئی معاون مشورہ فراہم کرتا ہے۔',
    uploadTitle: 'آڈیو اپلوڈ کریں'
  },
  sd: {
    recording: 'ٻڌي رهيو آهي...',
    imageNotice: 'آڈیو اپلوڈ ٿي وئي — پروسيس ٿي رهي آهي...',
    disclaimer: 'AI مددگار عام صلاح ڏئي ٿو۔',
    uploadTitle: 'آڈیو اپلوڈ ڪريو'
  },
  pa: {
    recording: 'سن رہیا اے...',
    imageNotice: 'آڈیو اپلوڈ ہو گئی — پروسیسنگ ہو رہی ہے...',
    disclaimer: 'AI مددگار عمومی صلاح دیندا اے۔',
    uploadTitle: 'آڈیو اپلوڈ کرو'
  },
  ps: {
    recording: 'اورېدلو...',
    imageNotice: 'غږ وسپاری شو — په چار کې دی...',
    disclaimer: 'AI مرسته عمومې لارښوونه ورکوي.',
    uploadTitle: 'غږ فایل پورته کړئ'
  }
};

const langMap = {
  en: "english",
  ur: "urdu",
  sd: "sindhi",
  pa: "punjabi",
  ps: "pashto",
};

export default function ChatInput({
  onSend,
  language,
  disabled,
  onUploadComplete,
  onToggleMic,
  isRecording,
  onAction,
  contextInfo,
  recordedAudioBlob,
  onCancelAudio,
  onSendAudio
}){

  const [input, setInput] = useState('');
  const [placeholderIndex, setPlaceholderIndex] = useState(0);
  const [showFileNotice, setShowFileNotice] = useState(false);

  const inputRef = useRef(null);
  const fileInputRef = useRef(null);

  const t = UI_TEXT[language] || UI_TEXT.en;
  const isRTL = ['ur', 'sd', 'pa', 'ps'].includes(language);

  // placeholder rotation
  useEffect(() => {
    const placeholders = placeholderTexts[language] || placeholderTexts.en;

    const interval = setInterval(() => {
      setTimeout(() => {
        setPlaceholderIndex(prev => (prev + 1) % placeholders.length);
      }, 300);
    }, 4000);

    return () => clearInterval(interval);
  }, [language]);

  const handleSend = useCallback(() => {
    const trimmed = input.trim();
    if (!trimmed || disabled) return;

    onSend(trimmed);
    setInput('');
    inputRef.current?.focus();
  }, [input, disabled, onSend]);

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  // ✅ FIX ONLY: correct backend endpoint
  const handleAudioUpload = async (e) => {
    const target = e.target;
    const file = target.files?.[0];
    if (!file) return;

    setShowFileNotice(true);

    const formData = new FormData();
    formData.append("file", file, file.name);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/speech-to-speech-record?target_lang=${langMap[language]}&context_info=${encodeURIComponent(contextInfo || '')}`,
        {
          method: "POST",
          body: formData
        }
      );

      const data = await response.json();

      // SEND RESULT TO APP.JSX ONLY
      if (onUploadComplete) {
        onUploadComplete(data);
      }

    } catch (err) {
      console.error("UPLOAD ERROR:", err);
    } finally {
      setShowFileNotice(false);
      target.value = "";
    }
  };
  const handleAudioClick = () => {
    
    fileInputRef.current?.click();
  }

  const placeholders = placeholderTexts[language] || placeholderTexts.en;
  const currentPlaceholder = placeholders[placeholderIndex % placeholders.length];
  const chips = quickReplyChips[language] || quickReplyChips.en;

  return (
    <div className="chat-input">

      <div className="chat-input__chips" dir={isRTL ? 'rtl' : 'ltr'}>
        {chips.map((chip, i) => {
          const IconComponent = LucideIcons[chip.icon] || LucideIcons.HelpCircle;
          return (
            <button
              key={i}
              className="chat-input__chip"
              onClick={() => onAction && onAction(chip.action)}
              disabled={disabled}
            >
              <IconComponent size={14} className="chat-input__chip-icon" />
              {chip.label}
            </button>
          );
        })}
      </div>

      {showFileNotice && (
        <div className="chat-input__file-notice">
          {t.imageNotice}
        </div>
      )}

      {/* ✅ YOUR ORIGINAL UI (UNCHANGED) */}
      <div className="chat-input__container">
        
        {!recordedAudioBlob && (
          <button
            className={`chat-input__icon-btn ${isRecording ? 'chat-input__icon-btn--recording' : ''}`}
            onClick={onToggleMic}
            type="button"
            aria-label={isRecording ? "Stop recording" : "Start voice input"}
            title={isRecording ? "Click to stop" : "Click to speak"}
          >
            {isRecording ? (
              <Square size={18} fill="currentColor" />
            ) : (
              <Mic size={18} />
            )}
          </button>
        )}

        {!recordedAudioBlob && !isRecording && (
          <button
            className="chat-input__icon-btn"
            onClick={handleAudioClick}
            type="button"
            aria-label="Attach file"
          >
            <Paperclip size={18} />
          </button>
        )}

        <input
          ref={fileInputRef}
          type="file"
          accept="audio/*"
          onChange={(e) => {
            console.log("INPUT TRIGGERED");
            handleAudioUpload(e);
          }}
          style={{ display: "none" }}
        />

        {recordedAudioBlob ? (
          <div className="chat-input__recording-overlay" dir={isRTL ? 'rtl' : 'ltr'} style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
            <button className="chat-input__icon-btn" onClick={onCancelAudio} type="button" title="Discard">
              <Trash2 size={18} color="#ff4d4f" />
            </button>
            <span style={{ flex: 1, padding: '0 12px', fontSize: '0.95rem', color: 'var(--text-secondary)' }}>
              Audio ready to send
            </span>
          </div>
        ) : isRecording ? (
          <div className="chat-input__recording-overlay" dir={isRTL ? 'rtl' : 'ltr'} style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
            <div className="chat-input__recording-dot"></div>
            <span>{t.recording}</span>
            <div style={{ flex: 1 }}></div>
            <button className="chat-input__icon-btn" onClick={onCancelAudio} type="button" title="Cancel recording" style={{marginRight: '8px'}}>
              <Trash2 size={18} color="#ff4d4f" />
            </button>
            <button className="chat-input__icon-btn" onClick={onToggleMic} type="button" title="Stop recording">
              <Square size={18} fill="currentColor" color="var(--text-secondary)" />
            </button>
          </div>
        ) : (
          <textarea
            className="chat-input__textarea"
            ref={inputRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={currentPlaceholder}
            disabled={disabled}
            dir={isRTL ? 'rtl' : 'ltr'}
          />
        )}

        {recordedAudioBlob ? (
          <button
            className="chat-input__send-btn"
            onClick={onSendAudio}
            disabled={disabled}
            type="button"
            style={{ background: 'var(--primary)', color: 'white' }}
          >
            <Send size={18} />
          </button>
        ) : (
          <button
            className="chat-input__send-btn"
            onClick={handleSend}
            disabled={!input.trim() || disabled || isRecording}
            type="button"
          >
            <Send size={18} />
          </button>
        )}
      </div>

      <p className="chat-input__disclaimer">
        {t.disclaimer}
      </p>
    </div>
  );
}