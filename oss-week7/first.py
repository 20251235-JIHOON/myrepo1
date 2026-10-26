from secret import API_KEY
import requests
import json

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
       "boxoffice/searchDailyBoxOfficeList.json")

params = {"key": API_KEY, "targetDt": "20260824"}

response = requests.get(url, params=params, timeout=10)

data = response.json()
result = data['boxOfficeResult']

movies = result['dailyBoxOfficeList']
for movie in movies[:5]:
    rank = movie['rank']
    name = movie['movieNm']
    audi = int(movie['audiCnt'])
    print(f"{rank}dnl {name} - {audi:,}명")
first = movies[0]
print(first['rank'])
print(first['movieNm'])
print(first['audiCnt'])
