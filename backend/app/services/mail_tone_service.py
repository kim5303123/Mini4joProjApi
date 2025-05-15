from app.models.mail_tone import MailToneRequest, MailToneResponse
from app.utils.openai_client import get_openai_completion


def build_prompt(situation: str, recipient: str, content: str) -> str:
    return (
        f"다음은 회사 이메일 작성 상황입니다.\n"
        f"상황: {situation}\n"
        f"수신자: {recipient}\n"
        f"원본 문장: {content}\n"

        f"""위 문장은 **신입사원이 작성한 미숙한 사과 이메일 문장**입니다.  
        이를 다음 기준에 맞춰 **정중하고 실무적으로 자연스러운 사과 이메일 문장**으로 변환해 주세요:

        1. **구체적인 잘못된 내용**이 드러나도록 표현해 주세요. (예: 어떤 오류인지)
        2. **책임을 회피하지 말고** 사과의 의도를 명확히 표현해 주세요.
        3. **해결 조치 또는 재발 방지 방안**을 포함해 주세요.
        4. **정중하면서도 신뢰감 있는 톤**을 사용해 주세요.
        5. 너무 장황하지 않고, **실제 사내 이메일에서 사용할 수 있는 현실적인 표현**을 사용해 주세요.

        - 출력은 변환된 문장만 보여 주세요. 설명은 하지 마세요."""
    )





async def convert_mail_tone(request: MailToneRequest) -> MailToneResponse:
    prompt = build_prompt(request.situation, request.recipient, request.content)
    converted = await get_openai_completion(prompt)
    return MailToneResponse(
        original_content=request.content,
        converted_content=converted
    )
