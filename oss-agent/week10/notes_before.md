# week09/tools.py 함수 정리 (수정 전)

## 개요

- 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 엔드포인트(`searchDailyBoxOfficeList.json`)를 호출한다.
- API 키는 `secret.py`의 `API_KEY`에서 가져온다.
- 외부 라이브러리로 `requests`를 쓴다. 요청 타임아웃은 10초다.

## 함수 목록

### 1. `get_boxoffice_rank_1(date)`

특정 날짜의 박스오피스 **1위 영화 제목**을 돌려준다.

| 항목 | 내용 |
|---|---|
| 입력 | `date` (str): 8자리 날짜, 예 `"20261101"` |
| 출력 | (str): 1위 영화 제목, 예 `"오디세이"` |
| docstring | 있음 |

동작:
1. `key`와 `targetDt`를 파라미터로 넣어 API에 GET 요청을 보낸다.
2. 응답 JSON에서 `boxOfficeResult.dailyBoxOfficeList`를 꺼낸다.
3. 리스트 첫 번째 항목의 `movieNm`을 반환한다.

### 2. `get_movie_audience(date, title)`

특정 날짜에 특정 영화의 **일일 관객 수**를 돌려준다.

| 항목 | 내용 |
|---|---|
| 입력 | `date` (str): 8자리 날짜 / `title` (str): 영화 제목 |
| 출력 | (str): 천 단위 쉼표가 붙은 관객 수, 예 `"123,456명"`. 순위에 없으면 `"'제목' 은(는) 날짜 순위에 없습니다."` |
| docstring | **없음** |

동작:
1. `get_boxoffice_rank_1`과 같은 방식으로 API를 호출해 박스오피스 목록을 가져온다.
2. 목록을 돌면서 `movieNm`이 `title`과 **정확히 일치하는** 영화를 찾는다.
3. 찾으면 `audiCnt`를 정수로 바꾸고 `"{관객수:,}명"` 형식으로 반환한다.
4. 못 찾으면 "순위에 없습니다" 안내 문자열을 반환한다.

## 눈에 띄는 점 (개선할 거리)

- `get_movie_audience`에 docstring이 없다. 에이전트가 이 함수를 도구로 쓸 때 설명이 부족할 수 있다.
- 두 함수가 API 호출과 목록 추출 코드를 똑같이 반복한다. 공통 함수로 묶을 수 있다.
- 에러 처리가 없다. 날짜가 잘못됐거나 API가 오류를 돌려주면 `KeyError`가 나고, 목록이 비어 있으면 `IndexError`가 난다.
- 제목은 완전히 일치해야만 찾는다. 띄어쓰기나 부분 일치는 처리하지 않는다.
