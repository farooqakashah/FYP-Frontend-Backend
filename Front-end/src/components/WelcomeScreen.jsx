import { ArrowDown } from 'lucide-react';
import './WelcomeScreen.css';

// ─── UI text translations ────────────────────────────────────
const UI_TEXT = {
  en: {
    title: 'AI Agriculture Assistant',
    subtitle: 'Your intelligent farming companion — ask about crops, weather, fertilizers, and more',
  },
  ur: {
    title: 'اے آئی زرعی معاون',
    subtitle: 'آپ کا ذہین کھیتی باڑی ساتھی — فصلوں، موسم، کھادوں اور مزید کے بارے میں پوچھیں',
  },
  sd: {
    title: 'اي آئي زرعي مددگار',
    subtitle: 'توهانجو سمجهدار کيتي ساٿي — فصلن، موسم، کادن ۽ وڌيڪ بابت پڇو',
  },
  pa: {
    title: 'اے آئی زرعی مددگار',
    subtitle: 'تہاڈا سیانا کھیتی ساتھی — فصلاں، موسم، کھاداں تے ہور بارے پچھو',
  },
  ps: {
    title: 'اي آئی کرنیز مرسته',
    subtitle: 'ستاسې هوښيار کرنیز ملگرے — په فصولو، هوا، خورو او نورو باندې پوښتنې.',
  }
};

/**
 * Welcome screen shown when there are no messages yet.
 * Displays only the hero: logo, title, subtitle.
 * Localized for English, Urdu, Sindhi, Punjabi, and Pashto.
 */
export default function WelcomeScreen({ language }) {
  const t = UI_TEXT[language] || UI_TEXT.en;
  const isRTL = ['ur', 'sd', 'pa', 'ps'].includes(language);

  return (
    <div className="welcome" dir={isRTL ? 'rtl' : 'ltr'}>
      <div className="welcome__hero">
        <div className="welcome__logo-glow">
          <img src="/newlogo.png" alt="Logo" className="welcome__logo" />
        </div>
        <h2 className="welcome__title">{t.title}</h2>
        <p className="welcome__subtitle">{t.subtitle}</p>

        {/* Decorative prompt hint */}
        <div className="welcome__hint">
          <span className="welcome__hint-arrow"><ArrowDown size={18} /></span>
          <span className="welcome__hint-text">
            {['ur','sd','pa','ps'].includes(language)
              ? 'نیچے ٹائپ کریں یا مائیک استعمال کریں'
              : 'Type below or use the microphone to begin'}
          </span>
        </div>
      </div>
    </div>
  );
}
