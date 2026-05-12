import './TypingIndicator.css';

// ─── UI text translations ────────────────────────────────────
const THINKING_TEXT = {
  en: 'AI is thinking',
  ur: 'اے آئی سوچ رہا ہے',
  sd: 'اي آئي سوچي رهيو آهي',
  pa: 'اے آئی سوچ رہیا اے',
  ps: 'AI فکر کوي'
};

const VOICE_TEXT = {
  en: 'Processing voice',
  ur: 'آواز پروسیس ہو رہی ہے',
  sd: 'آواز پروسيس ٿي رهيو آهي',
  pa: 'آواز پروسیس ہو رہیا اے',
  ps: 'د غږ پروسس روان دی'
};

/**
 * Animated typing indicator shown when "AI is thinking" or "Processing voice".
 * Three bouncing dots with a label.
 * Thinking label localized for each supported language including Pashto.
 */
export default function TypingIndicator({ language, mode = 'text' }) {
  const isRTL = ['ur', 'sd', 'pa', 'ps'].includes(language);
  const textDict = mode === 'voice' ? VOICE_TEXT : THINKING_TEXT;
  const text = textDict[language] || textDict.en;

  return (
    <div className="typing-indicator" dir={isRTL ? 'rtl' : 'ltr'}>
      <div className="typing-indicator__avatar">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66.95-2.3c.48.17.98.3 1.34.3C19 20 22 3 22 3c-1 2-8 2.25-13 3.5S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z" />
        </svg>
      </div>
      <div className="typing-indicator__content">
        <span className="typing-indicator__label">{text}</span>
        <div className="typing-indicator__dots">
          <span className="typing-indicator__dot" />
          <span className="typing-indicator__dot" />
          <span className="typing-indicator__dot" />
        </div>
      </div>
    </div>
  );
}