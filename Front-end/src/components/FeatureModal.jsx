import { useState, useEffect } from 'react';
import { X, Loader2, Cloud, TrendingUp, Wheat } from 'lucide-react';
import './FeatureModal.css';

const UI_TEXT = {
  en: {
    weather: 'Weather Forecast',
    market: 'Market Rates',
    agronomy: 'Agronomy Advice',
    loading: 'Loading...',
    error: 'Failed to load data.',
    price: 'Price (PKR)',
    unit: 'Unit',
    brand: 'Brand / Variety',
  },
  ur: {
    weather: 'موسم کی پیشن گوئی',
    market: 'مارکیٹ کے نرخ',
    agronomy: 'علم زراعت کی تجویز',
    loading: 'لوڈ ہو رہا ہے...',
    error: 'ڈیٹا لوڈ کرنے میں ناکام۔',
    price: 'قیمت (PKR)',
    unit: 'یونٹ',
    brand: 'برانڈ / قسم',
  },
  sd: {
    weather: 'موسم جي اڳڪٿي',
    market: 'مارڪيٽ جا اگهه',
    agronomy: 'علم زراعت جي صلاح',
    loading: 'لوڊ ٿي رهيو آهي...',
    error: 'ڊيٽا لوڊ ڪرڻ ۾ ناڪام.',
    price: 'قيمت (PKR)',
    unit: 'يونٽ',
    brand: 'برانڊ / قسم',
  },
  pa: {
    weather: 'موسم دی پیشنگوئی',
    market: 'مارکیٹ دے ریٹ',
    agronomy: 'علم زراعت دی صلاح',
    loading: 'لوڈ ہو رہیا اے...',
    error: 'ڈیٹا لوڈ کرن وچ ناکام۔',
    price: 'قیمت (PKR)',
    unit: 'یونٹ',
    brand: 'برانڈ / قسم',
  },
  ps: {
    weather: 'د موسم وړاندوینه',
    market: 'د بازار بیې',
    agronomy: 'کرنې مشوره',
    loading: 'بار کیږي...',
    error: 'د معلوماتو پورته کول ناکام شول.',
    price: 'بیه (PKR)',
    unit: 'یونټ',
    brand: 'نښه / ډول',
  }
};

const langMap = {
  en: "english",
  ur: "urdu",
  sd: "sindhi",
  pa: "punjabi",
  ps: "pashto",
};

