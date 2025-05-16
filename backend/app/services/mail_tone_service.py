from app.models.mail_tone import MailToneRequest, MailToneResponse, SituationEnum, RecipientEnum
from app.utils.openai_client import get_openai_completion
from typing import Optional


def build_smart_email_prompt(
    content: str,
    situation: Optional[str] = None,
    recipient_type: Optional[str] = None
) -> str:
    """
    신입사원이 작성한 메일 초안을 기반으로, 상황에 맞는 실제 업무 이메일을 완성하는 GPT 프롬프트.
    - 이메일은 [수신인 정보] + [발신인 정보] + [인사말] + [본문] + [마무리/서명]의 기본 구조를 반드시 따라야 함
    - 출력은 설명 없이 실제 이메일 형식의 문장만 나오게 유도함
    """

    # 본문 구성 규칙 (상황별)
    situation_instruction = {
        "사과": """
1. 문제 발생 사실
2. 사과
3. 원인 간략 설명
4. 조치 사항 또는 해결 방안
5. 재발 방지 의지 및 협조 요청
        """,
        "협조": """
1. 요청 배경 설명
2. 요청 사항 구체화
3. 요청 목적 또는 협조 필요성 강조 (선택 사항)
4. 회신 방법 또는 기대 결과 안내
        """,
        "업무진행": """
1. 현재까지 진행된 업무 요약
2. 요약 전달 목적 또는 참고 방법 안내
3. 확인 또는 관련 질의 유도
4. 피드백 요청 또는 다음 단계 안내
        """
    }

    return f"""
다음은 신입사원이 회사 이메일을 작성하려고 남긴 초안입니다.

- 원문: "{content}"

GPT는 아래 조건에 따라 실제 업무용 이메일을 완성해 주세요.

이메일은 다음 구조를 반드시 포함해야 합니다:
1. 수신인 정보 
2. 발신인 정보 
3. 인사말 
4. 본문 (간결하고상황에 맞는 흐름을 반영)
5. 마무리 인사 + 서명 (예: 감사합니다. 이하나 배상)

   
- '수신인:' , '발신인:' 라벨만 출력하세요
- 인사말은 반드시 '안녕하세요 [발신인 정보]입니다.'로 시작해야 하며, 수신인 이름을 인사말에 부르지 마세요.
- 지시, 설명, 시스템 안내문은 절대 출력하지 마세요 
- 반드시 인사말은 발신인 정보를 포함해야 합니다.

상황: {situation or '자동 유추'}

본문 흐름 예시:
{situation_instruction.get(situation, '- 원문 내용에 맞게 자연스럽게 구성해 주세요.')}

※ 반드시 실제 메일처럼 자연스럽고 정중한 단락으로 출력해 주세요.
    """


async def convert_mail_tone(request: MailToneRequest) -> MailToneResponse:
    prompt = build_smart_email_prompt(
        content=request.content,
        situation=getattr(request, "situation", None),
        recipient_type=getattr(request, "recipient", None)
    )
    converted = await get_openai_completion(prompt)
    return MailToneResponse(
        original_content=request.content,
        converted_content=converted
    )
