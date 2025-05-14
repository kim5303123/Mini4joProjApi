from fastapi import APIRouter, HTTPException
from app.models.mail_tone import MailToneRequest, MailToneResponse
from app.services.mail_tone_service import convert_mail_tone
import traceback

router = APIRouter()

@router.post("/convert", response_model=MailToneResponse)
async def convert_mail_tone_endpoint(request: MailToneRequest):
    try:
        return await convert_mail_tone(request)
    except Exception as e:
        print("=== 예외 발생 ===")
        print(e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="메일 변환 중 오류가 발생했습니다.")
