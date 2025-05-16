from app.models.mail_tone import MailToneRequest, MailToneResponse, SituationEnum, RecipientEnum
from app.utils.openai_client import get_openai_completion
from typing import Optional


def build_full_mail_prompt(
    content: str,
    situation: Optional[str] = None,
    recipient_type: Optional[str] = None,
    recipient_name: Optional[str] = None
) -> str:
    """
    신입사원이 작성한 이메일 초안을 기반으로,
    상황 및 수신자 유형이 명시되지 않아도 GPT가 유추하여
    수신인 / 발신인 / 인사 / 본문 / 마무리 / 서명으로 구성된 완전한 이메일을 생성하게 유도하는 프롬프트입니다.
    """
    # 수신자 이름 포맷
    recipient_display = f"{recipient_name}님" if recipient_name else "수신자"

    # 상황 텍스트 조건 분기
    situation_text = (
        f"- 상황: {situation}\n"
    )

    # 메일 유형 조건 분기
    recipient_type_text = (
        f"- 메일 유형: {recipient_type}\n"
    )

    prompt = (
        f"다음은 신입사원이 회사 이메일을 작성하려고 쓴 초안입니다.\n\n"
        f"- 원문: \"{content}\"\n"
        f"- 수신자: {recipient_display}\n"
        f"{situation_text}{recipient_type_text}\n"
        f"아래 기준에 따라 ** 수신인 / 발신인 / 인사 / 본문 / 마무리 / 서명**으로 구성된 이메일을 완성해 주세요.\n\n"
        f"구성 기준:\n"
        f"1. **입력 문장을 최대한 해석하여** 상황(결재, 사과, 요청 등)을 파악하고 어울리는 이메일을 자연스럽게 작성해 주세요.\n"
        f"2. **수신인 / 발신인 / 인사 / 본문 / 마무리 / 서명**의 각 구성 요소는 실제 메일처럼 단락으로 구분하고, 라벨('제목:' 등)은 출력하지 마세요.\n"
        f"   **특히, 발신인 다음에는 반드시 한 줄(엔터) 띄우고 인사말이 시작되게 해 주세요.**\n"
        f"3. **수신인/발신인 정보가 없으면, 절대 임의로 이름을 채우지 말고, '수신인: ', '발신인: '처럼 콜론 뒤를 비워 두세요.**\n"
        f"4. **입력에 없는 정보(예: 금액, 첨부파일, 파일명 등)는 절대 임의로 추가하지 마세요.**\n"
        f"5. **GPT의 안내문, 요청문, 사과문 등은 출력하지 마세요.**\n"
        f"6. 메일은 실무에서 바로 사용할 수 있을 만큼 자연스럽고 예의 바른 표현으로 작성해 주세요.\n\n"
        f"출력은 완성된 메일처럼 보여 주세요. 반드시 설명 없이 본문만 출력해 주세요.\n"
        f"제목은 본문의 내용을 한눈에 알아볼 수 있도록 함축적으로 작성해 주세요.\n"
        f"수신인과 발신인이 없다면 최상단에 '수신인: ', '발신인: '을 추가하고, 콜론 뒤는 공란으로 남겨 두세요.\n"
    )
    return prompt


async def convert_mail_tone(request: MailToneRequest) -> MailToneResponse:
    prompt = build_full_mail_prompt(
        content=request.content,
        situation=getattr(request, "situation", None),
        recipient_type=getattr(request, "recipient", None),
        recipient_name=getattr(request, "recipient_name", None)
    )
    converted = await get_openai_completion(prompt)
    return MailToneResponse(
        original_content=request.content,
        converted_content=converted
    )


