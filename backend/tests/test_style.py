from app.models.mail_tone import SituationEnum, RecipientEnum, MailToneRequest

def test_mail_tone_request():
    req = MailToneRequest(
        situation=SituationEnum.report,
        recipient=RecipientEnum.boss,
        content="테스트 본문"
    )
    assert req.situation == SituationEnum.report
    assert req.recipient == RecipientEnum.boss
    assert req.content == "테스트 본문" 