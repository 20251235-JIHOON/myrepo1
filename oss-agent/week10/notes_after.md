작성: Claude Code / 확인: 원동진

# week09/tools.py 함수 정리

## 개요

- 영화진흥위원회 KOBIS 오픈 API(Open API, 공개 응용 프로그램 인터페이스)의 일별 박스오피스(box office, 흥행 순위) 엔드포인트(endpoint, 접속 주소)를 호출함
  - 주소: `searchDailyBoxOfficeList.json`
- API 키(key, 인증 열쇠)는 `secret.py`의 `API_KEY`에서 가져옴
- `requests` 라이브러리(library, 외부 코드 묶음)로 HTTP 요청(request, 서버에 보내는 질의)을 보냄
- 타임아웃(timeout, 응답 대기 제한 시간)은 10초임
- 함수는 2개임

## 함수 1. `get_boxoffice_rank_1(date)`

- 역할: 지정한 날짜의 박스오피스 1위 영화 제목을 돌려줌
- 입력: `date` (str, 문자열). 8자리 날짜임. 예: `"20261101"`
- 출력: (str, 문자열) 1위 영화 제목임. 예: `"오디세이"`
- docstring(독스트링, 함수 설명 주석): 있음
- 동작 순서
  - `key`와 `targetDt`(대상 날짜)를 파라미터(parameter, 요청 인자)에 담아 GET 요청(조회 요청)을 보냄
  - 응답 JSON(제이슨, 데이터 교환 형식)에서 `boxOfficeResult.dailyBoxOfficeList`(일별 순위 목록)를 꺼냄
  - 목록 첫 번째 항목의 `movieNm`(영화 이름)을 반환함

## 함수 2. `get_movie_audience(date, title)`

- 역할: 지정한 날짜에 지정한 영화의 일일 관객 수를 돌려줌
- 입력
  - `date` (str, 문자열): 8자리 날짜임
  - `title` (str, 문자열): 영화 제목임
- 출력: (str, 문자열)
  - 찾은 경우: 천 단위 쉼표를 붙인 관객 수임. 예: `"123,456명"`
  - 못 찾은 경우: `"'제목' 은(는) 날짜 순위에 없습니다."` 안내 문구임
- docstring(독스트링, 함수 설명 주석): 없음
- 동작 순서
  - 함수 1과 같은 방식으로 API를 호출해 순위 목록을 가져옴
  - 목록을 반복(loop, 루프)하며 `movieNm`(영화 이름)이 `title`과 정확히 같은 항목을 찾음
  - 찾으면 `audiCnt`(관객 수)를 정수(int, 인트)로 바꾸고 `"{관객수:,}명"` 형식으로 반환함
  - 끝까지 못 찾으면 안내 문구를 반환함

## 개선할 점

- `get_movie_audience`에 docstring(독스트링, 함수 설명 주석)이 없음
  - 에이전트(agent, 스스로 도구를 고르는 AI 프로그램)가 이 함수를 도구(tool, 호출 가능한 기능)로 쓸 때 설명이 부족할 수 있음
- 두 함수가 API 호출 코드와 목록 추출 코드를 똑같이 반복함. 공통 함수로 묶을 수 있음
- 에러 처리(error handling, 오류 대응)가 없음
  - 날짜가 잘못됐거나 API가 오류를 돌려주면 `KeyError`(키 없음 오류)가 날 수 있음
  - 목록이 비어 있으면 `IndexError`(위치 범위 초과 오류)가 날 수 있음
- 영화 제목이 정확히 같아야만 찾음. 띄어쓰기 차이나 부분 일치는 처리하지 않음
- 참고: CLAUDE.md 규칙에 따라 이번 작업에서 tools.py는 고치지 않음
