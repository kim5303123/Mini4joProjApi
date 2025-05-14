from app.schemas.style import MailTransformRequest, MailTransformResponse
from app.utils.openai_client import get_openai_client

async def transform_mail(request: MailTransformRequest) -> MailTransformResponse:
    client = get_openai_client()
    prompt = _build_prompt(
        content=request.original_content,
        situation=request.situation.value,
        receiver=request.receiver.value
    )
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 한국어 비즈니스 메일 작성 전문가야."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=256,
        temperature=0.7
    )
    result = response.choices[0].message.content.strip()
    return MailTransformResponse(transformed_content=result)

def _build_prompt(content: str, situation: str, receiver: str) -> str:
    return (
        f"아래 문장을 상황({situation})과 대상({receiver})에 맞는 적절한 회사 메일 문장으로 변환해줘. 변환된 문장만 출력해줘.\n문장: {content}"
    ) 