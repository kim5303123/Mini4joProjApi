from pydantic import BaseModel
from enum import Enum

class SituationEnum(str, Enum):
    report = "보고"
    request = "요청"
    data_delivery = "자료 전달"
    apology = "사과"
    meeting_request = "회의 요청"

class RecipientEnum(str, Enum):
    boss = "상사/팀장"
    coworker = "동료"
    external_client = "외부 고객"

class MailToneRequest(BaseModel):
    situation: SituationEnum
    recipient: RecipientEnum
    content: str

class MailToneResponse(BaseModel):
    original_content: str
    converted_content: str
