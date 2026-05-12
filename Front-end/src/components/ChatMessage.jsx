import { useMemo, useRef, useState, useEffect } from 'react';
import { Play, Pause, MoreHorizontal, Square, Trash2, User, Bot, Volume2 } from 'lucide-react';
import { parseMarkdown } from '../utils/parseMarkdown';
import './ChatMessage.css';

// ─── UI text translations ────────────────────────────────────
const UI_TEXT = {
  en: { you: 'You', ai: 'AI Assistant', stop: 'Stop', delete: 'Delete', readAloud: 'Read aloud' },
  ur: { you: 'آپ', ai: 'اے آئی معاون', stop: 'رکیں', delete: 'ڈیلیٹ', readAloud: 'زور سے پڑھیں' },
  sd: { you: 'توهان', ai: 'اي آئي مددگار', stop: 'بند', delete: 'ڊليٽ', readAloud: 'آواز سان پڙهو' },
  pa: { you: 'تسیں', ai: 'اے آئی مددگار', stop: 'رکو', delete: 'ڈیلیٹ', readAloud: 'اچی آواز نال پڑھو' },
  ps: { you: 'تاسو', ai: 'AI مرسته', stop: 'بندېدن', delete: 'ړنګول', readAloud: 'په غوږ واخلئ' }
};

/**
 * Beautiful audio player replacing the plain white HTML audio bar.
 * Shows waveform bars that animate while playing.
 */
function AudioPlayer({ src, onStop, onDelete, stopLabel, deleteLabel }) {
  const audioRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [duration, setDuration] = useState(0);
  const [currentTime, setCurrentTime] = useState(0);
  const [showActions, setShowActions] = useState(false);
  const animFrameRef = useRef(null);

  // Waveform bar heights (stable pseudo-random)
  const bars = useMemo(() => {
    return Array.from({ length: 28 }, (_, i) => {
      const seed = (i * 7919 + 12345) % 65536;
      return 0.25 + (seed / 65536) * 0.75;
    });
  }, []);

  const formatTime = (s) => {
    if (!isFinite(s) || isNaN(s)) return '0:00';
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return `${m}:${sec.toString().padStart(2, '0')}`;
  };

  const tick = () => {
    const el = audioRef.current;
    if (!el) return;
    setCurrentTime(el.currentTime);
    setProgress(el.duration ? (el.currentTime / el.duration) * 100 : 0);
    if (!el.paused) {
      animFrameRef.current = requestAnimationFrame(tick);
    }
  };

  useEffect(() => {
    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    };
  }, []);

  const togglePlay = () => {
    const el = audioRef.current;
    if (!el) return;
    if (el.paused) {
      el.play().catch(() => {});
      setIsPlaying(true);
      animFrameRef.current = requestAnimationFrame(tick);
    } else {
      el.pause();
      setIsPlaying(false);
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    }
  };

  const handleSeek = (e) => {
    const el = audioRef.current;
    if (!el || !el.duration) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const pct = x / rect.width;
    el.currentTime = pct * el.duration;
    setProgress(pct * 100);
  };

  return (
    <div className={`cm-audio ${isPlaying ? 'cm-audio--playing' : ''}`}>
      <audio
        ref={audioRef}
        src={src}
        preload="metadata"
        onLoadedMetadata={() => setDuration(audioRef.current?.duration || 0)}
        onEnded={() => { setIsPlaying(false); setProgress(0); setCurrentTime(0); }}
        onPlay={() => setIsPlaying(true)}
        onPause={() => setIsPlaying(false)}
      />

      {/* Play / Pause button */}
      <button className="cm-audio__play-btn" onClick={togglePlay} aria-label={isPlaying ? 'Pause' : 'Play'}>
        {isPlaying ? (
          <Pause size={16} fill="currentColor" />
        ) : (
          <Play size={16} fill="currentColor" />
        )}
      </button>

      {/* Waveform + scrub */}
      <div className="cm-audio__waveform-wrap" onClick={handleSeek}>
        <div className="cm-audio__waveform">
          {bars.map((h, i) => {
            const barPos = i / bars.length;
            const filled = barPos < progress / 100;
            return (
              <div
                key={i}
                className={`cm-audio__bar ${filled ? 'cm-audio__bar--filled' : ''} ${isPlaying ? 'cm-audio__bar--animated' : ''}`}
                style={{
                  height: `${h * 100}%`,
                  animationDelay: `${i * 0.04}s`,
                }}
              />
            );
          })}
        </div>
        {/* Progress overlay */}
        <div className="cm-audio__progress-track">
          <div className="cm-audio__progress-fill" style={{ width: `${progress}%` }} />
        </div>
      </div>

      {/* Time */}
      <span className="cm-audio__time">
        {formatTime(currentTime)} / {formatTime(duration)}
      </span>

      {/* More actions */}
      <button
        className="cm-audio__more-btn"
        onClick={() => setShowActions(p => !p)}
        aria-label="Audio actions"
      >
        <MoreHorizontal size={16} />
      </button>

      {showActions && (
        <div className="cm-audio__actions">
          <button
            className="cm-audio__action-btn"
            onClick={() => { audioRef.current?.pause(); setIsPlaying(false); onStop?.(); setShowActions(false); }}
          >
            <Square size={14} style={{ marginRight: '6px' }} /> {stopLabel}
          </button>
          <button
            className="cm-audio__action-btn cm-audio__action-btn--danger"
            onClick={() => { audioRef.current?.pause(); onDelete?.(); setShowActions(false); }}
          >
            <Trash2 size={14} style={{ marginRight: '6px' }} /> {deleteLabel}
          </button>
        </div>
      )}
    </div>
  );
}

