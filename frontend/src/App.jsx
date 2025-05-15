import React, { useState } from 'react';
import './styles/App.css';
import { convertMailTone } from './api/mailToneApi';

const formats = ['결제', '사과', '업무요청'];
const situationMap = {
  '결제': '결제',
  '사과': '사과',
  '업무요청': '업무요청',
};
const recipientMap = {
  '외부': '외부 메일',
  '내부': '내부 메일',
};

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [selectedSituation, setSelectedSituation] = useState('');
  const [selectedTarget, setSelectedTarget] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const to = ['외부', '내부'];

  const handleConvert = async () => {
    setError('');
    if (!selectedSituation || !selectedTarget || !inputText) {
      setError('상황, 대상, 내용을 모두 입력해 주세요.');
      return;
    }
    setLoading(true);
    setOutputText('');
    try {
      const res = await convertMailTone({
        situation: situationMap[selectedSituation],
        recipient: recipientMap[selectedTarget],
        content: inputText,
      });
      setOutputText(res.converted_content);
    } catch (e) {
      setError('변환 중 오류가 발생했습니다.');
    } finally {
      setLoading(false);
    }
  };

  const getTemplate = (situation) => {
    switch (situation) {
      case '결제':
        return `예시) 안녕하세요, OOO입니다.\n이번 달 OO비용에 대한 결제를 요청드립니다.\n확인 부탁드립니다.`;
      case '사과':
        return `예시) 안녕하세요, OOO입니다.\n이번 일에 대해 불편을 드려 정말 죄송합니다.\n다시는 같은 일이 발생하지 않도록 주의하겠습니다.`;
      case '업무요청':
        return `예시) 안녕하세요, OOO입니다.\nOO 프로젝트와 관련하여 협조 요청드립니다.\n자세한 사항은 아래 내용을 참고해 주세요.`;
      default:
        return `예시) 안녕하세요, OOO입니다.\n저는 OO팀에서 OO업무를 담당하고 있는 OOO입니다.\n이번에 OO 관련하여 문의드립니다.`;
    }
  };

  return (
    <div className="main-wrapper">
      <header className="page-title">
        <div className="title-row">
          <img
            src="/assets/Code snippets-cuate.png"
            alt="일러스트"
            className="hero-illustration"
          />
          <div className="title-text">
            <h1>개떡을 찰떡으로!</h1>
            <p>정중하고 상황에 맞는 메일을 빠르게 완성해보세요</p>
          </div>
        </div>
      </header>
      <div className="format-container">
        <div className="format-buttons-row">
          <div className="format-group">
            <span className="format-label">상황 :</span>
            <div className="format-buttons-wrapper">
              {formats.map((f) => (
                <button
                  key={f}
                  className={`format-btn${selectedSituation === f ? ' selected' : ''}`}
                  onClick={() => setSelectedSituation(f)}
                  type="button"
                >
                  {f}
                </button>
              ))}
            </div>
          </div>

          <div className="format-group">
            <span className="format-label">대상 :</span>
            <div className="format-buttons-wrapper">
              {to.map((t) => (
                <button
                  key={t}
                  className={`format-btn${selectedTarget === t ? ' selected' : ''}`}
                  onClick={() => setSelectedTarget(t)}
                  type="button"
                >
                  {t}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      <main className="content-flex">
        <div className="box left-box">
          <h2>입력창</h2>
          <div className="input-area-wrapper">
            <div className="textarea-wrapper">
              <div className="template-preview">
                {getTemplate(selectedSituation)}
              </div>
              <textarea
                className="input-textarea"
                placeholder="이 아래에 내용을 작성해 주세요"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
              />
              <div className="input-toolbar">
                <button className="convert-inline-btn" onClick={handleConvert} disabled={loading}>
                  {loading ? '변환 중...' : '변환하기'}
                </button>
              </div>
              {error && <div className="error-message">{error}</div>}
            </div>
          </div>
        </div>

        <div className="arrow-image-wrapper">
          <img src="/assets/arrow4.png" alt="화살표" className="arrow-image" />
        </div>

        <div className="box right-box">
          <h2>변환 결과창</h2>
          <div className="result-area">
            {outputText || '변환된 문장이 여기에 표시됩니다.'}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
