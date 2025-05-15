from app.models.mail_tone import MailToneRequest, MailToneResponse
from app.utils.openai_client import get_openai_completion


def build_prompt(situation: str, recipient: str, content: str) -> str:
    # return (
    #     f"다음은 회사 이메일 작성 상황입니다.\n"
    #     f"상황: {situation}\n"
    #     f"수신자: {recipient}\n"
    #     f"원본 문장: {content}\n"
    #     f"""위 문장은 **신입사원이 작성한 미숙한 사과 이메일 문장**입니다.  
    #      이를 다음 기준에 맞춰 **정중하고 실무적으로 자연스러운 이메일 문장**으로 변환해 주세요:
    #      **정중하면서도 신뢰감 있는 톤**을 사용해 주세요.
    #      너무 장황하지 않고, **실제 사내 이메일에서 사용할 수 있는 현실적인 표현**을 사용해 주세요.

    #     - 출력은 변환된 문장만 보여 주세요. 설명은 하지 마세요."""
    # )
    return f"""
[역할]
당신은 해운/물류 업계 전문 에디터입니다. 
신입 사원이 작성한 초안을 아래 기준에 맞게 **실무용 이메일**로 변환해 주세요.

[수정 원칙]
1. **구조 고정**: 수신/발신 → 인사 → 본문 → 서명(ㅇㅇㅇ 배상) 형식 필수 유지
2. **핵심 정보 보존**: 
   - 선박명(VESSEL), VOY 번호, ETD/ETA 날짜
   - 화물 코드(ORDER NO), 포트 정보
   - 특이사항(방역, 입고지 등)
3. **업계 관행 반영**:
   - "캔슬되었사오니" → "취소되었사오니" (공식 문서체)
   - "확인 부탁드립니다" → "확인 부탁드립니다" (반말 X)
   - 영문 약어 사용 시 괄호 설명 추가(예: TRC(Transhipment Cargo))

[변환 예시]
■ 입력: 
"도쿄행 JP항공편 5월 스케쥴 변동. 월-금 OUT 캔슬. 항공기 정비 때문"

■ 출력:
안녕하세요.
4조해운항공 ㅇㅇㅇ입니다.

도쿄행 JP항공편의 5월 스케쥴 변동 관련 안내드립니다.
항공기 정비 사유로 인해 월요일-금요일 OUT 일정이 취소되었사오니 참고 부탁드립니다.

감사합니다.
ㅇㅇㅇ 배상

[실제 변환 요청]
상황: {situation}
수신자: {recipient}
원본 내용: {content}

→ 위 예시 형식과 동일하게 변환해주세요. 설명은 생략하고 결과만 출력합니다.
"""




async def convert_mail_tone(request: MailToneRequest) -> MailToneResponse:
    prompt = build_prompt(request.situation, request.recipient, request.content)
    converted = await get_openai_completion(prompt)
    return MailToneResponse(
        original_content=request.content,
        converted_content=converted
    )
