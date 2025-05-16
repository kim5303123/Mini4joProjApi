from pydantic import BaseModel
from enum import Enum

class SituationEnum(str, Enum):
    payment = "협조"
    apology = "사과"
    work_request = "업무 진행 내용 전달"

class RecipientEnum(str, Enum):
    external_mail = "외부"
    internal_mail = "내부"

class MailToneRequest(BaseModel):
    situation: SituationEnum
    recipient: RecipientEnum
    content: str

class MailToneResponse(BaseModel):
    original_content: str
    converted_content: str
