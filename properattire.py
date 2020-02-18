from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from datetime import datetime

list = ['민소매', '반팔', '반바지', '원피스', '얇은 셔츠', '면바지', '얇은 가디건', '긴팔', '청바지', '얇은 니트', '맨투맨',
        '가디건', '자켓', '야상', '스타킹', '트렌츠 코트', '니트', '코트', '가죽 자켓', '레깅스', '패딩', '두꺼운 코트', '목도리', '기모제품']

doc = ET.parse('clotheslist.xml')
root = doc.getroot()

min_text = []
max_text = []
select = []

for i in root.iter('min'):
    min_text.append(float(i.text))
for j in root.iter('max'):
    max_text.append(float(j.text))


def toohot(temp, s1):
    string = 'clothes' + str(s1)

    for c in root.findall(string):
        c.find('min').text = str(temp)
        if float(c.find('min').text) > float(c.find('max').text):
            c.find('max').text = str(temp)

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')

    return


def toocold(temp, s1):
    string = 'clothes' + str(s1)

    for c in root.findall(string):
        c.find('max').text = str(temp)
        if float(c.find('max').text) < float(c.find('min').text):
            c.find('min').text = str(temp)

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')

    return


def selectyourclothes(temp):
    a = 0
    for i in range(0, 24):
        if min_text[i] <= temp <= max_text[i]:  # 범위내에 적절한 옷이 있을 때
            select.append(i)
            a += 1
    if a != 0:
        return select
    else:
        b = 0
        t = temp
        while b == 0:
            for j in range(0, 24):
                if min_text[j] <= t + 1 <= max_text[j]:
                    b += 1
                    select.append(j)
                if min_text[j] <= t - 1 <= max_text[j]:
                    b += 1
                    select.append(j)
        return select


loop = 1
while loop > 0:
    try:
        check = int(input('1. 추천받기\n2. 평가하기\n3. 종료하기\n--------------------\n'))
        if check == 1:

            city = input('도시를 입력하세요: ')
            location = urllib.parse.quote(city + '+날씨')
            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + location

            html = urlopen(url)
            html_source = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
            cel = html_source.find('span', class_='sensible').find('span', class_='num').text

            print('%s의 현재 체감 온도는 %s도 입니다.' % (city, cel))
            select = selectyourclothes(float(cel))

            y = datetime.today().year
            m = datetime.today().month
            d = datetime.today().day
            h = datetime.today().hour
            mi = datetime.today().minute

            fp = open("myrecommendation.txt", 'wt')  # 최근 사용 정보 / 추천 서비스 사용 할 때 마다 그 때의 추천 정보와 기온 저장
            fp.write(str(1) + '\n')                  # readline 해서 이전에 추천받은 내역이 있는지 없는지 확인
            fp.write('%d년 %d월 %d일 %d시 %d분 %s\n' % (y, m, d, h, mi, city))
            fp.write('체감 온도가 ' + str(cel) + '일 때\n')

            for s in select:                        # 추천 내역 화면에 출력 / 파일에 추천 내역 기록
                print(str(s) + ' ' + list[s])
                fp.write(str(s) + ' ' + list[s] + '\n')

            fp.close()

        elif check == 3:
            loop = 0

        elif check == 2:

            f = open('myrecommendation.txt', 'rt')
            fir = f.readline()                      # 이전 추천 내역이 있는지 없는지 확인

            if fir == '0':
                print('추천받은 내역이 없습니다.')
                f.close()
            else:
                print('최근 추천 내역은 다음과 같습니다.\n')
                print(f.read())
                f.close()
                s1 = int(input('항목을 선택하세요> '))
                s2 = int(input('1. 더웠음 2. 적절 3. 추움 >'))

                if s2 == 1:
                    toohot(cel, s1)
                if s2 == 3:
                    toocold(cel, s1)

    except:
        print('입력을 확인 해 주세요.\n')
        loop = 1
