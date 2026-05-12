import { useState, useEffect } from 'react';
import { Menu, ArrowLeft, MessageSquarePlus, CloudSun, TriangleAlert, WifiOff, Cloud } from 'lucide-react';
import './Header.css';

// ─── UI text translations ────────────────────────────────────
const UI_TEXT = {
  en: { title: 'AI Agriculture Assistant', subtitle: 'Your Smart Farming Companion', offline: 'Offline Mode', newChat: 'New Chat', back: 'Back' },
  ur: { title: 'اے آئی زرعی معاون', subtitle: 'آپ کا ذہین کھیتی باڑی ساتھی', offline: 'آف لائن موڈ', newChat: 'نئی چیٹ', back: 'واپس' },
  sd: { title: 'اي آئي زرعي مددگار', subtitle: 'توهانجو سمجهدار کيتي ساٿي', offline: 'آف لائن', newChat: 'نئين چيٽ', back: 'واپس' },
  pa: { title: 'اے آئی زرعی مددگار', subtitle: 'تہاڈا سیانا کھیتی ساتھی', offline: 'آف لائن', newChat: 'نویں چیٹ', back: 'واپس' },
  ps: { title: 'اي آئی کرنیزی مرسته', subtitle: 'ستاسو هوښيار کرنیز ملگری', offline: 'آف لائن', newChat: 'نوې خبرې', back: 'بیرته' }
};

// Language buttons config
const LANG_OPTIONS = [
  { code: 'en', label: 'EN', title: 'Switch to English' },
  { code: 'ur', label: 'اردو', title: 'اردو میں تبدیل کریں' },
  { code: 'sd', label: 'سنڌي', title: 'سنڌيءَ ۾ تبديل ڪريو' },
  { code: 'pa', label: 'پنجابی', title: 'پنجابی وچ بدلو' },
  { code: 'ps', label: 'پښتو', title: 'پښتو ته بدل کړئ' }
];

/**
 * Header component with:
 * - App branding (logo + title)
 * - Language toggle inline (page-reloads on change)
 * - Compact live weather pill from API
 * - Mobile menu toggle
 */
export default function Header({ language, onLanguageChange, onMenuToggle, onNewChat, hasMessages, weather, weatherLoading, weatherError }) {
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  // Listen for online/offline events
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  const t = UI_TEXT[language] || UI_TEXT.en;

  // Lang change: save + reload (same as sidebar)
  const handleLangChange = (code) => {
    if (code === language) return;
    localStorage.setItem('agri_lang', code);
    onLanguageChange(code);
    setTimeout(() => window.location.reload(), 80);
  };

  // Weather display pill content
  const renderWeather = () => {
    if (weatherLoading) {
      return (
        <div className="header__weather header__weather--loading">
          <span className="header__weather-spinner" />
          <span className="header__weather-text">—</span>
        </div>
      );
    }
    if (weather) {
      return (
        <div className="header__weather">
          <span className="header__weather-icon"><CloudSun size={14} /></span>
          <span className="header__weather-city">{weather.city || '—'}</span>
          <span className="header__weather-divider" />
          <span className="header__weather-temp">
            {typeof weather.temperature === 'number' ? `${weather.temperature}°C` : '—'}
          </span>
          <span className="header__weather-humidity">
            💧{typeof weather.humidity === 'number' ? `${weather.humidity}%` : '—'}
          </span>
        </div>
      );
    }
    if (weatherError) {
      return (
        <div className="header__weather header__weather--unavailable">
          <span className="header__weather-icon"><TriangleAlert size={14} /></span>
          <span className="header__weather-text">Not Available</span>
        </div>
      );
    }
    return null;
  };

  return (
    <header className="header">
      {/* Mobile left-side controls */}
      <div className="header__mobile-left">
        {/* Mobile Menu Toggle */}
        <button className="header__menu-btn" onClick={onMenuToggle} aria-label="Toggle menu">
          <Menu size={22} />
        </button>

        {/* Mobile Back Button — shown when there are messages */}
        {hasMessages && (
          <button className="header__back-btn" onClick={onNewChat} aria-label={t.back} title={t.back}>
            <ArrowLeft size={20} />
          </button>
        )}
      </div>

      {/* Mobile New Chat Button — ALWAYS visible on mobile */}
      <button className="header__new-chat-btn" onClick={onNewChat} aria-label={t.newChat} title={t.newChat}>
        <MessageSquarePlus size={20} />
      </button>

      {/* App Logo & Title */}
      <div className="header__brand">
        <div className="header__logo-wrapper">
          <img src="/newlogo.png" alt="AI Agriculture Assistant Logo" className="header__logo" />
        </div>
        <div className="header__titles">
          <h1 className="header__title">{t.title}</h1>
          <p className="header__subtitle">{t.subtitle}</p>
        </div>
      </div>

      {/* Right side actions */}
      <div className="header__actions">
        {/* Live weather pill */}
        {renderWeather()}

        {/* Language Toggle */}
        <div className="header__lang-toggle">
          {LANG_OPTIONS.map(opt => (
            <button
              key={opt.code}
              className={`header__lang-btn ${language === opt.code ? 'header__lang-btn--active' : ''}`}
              onClick={() => handleLangChange(opt.code)}
              title={opt.title}
            >
              {opt.label}
            </button>
          ))}
        </div>

        {/* Offline indicator — only shown when offline */}
        {!isOnline && (
          <div className="header__status header__status--offline">
            <WifiOff size={14} className="header__status-icon header__status-icon--offline" />
            <span className="header__status-text">{t.offline}</span>
            <div className="header__status-dot header__status-dot--offline" />
          </div>
        )}
      </div>
    </header>
  );
}
