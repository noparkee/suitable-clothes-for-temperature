# 처음 한 번만 실행
from xml.etree.ElementTree import Element, SubElement, ElementTree

def makebasisxml():
    root = Element('clotheslists')

    minsomae = SubElement(root, 'clothes0')
    SubElement(minsomae, 'name').text = 'minsomae'
    SubElement(minsomae, 'n').text = '0'
    SubElement(minsomae, 'min').text = '28'
    SubElement(minsomae, 'max').text = '50'

    banpal = SubElement(root, 'clothes1')
    SubElement(banpal, 'name').text = 'banpal'
    SubElement(banpal, 'n').text = '1'
    SubElement(banpal, 'min').text = '23'
    SubElement(banpal, 'max').text = '50'

    banbaji = SubElement(root, 'clothes2')
    SubElement(banbaji, 'name').text = 'banbaji'
    SubElement(banbaji, 'n').text = '2'
    SubElement(banbaji, 'min').text = '23'
    SubElement(banbaji, 'max').text = '50'

    onepiece = SubElement(root, 'clothes3')
    SubElement(onepiece, 'name').text = 'onepiece'
    SubElement(onepiece, 'n').text = '3'
    SubElement(onepiece, 'min').text = '28'
    SubElement(onepiece, 'max').text = '50'

    yalbshirt = SubElement(root, 'clothes4')
    SubElement(yalbshirt, 'name').text = 'yalbshirt'
    SubElement(yalbshirt, 'n').text = '4'
    SubElement(yalbshirt, 'min').text = '23'
    SubElement(yalbshirt, 'max').text = '27'

    myeonbaji = SubElement(root, 'clothes5')
    SubElement(myeonbaji, 'name').text = 'myeonbaji'
    SubElement(myeonbaji, 'n').text = '5'
    SubElement(myeonbaji, 'min').text = '20'
    SubElement(myeonbaji, 'max').text = '27'

    yalbcardigan = SubElement(root, 'clothes6')
    SubElement(yalbcardigan, 'name').text = 'yalbcardigan'
    SubElement(yalbcardigan, 'n').text = '6'
    SubElement(yalbcardigan, 'min').text = '20'
    SubElement(yalbcardigan, 'max').text = '22'

    ginpal = SubElement(root, 'clothes7')
    SubElement(ginpal, 'name').text = 'ginpal'
    SubElement(ginpal, 'n').text = '7'
    SubElement(ginpal, 'min').text = '20'
    SubElement(ginpal, 'max').text = '22'

    jean = SubElement(root, 'clothes8')
    SubElement(jean, 'name').text = 'jean'
    SubElement(jean, 'n').text = '8'
    SubElement(jean, 'min').text = '9'
    SubElement(jean, 'max').text = '22'

    yalbknit = SubElement(root, 'clothes9')
    SubElement(yalbknit, 'name').text = 'yalbknit'
    SubElement(yalbknit, 'n').text = '9'
    SubElement(yalbknit, 'min').text = '17'
    SubElement(yalbknit, 'max').text = '19'

    mtm = SubElement(root, 'clothes10')
    SubElement(mtm, 'name').text = 'mtm'
    SubElement(mtm, 'n').text = '10'
    SubElement(mtm, 'min').text = '17'
    SubElement(mtm, 'max').text = '19'

    cardigan = SubElement(root, 'clothes11')
    SubElement(cardigan, 'name').text = 'cardigan'
    SubElement(cardigan, 'n').text = '11'
    SubElement(cardigan, 'min').text = '12'
    SubElement(cardigan, 'max').text = '19'

    jacket = SubElement(root, 'clothes12')
    SubElement(jacket, 'name').text = 'jacket'
    SubElement(jacket, 'n').text = '12'
    SubElement(jacket, 'min').text = '9'
    SubElement(jacket, 'max').text = '16'

    yasang = SubElement(root, 'clothes13')
    SubElement(yasang, 'name').text = 'yasang'
    SubElement(yasang, 'n').text = '13'
    SubElement(yasang, 'min').text = '9'
    SubElement(yasang, 'max').text = '16'

    stocking = SubElement(root, 'clothes14')
    SubElement(stocking, 'name').text = 'stocking'
    SubElement(stocking, 'n').text = '14'
    SubElement(stocking, 'min').text = '9'
    SubElement(stocking, 'max').text = '16'

    trenchcoat = SubElement(root, 'clothes15')
    SubElement(trenchcoat, 'name').text = 'trenchcoat'
    SubElement(trenchcoat, 'n').text = '15'
    SubElement(trenchcoat, 'min').text = '9'
    SubElement(trenchcoat, 'max').text = '11'

    knit = SubElement(root, 'clothes16')
    SubElement(knit, 'name').text = 'knit'
    SubElement(knit, 'n').text = '16'
    SubElement(knit, 'min').text = '9'
    SubElement(knit, 'max').text = '11'

    coat = SubElement(root, 'clothes17')
    SubElement(coat, 'name').text = 'coat'
    SubElement(coat, 'n').text = '17'
    SubElement(coat, 'min').text = '5'
    SubElement(coat, 'max').text = '8'

    gajuckjacket = SubElement(root, 'clothes18')
    SubElement(gajuckjacket, 'name').text = 'gajuckjacket'
    SubElement(gajuckjacket, 'n').text = '18'
    SubElement(gajuckjacket, 'min').text = '5'
    SubElement(gajuckjacket, 'max').text = '8'

    leggings = SubElement(root, 'clothes19')
    SubElement(leggings, 'name').text = 'leggings'
    SubElement(leggings, 'n').text = '19'
    SubElement(leggings, 'min').text = '5'
    SubElement(leggings, 'max').text = '8'

    padding = SubElement(root, 'clothes20')
    SubElement(padding, 'name').text = 'padding'
    SubElement(padding, 'n').text = '20'
    SubElement(padding, 'min').text = '-50'
    SubElement(padding, 'max').text = '4'

    dukkcoat = SubElement(root, 'clothes21')
    SubElement(dukkcoat, 'name').text = 'dukkcoat'
    SubElement(dukkcoat, 'n').text = '21'
    SubElement(dukkcoat, 'min').text = '-50'
    SubElement(dukkcoat, 'max').text = '4'

    mockdori = SubElement(root, 'clothes22')
    SubElement(mockdori, 'name').text = 'mockdori'
    SubElement(mockdori, 'n').text = '22'
    SubElement(mockdori, 'min').text = '-50'
    SubElement(mockdori, 'max').text = '4'

    gimo = SubElement(root, 'clothes23')
    SubElement(gimo, 'name').text = 'gimo'
    SubElement(gimo, 'n').text = '23'
    SubElement(gimo, 'min').text = '-50'
    SubElement(gimo, 'max').text = '4'

    tree = ElementTree(root)
    tree.write('./' + 'clotheslist' + '.xml')

def makebasistxt():
    fp = open('myrecommendation.txt', 'wt')             # 바로 직전 추천 내역 기록용
    fp.write(str(0))
    fp.close()
