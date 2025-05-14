from pydantic import BaseModel
from enum import Enum

class Situation(str, Enum):
    report = "보고"
    question = "질문"
    meeting_request = "회의 요청"
    apology = "사과"
    data_request = "자료 요청"
    confirmation = "확인 요청"

class Receiver(str, Enum):
    boss = "상사"
    coworker = "동료"
    external_partner = "외부 파트너"

class MailTransformRequest(BaseModel):
    original_content: str
    situation: Situation
    receiver: Receiver

class MailTransformResponse(BaseModel):
    transformed_content: str 