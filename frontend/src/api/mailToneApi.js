import axios from 'axios';

/**
 * 메일 톤 변환 API 호출
 * @param {Object} params
 * @param {string} params.situation - 결재|사과|업무요청
 * @param {string} params.recipient - 외부 메일|내부 메일
 * @param {string} params.content - 원본 메일 내용
 * @returns {Promise<{original_content: string, converted_content: string}>}
 */
export async function convertMailTone({ situation, recipient, content }) {
  const response = await axios.post('http://localhost:8000/mail_tone/convert', {
    situation,
    recipient,
    content,
  });
  return response.data;
} 