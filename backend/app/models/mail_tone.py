from pydantic import BaseModel
from enum import Enum

class SituationEnum(str, Enum):
    payment = "결제"
    apology = "사과"
    work_request = "업무요청"

class RecipientEnum(str, Enum):
    external_mail = "외부 메일"
    internal_mail = "내부 메일"

class MailToneRequest(BaseModel):
    situation: SituationEnum
    recipient: RecipientEnum
    content: str

class MailToneResponse(BaseModel):
    original_content: str
    converted_content: str
