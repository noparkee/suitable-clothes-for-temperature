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
    t = temp + 0.5
    for c in root.findall(string):
        c.find('min').text = str(t)
        if float(c.find('min').text) > float(c.find('max').text):
            c.find('max').text = str(t)

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')
    return

def toohot(temp, s1):
    doc = ET.parse('clotheslist.xml')
    root = doc.getroot()

    string = 'clothes' + str(s1)
    t = temp - 0.5
    for c in root.findall(string):
        c.find('max').text = str(t)
        if float(c.find('max').text) < float(c.find('min').text):
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