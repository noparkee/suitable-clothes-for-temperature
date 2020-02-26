from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET

list = ['민소매', '반팔', '반바지', '원피스', '얇은 셔츠', '면바지', '얇은 가디건', '긴팔', '청바지', '얇은 니트', '맨투맨',
            '가디건', '자켓', '야상', '스타킹', '트렌츠 코트', '니트', '코트', '가죽 자켓', '레깅스', '패딩', '두꺼운 코트', '목도리', '기모제품']

def findnumber(str):
    for i in range(0, 24):
        if str == list[i]:
            return i

def toocold(temp, s1):
    doc = ET.parse('clotheslist.xml')
    root = doc.getroot()

    string = 'clothes' + str(s1)
    t = temp + 0.3

    for c in root.findall(string):
        max = float(c.find('max').text)
        min = float(c.find('min').text)

        if min > temp:  # t 근처에 옷이 없는 경우, t가 min보다 작은데 추천되었고, 그에 대한 평가로 춥다고 할 때.
            min = min + 0.1
            c.find('min').text = str(min)
        elif min < temp:  # t가 min보다 큰 경우
            min = temp
            c.find('min').text = str(t)

        if max < min:  # max와 min이 바뀌는거 방지
            c.find('max').text = str(t)

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')
    return

def toohot(temp, s1):
    doc = ET.parse('clotheslist.xml')
    root = doc.getroot()

    string = 'clothes' + str(s1)
    t = temp - 0.3

    for c in root.findall(string):
        max = float(c.find('max').text)
        min = float(c.find('min').text)

        if max < temp:             # t 근처에 옷이 없는 경우, max가 t보다 작은데 추천되었고, 그에 대한 평가로 덥다고 할 때.
            max = max - 0.1
            c.find('max').text = str(max)
        elif max > temp:           # t보다 max가 큰 경우
            max = t
            c.find('max').text = str(t)

        if max < min:       # max와 min이 바뀌는거 방지
            c.find('min').text = str(t)

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')

def previousdata(cel):
    f = open('myrecommendation.txt', 'rt')
    fir = f.readline()  # 이전 추천 내역이 있는지 없는지 확인

    if fir == '0':
        print('추천받은 내역이 없습니다.')
        f.close()
        return 0
    else:
        return 1