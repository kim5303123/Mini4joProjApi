import pytest
from httpx import AsyncClient
from app.main import app
from app.schemas.style import Situation, Receiver

@pytest.mark.asyncio
async def test_transform_mail():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
            "original_content": "자료를 내일까지 보내드리겠습니다.",
            "situation": Situation.report.value,
            "receiver": Receiver.boss.value
        }
        response = await ac.post("/transform-mail", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "transformed_content" in data
        assert isinstance(data["transformed_content"], str) 