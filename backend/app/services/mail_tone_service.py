from app.models.mail_tone import MailToneRequest, MailToneResponse
from app.utils.openai_client import get_openai_completion


def build_prompt(situation: str, recipient: str, content: str) -> str:
    return (
        f"다음은 회사 이메일 작성 상황입니다.\n"
        f"상황: {situation}\n"
        f"수신자: {recipient}\n"
        f"원본 문장: {content}\n"
        f"상황과 수신자에 맞는 예의 바르고 자연스러운 이메일 문장으로 변환해 주세요. "
        f"불필요한 설명 없이 변환된 문장만 출력해 주세요."
    )


async def convert_mail_tone(request: MailToneRequest) -> MailToneResponse:
    prompt = build_prompt(request.situation, request.recipient, request.content)
    converted = await get_openai_completion(prompt)
    return MailToneResponse(
        original_content=request.content,
        converted_content=converted
    )
