from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

list = ['민소매', '반팔', '반바지', '원피스', '얇은 셔츠', '면바지', '얇은 가디건', '긴팔', '청바지', '얇은 니트', '맨투맨',
            '가디건', '자켓', '야상', '스타킹', '트렌츠 코트', '니트', '코트', '가죽 자켓', '레깅스', '패딩', '두꺼운 코트', '목도리', '기모제품']


def selectyourclothes(temp, root):

    min_text = []
    max_text = []
    select = []
    for i in root.iter('min'):
        min_text.append(float(i.text))
    for j in root.iter('max'):
        max_text.append(float(j.text))

    a = 0
    for i in range(0, 24):
        if min_text[i] <= temp <= max_text[i]:
            select.append(i)
            a += 1

    if a != 0:              # 범위내에 적절한 옷이 있을 때
        return select
    else:                   # 범위내에 적절한 옷이 없을 때
        b = 0
        tem = 0.5
        while b == 0:
            for j in range(0, 24):
                if min_text[j] <= temp + tem <= max_text[j]:
                    b += 1
                    select.append(j)
                if min_text[j] <= temp - tem <= max_text[j]:
                    b += 1
                    select.append(j)
            tem = tem + 0.5

        return select

def gettemperature(city):

    location = urllib.parse.quote(city + '+날씨')
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + location

    html = urlopen(url)
    html_source = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    cel = html_source.find('span', class_='sensible').find('span', class_='num').text

    return cel


def printclothes(select):
    clothes = []

    for s in select:
        clothes.append(list[s])

    return clothes

def saverecommendation(select, cel, city, y, m, d, h, mi):

    fp = open("myrecommendation.txt", 'wt')  # 최근 사용 정보 / 추천 서비스 사용 할 때 마다 그 때의 추천 정보와 기온 저장
    fp.write(str(1) + '\n')  # readline 해서 이전에 추천받은 내역이 있는지 없는지 확인
    fp.write('%d년 %d월 %d일 %d시 %d분 %s 체감 온도 %s°C\n' % (y, m, d, h, mi, city, cel))

    for s in select:  # 파일에 추천 내역 기록
        fp.write(list[s] + '\n')