/**
 * Individual chat message bubble.
 * Supports both user and AI messages with different styling.
 * AI messages render markdown content and include a speaker button for TTS.
 * Localized strings for all UI languages including Pashto.
 */
export default function ChatMessage({
  message,
  onSpeak,
  isSpeaking,
  language = 'en',
  onStopAudio,
  onDeleteAudio
}) {
  const isUser = message.role === 'user';
  const isStatus = message.role === 'status';
  const t = UI_TEXT[language] || UI_TEXT.en;

  // Parse markdown for AI messages
  const renderedContent = useMemo(() => {
    if (isUser || isStatus) return null;
    return parseMarkdown(message.text);
  }, [message.text, isUser, isStatus]);

  return (
    <div
      className={`chat-message ${
        isUser ? 'chat-message--user' : isStatus ? 'chat-message--status' : 'chat-message--ai'
      }`}
    >
      {/* Avatar */}
      <div
        className={`chat-message__avatar ${
          isUser ? 'chat-message__avatar--user' : 'chat-message__avatar--ai'
        }`}
      >
        {isUser ? (
          <User size={20} />
        ) : (
          <Bot size={20} />
        )}
      </div>

      {/* Message Content */}
      <div className="chat-message__content">
        <div className="chat-message__header">
          <span className="chat-message__sender">{isUser ? t.you : t.ai}</span>
          <span className="chat-message__time">{message.time}</span>
        </div>
        <div className="chat-message__bubble">
          {isUser ? (
            <p className="chat-message__text">{message.text}</p>
          ) : isStatus ? (
            <p className="chat-message__text chat-message__text--status">{message.text}</p>
          ) : (
            <div
              className="chat-message__markdown"
              dangerouslySetInnerHTML={{ __html: renderedContent }}
            />
          )}

          {!!message.audio_url && (
            <AudioPlayer
              src={`http://127.0.0.1:8000${message.audio_url}`}
              stopLabel={t.stop}
              deleteLabel={t.delete}
              onStop={onStopAudio}
              onDelete={() => onDeleteAudio?.(message.audio_url)}
            />
          )}
        </div>
        {/* TTS Button for AI messages */}
        {!isUser && !isStatus && (
          <button
            className={`chat-message__speak-btn ${isSpeaking ? 'chat-message__speak-btn--active' : ''}`}
            onClick={() => onSpeak(message.text)}
            title={t.readAloud}
          >
            <Volume2 size={16} />
          </button>
        )}
      </div>
    </div>
  );
}
