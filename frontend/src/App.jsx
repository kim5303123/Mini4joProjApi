import React, { useState } from 'react';
import './styles/App.css';
import { convertMailTone } from './api/mailToneApi';
import { ChevronsRight } from 'lucide-react';

const formats = ['협조', '사과', '업무 진행 내용 전달'];
const situationMap = {
  '협조': '협조',
  '사과': '사과',
  '업무 진행 내용 전달': '업무 진행 내용 전달',
};
const recipientMap = {
  '외부': '외부',
  '내부': '내부',
};

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [selectedSituation, setSelectedSituation] = useState('협조');
  const [selectedTarget, setSelectedTarget] = useState('내부');
  const [loading, setLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState('');
  const [showToast, setShowToast] = useState(false);
  const to = ['외부', '내부'];

  const handleConvert = async () => {
    if (!selectedSituation || !selectedTarget || !inputText) {
      setModalMessage('상황, 대상, 내용을 모두 입력해 주세요.');
      setShowModal(true);
      return;
    }
    setLoading(true);
    setOutputText('');
    try {
      const params = {
        situation: situationMap[selectedSituation],
        recipient: recipientMap[selectedTarget],
        content: inputText,
      };
      console.log(params);
      const res = await convertMailTone(params);
      setOutputText(res.converted_content);
    } catch (e) {
      setModalMessage('변환 중 오류가 발생했습니다.');
      setShowModal(true);
    } finally {
      setLoading(false);
    }
  };

  const getTemplate = (situation) => {
    switch (situation) {
      case '협조':
        return `예시) 안녕하세요\n○○건 확인 좀 해주실게 있어서 메일 드립니다.\n내용 보시고 가능하시면 회신 부탁드려요`;
      case '사과':
        return `예시) 안녕하세요 ○○님\n오늘 보낸 자료에 숫자 하나 잘못 들어간 거 같아서요\n다시 정리해서 보내드릴게요, 지금 확인 부탁드려요`;
      case '업무 진행 내용 전달':
        return `예시) 안녕하세요.\n지금까지 한 부분 정리해서 보내드립니다.\n한번 보시고 필요한 거 있으시면 말씀 주세요`;
      default:
        return `예시) 안녕하세요, OOO입니다.\n저는 OO팀에서 OO업무를 담당하고 있는 OOO입니다.\n이번에 OO 관련하여 문의드립니다.`;
    }
  };

  const handleCopyOutput = () => {
    if (!outputText) return;
    navigator.clipboard.writeText(outputText);
    setShowToast(true);
    setTimeout(() => setShowToast(false), 2000);
  };

  return (
    <div className="main-wrapper">
      {showModal && (
        <div className="custom-modal-overlay">
          <div className="custom-modal-box">
            <img src="/assets/logo4.png" alt="로고" className="custom-modal-logo" />
            <div className="custom-modal-message">{modalMessage}</div>
            <button className="custom-modal-btn" onClick={() => setShowModal(false)}>
              확인
            </button>
          </div>
        </div>
      )}
      {showToast && (
        <div className="toast-message">복사되었습니다!</div>
      )}
      <header className="page-title">
        <div className="title-row">
          <img src="/assets/logo4.png" alt="로고" className="hero-illustration" />
          <div className="title-text">
            <div className="title-main-row">
              <h1 className="title-main">개떡에서 찰떡으로!</h1>
            </div>
            <p className="title-sub">정중하고 상황에 맞는 메일을 빠르게 완성해보세요</p>
          </div>
        </div>
      </header>


      <section className="selector-section">
        <div className="selector-group">
          <span className="selector-label">상황 :</span>
          <div className="selector-buttons">
            {formats.map((f) => (
              <button
                key={f}
                className={`selector-btn${selectedSituation === f ? ' selected' : ''}`}
                onClick={() => setSelectedSituation(f)}
              >
                {f}
              </button>
            ))}
          </div>
        </div>

        <div className="selector-group">
          <span className="selector-label">대상 :</span>
          <div className="selector-buttons">
            {to.map((t) => (
              <button
                key={t}
                className={`selector-btn${selectedTarget === t ? ' selected' : ''}`}
                onClick={() => setSelectedTarget(t)}
              >
                {t}
              </button>
            ))}
          </div>
        </div>
      </section>

      <main className="content-flex">
        <section className={`input-section ${outputText ? 'converted' : ''}`}>
          <h2>전하고 싶은 말</h2>
          <div className="textarea-wrapper">
            <div className="template-preview">{getTemplate(selectedSituation)}</div>
            <div className="template-divider" />
            <textarea
              className="input-textarea"
              placeholder="이 아래에 내용을 작성해 주세요"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
            />
            <div className="input-toolbar">
              <button
                className="convert-inline-btn"
                onClick={handleConvert}
                disabled={loading}
              >
                {loading ? '변환 중...' : '변환하기'}
              </button>
            </div>
          </div>
        </section>

        <div className="arrow-image-wrapper">
          <ChevronsRight className={`arrow-icon arrow1 ${loading ? 'arrow-animate1' : ''}`} />
          <ChevronsRight className={`arrow-icon arrow2 ${loading ? 'arrow-animate2' : ''}`} />
        </div>

        <section className={`output-section ${outputText ? 'converted' : ''}`}>
          <h2>다듬어진 말</h2>
          <div className="result-wrapper">
            <div
              className="result-area"
              tabIndex={0}
              onClick={handleCopyOutput}
            >
              {outputText || '변환된 문장이 여기에 표시됩니다.'}
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
