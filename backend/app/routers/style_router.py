from fastapi import APIRouter, HTTPException
from app.schemas.style import MailTransformRequest, MailTransformResponse
from app.services.style_service import transform_mail

router = APIRouter()

@router.post("/transform-mail", response_model=MailTransformResponse)
async def transform_mail_route(request: MailTransformRequest) -> MailTransformResponse:
    try:
        return await transform_mail(request)
    except Exception as exc:
        raise HTTPException(status_code=500, detail="메일 변환 중 오류가 발생했습니다.") from exc 