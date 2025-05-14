# 메일 문장 변환 웹 서비스

이 프로젝트는 사회 초년생/신입사원이 회사 메일을 작성할 때, 상황(보고, 질문, 회의 요청, 사과, 자료 요청, 확인 요청)과 대상(상사, 동료, 외부 파트너)에 맞는 분위기로 문장을 변환해주는 웹 서비스입니다.

## 주요 기능
- 사용자가 입력한 메일 내용을 상황과 대상에 맞게 자동 변환
- FastAPI 기반 REST API 제공
- OpenAI 등 LLM 활용(프롬프트 엔지니어링)
- 프론트엔드: 정적 HTML (static/)

## 디렉터리 구조
- app/: FastAPI 백엔드 코드
  - routers/: 라우터
  - schemas/: Pydantic 모델
  - services/: 비즈니스 로직
  - utils/: 유틸리티
  - types/: Enum 등 타입 정의
- static/: 정적 파일(HTML)
- tests/: 테스트 코드

## 실행 방법
```bash
uvicorn app.main:app --reload
```
