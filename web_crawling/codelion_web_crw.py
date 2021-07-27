from os import write
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.daum.net'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a', 'link_favorsch')

rank = 1
# 오늘 날짜 출력
print(datetime.today().strftime('%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n'))
# 실시간 검색어 출력
for result in results:
	print(str(rank)+'위 : '+result.get_text()+'\n')
	rank += 1