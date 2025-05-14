import React, { useState } from 'react';
import './styles/App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [format, setFormat] = useState('');
  const formats = ['결제요청 메일', '사과 메일', '업무 협조 요청 메일'];

  const handleConvert = () => {
    console.log('입력 텍스트:', inputText);
    console.log('선택된 형식:', format);
    setOutputText(inputText);
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
            <h1>자연스러운 업무 메일 도우미</h1>
            <p>정중하고 상황에 맞는 메일을 빠르게 완성해보세요</p>
          </div>
        </div>
      </header>

      <div className="format-buttons-row">
        <span className="format-label">모드 :</span>
        <div className="format-buttons-wrapper">
          {formats.map((f) => (
            <button
              key={f}
              className={`format-btn${format === f ? ' selected' : ''}`}
              onClick={() => setFormat(f)}
              type="button"
            >
              {f}
            </button>
          ))}
        </div>
      </div>

      <main className="content-flex">
        <div className="box left-box">
          <h2>입력창</h2>
          <div className="input-area-wrapper">
            <textarea
              className="input-textarea"
              placeholder="여기에 문장을 입력하세요."
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
            />
            <div className="input-toolbar">
              {/* <span className="input-counter">{inputText.length} / 5000</span> */}
              <button className="convert-inline-btn" onClick={handleConvert}>변환하기</button>
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