export default function FeatureModal({ feature, language, onClose }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const t = UI_TEXT[language] || UI_TEXT.en;
  const isRTL = ['ur', 'sd', 'pa', 'ps'].includes(language);

  useEffect(() => {
    let isMounted = true;

    const getCurrentPosition = () =>
      new Promise((resolve, reject) => {
        if (!navigator.geolocation) {
          reject(new Error("Geolocation not supported."));
          return;
        }
        navigator.geolocation.getCurrentPosition(resolve, reject, {
          timeout: 10000,
        });
      });

    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        if (feature === 'weather') {
          const pos = await getCurrentPosition();
          const { latitude, longitude } = pos.coords;
          const res = await fetch(`http://127.0.0.1:8000/weather-forecast-10?lat=${latitude}&lon=${longitude}`);
          if (!res.ok) throw new Error("Weather fetch failed");
          const json = await res.json();
          if (isMounted) setData(json.list);
        } else if (feature === 'market') {
          const res = await fetch(`http://127.0.0.1:8000/market-rates-data`);
          if (!res.ok) throw new Error("Market fetch failed");
          const json = await res.json();
          if (isMounted) setData(json);
        } else if (feature === 'agronomy') {
          const pos = await getCurrentPosition().catch(() => ({ coords: { latitude: 30.3753, longitude: 69.3451 } })); // default to PK center if blocked
          const { latitude, longitude } = pos.coords;
          const month = new Date().toLocaleString('en-US', { month: 'long' });
          const res = await fetch(`http://127.0.0.1:8000/agronomy-advice`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ lat: latitude, lon: longitude, month, language: langMap[language] || 'english' })
          });
          if (!res.ok) throw new Error("Agronomy fetch failed");
          const json = await res.json();
          if (isMounted) setData(json.advice);
        }
      } catch (err) {
        console.error(err);
        if (isMounted) setError(t.error);
      } finally {
        if (isMounted) setLoading(false);
      }
    };

    fetchData();
    return () => { isMounted = false; };
  }, [feature, language, t.error]);

  const renderWeather = () => {
    if (!data || !Array.isArray(data)) return null;
    
    // Group by day or just show first 10 items (if it's 3-hour forecast, take 1 per day)
    // The daily api returns list of days. The 3-hour api returns 40 items.
    const isDaily = data[0]?.temp && typeof data[0].temp === 'object';
    
    let displayList = data;
    if (!isDaily && data.length > 10) {
      // Pick one forecast per day (e.g., around noon)
      const dailyMap = new Map();
      data.forEach(item => {
        const date = new Date(item.dt * 1000).toLocaleDateString();
        if (!dailyMap.has(date)) {
          dailyMap.set(date, item);
        }
      });
      displayList = Array.from(dailyMap.values()).slice(0, 10);
    }

    return (
      <div className="weather-grid">
        {displayList.map((item, i) => {
          const date = new Date(item.dt * 1000).toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric' });
          const temp = isDaily ? item.temp.day : item.main.temp;
          const icon = item.weather?.[0]?.icon;
          const desc = item.weather?.[0]?.description;
          return (
            <div key={i} className="weather-card">
              <div className="weather-card__date">{date}</div>
              {icon && <img src={`https://openweathermap.org/img/wn/${icon}@2x.png`} alt="weather" width="50" />}
              <div className="weather-card__temp">{Math.round(temp)}°C</div>
              <div className="weather-card__desc">{desc}</div>
            </div>
          );
        })}
      </div>
    );
  };

  const renderMarket = () => {
    if (!data || !Array.isArray(data)) return null;
    return (
      <div className="market-table-container">
        {data.map((cat, i) => (
          <div key={i}>
            <h3 className="market-category">{cat.category}</h3>
            <table className="market-table" dir={isRTL ? 'rtl' : 'ltr'}>
              <thead>
                <tr>
                  <th>{t.brand}</th>
                  <th>{t.price}</th>
                  <th>{t.unit}</th>
                </tr>
              </thead>
              <tbody>
                {cat.products.map((prod, j) => (
                  <tr key={j}>
                    <td>{prod.name}</td>
                    <td>Rs. {prod.price_pkr}</td>
                    <td>{prod.unit}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    );
  };

  const renderAgronomy = () => {
    if (!data) return null;
    return <div className="agronomy-content" dir={isRTL ? 'rtl' : 'ltr'}>{data}</div>;
  };

  const titles = {
    weather: { icon: Cloud, text: t.weather },
    market: { icon: TrendingUp, text: t.market },
    agronomy: { icon: Wheat, text: t.agronomy },
  };

  const { icon: Icon, text: titleText } = titles[feature] || titles.weather;

  return (
    <div className="feature-modal-overlay" onClick={onClose}>
      <div className="feature-modal" onClick={e => e.stopPropagation()} dir={isRTL ? 'rtl' : 'ltr'}>
        <div className="feature-modal__header">
          <h2 className="feature-modal__title" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Icon size={20} /> {titleText}
          </h2>
          <button className="feature-modal__close" onClick={onClose}><X size={20} /></button>
        </div>
        <div className="feature-modal__content">
          {loading ? (
            <div className="feature-modal__loading">
              <Loader2 size={32} className="lucide-spin" />
              <p>{t.loading}</p>
            </div>
          ) : error ? (
            <div className="feature-modal__error">{error}</div>
          ) : (
            <>
              {feature === 'weather' && renderWeather()}
              {feature === 'market' && renderMarket()}
              {feature === 'agronomy' && renderAgronomy()}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
