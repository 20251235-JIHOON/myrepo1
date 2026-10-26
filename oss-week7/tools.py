import requests
import json

def get_boxoffice_rank_1(data):
    params = {"key": "386d93494c22220536241345cf5d6663", "targetDt": data}
    response = requests.get(
        "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json",
        params=params, timeout=10
    )
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']


def get_movie_audience(date, title):
    """특정 날짜와 영화 제목을 입력받아 해당 영화의 관객 수를 반환하는 함수"""
    params = {"key": "386d93494c22220536241345cf5d6663", "targetDt": date}
    response = requests.get(
        "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json",
        params=params, timeout=10
    )
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    
    for movie in movies:
        if movie['movieNm'] == title:
            audience_num = int(movie['audiCnt'])
            return f"{audience_num:,}명"
            
    return f"'{title}' 은(는) {date} 순위에 없습니다."