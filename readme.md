체감온도에 알맞은 옷 추천 서비스   
============
## 1. 동기 및 목적   
### 1-1. 동기   
+ 날씨 감각이 부족해 평소 환절기 같은 날씨에 옷을 입는데 어려움을 겪었다.
+ 이전의 날씨와 오늘의 날씨를 비교하는데 귀찮음이 동반된다.
### 1-2. 목적   
+ 위치를 입력하면 그 위치의 현재 체감온도와 그에 알맞은 옷을 추천한다.
+ 이 때 추천받는 옷들은 사용자의 평가에 기반한다.

## 2. 작동 방식
### 2-1. 추천 기능   
 + 각 옷들 마다 기온에 따른 구간을 처음에 설정하고 이를 파일로 만든다. 이 파일이 clotheslist.xml파일이다.   
 + xml 파일을 보면 아래와 같이 구성되어 있다. clothes + '고유 번호' 아래에 이름, 최저기온과 최대기온이 있다.
```
-<clothes0>
  <name>minsomae</name>
  <n>0</n>
  <min>28</min>
  <max>50</max>
</clothes0>
```
 + 웹 크롤링을 이용해서 네이버에서 검색한 지역의 체감기온을 가져온다.
```python
def gettemperature(city):

    location = urllib.parse.quote(city + '+날씨')
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + location

    html = urlopen(url)
    html_source = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    cel = html_source.find('span', class_='sensible').find('span', class_='num').text

    return cel
``` 
 + 사용자의 평가가 없을 때는 exe 파일을 처음 실행할 때 만들어진 이 xml파일을 가지고 옷을 추천해준다.
 + 현재 체감 온도가 최저기온과 최대기온 사이에 있는 옷을 찾아서 추천해주는 것이다.
 + 만약 사용자가 평가를 했다면 수정된 xml 파일을 가지고 똑같은 방식으로 옷을 추천해준다.   
 + 만약 체감 온도가 어느 옷의 최저기온과 최대기온 사이에도 존재하지 않는다면 체감 온도에 특정값을 더하거나 빼서 구간 안에 위치하도록 하는 옷이 있을 때 까지 
 찾는 것을 반복한다.
 ```python
 # selectyourclothes 함수의 일부분
 
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

 ```
 
### 2-2. 평가 기능
+ 사용자가 덥거나 춥다고 평가를 하면 xml 파일의 max나 min이 수정된다.
  + 사용자가 덥다고 평가 했을 경우, 현재 체감온도 보다 조금 낮은 온도로 max를 바꿔서 범위를 조정한다. 더 낮은 온도 구간에 추천된다.
  + 사용자가 춥다고 평가 했을 경우에는 현재 체감온도 보다 조금 높은 온도로 min을 바꿔서 범위를 조정한다. 더 높은 온도 구간에 추천된다.
  ```python
  # toocold 함수의 일부분
  
  if min > temp:  
            min = min + 0.3
            c.find('min').text = str(t)
        elif min < temp:  
            min = temp
            c.find('min').text = str(t)

        if max < min:  
            c.find('max').text = str(t)
  ```


## 3. 각 파일 설명
+ PyQt5 Designer를 이용해서 UI 틀을 짰고, 각 화면에서 필요한 함수를 연결 하는 방식으로 코드를 구성했다.   
+ 참고로 properattire은 exe 파일로 만들기 전 전체적인 틀을 짜보는 용으로 만든 코드이다.

### 3-1. main.py
  + 처음 exe 파일을 실행했을 때 보여지는 화면의 UI
  + 추천 및 평가 버튼을 눌렀을 때 그에 맞는 화면 전환
  + myrecommendation.txt 파일이나 clotheslist.xml 파일이 없을 때 파일 생성
  
### 3-2. makebasisfile.py
  + 옷을 추천해주는 기준이 되는 clotheslist.xml 파일 생성
  + 직전의 추천 내역을 평가할 수 있도록 직전의 추천 내역을 기록할 myrecommendation.txt 파일 생성
  
### 3-3. recommendation.py 와 recommendclothes.py
  + recommendation.py는 추천 화면의 UI와 recommendclothes.py의 함수를 연결
  + recommnedclothes.py에는 추천 기능에 필요한 함수들이 모여있음
    + 네이버에서 현재 지역의 체감 온도를 가져옴
    + 적절한 옷을 고름
    + 추천 내역을 리스트에 저장
    + 추천 내역을 myrecommendation.txt 파일에 기록
    
### 3-4. evaluation.py 와 evaluateclothes.py
  + evaluation.py는 평가 화면의 UI와 evaluateclothes.py의 함수를 연결
  + evaluateclothes.py에는 평가기능에 필요한 함수들이 모여있음
    + 평가할 때 선택된 옷의 번호 추출
    + 옷의 번호를 이용해 평가에 따른 xml 파일 수정

## 4. 사용법
### 4-1. RECOMMENDATION
1. 추천을 누르고 자신이 있는 위치를 한글로 검색한다.
2. 옷을 추천받는다.

### 4-2. EVALUATION
1. 추천 기능을 한 번은 사용해야 평가 기능도 사용가능하다. 그렇지 않으면 NO DATA! 라고 경고가 뜬다.
2. 평가 기능을 제대로 눌렀다면 바로 직전에 추천 받은 위치, 시각, 그 때의 체감 온도 그리고 옷이 화면에 뜬다.
3. 평가 받은 옷들 중 맘에 안 들었던 옷을 선택해서 더웠는지 추웠는지 체크해서 OK 버튼을 누른다.

## 5. 한계
1. 네이버 웹 크롤링으로 하다보니 같은 지역이라도 네이버에 검색했을 때 나오지 않는 지역은 찾을 수 없다.   
  예를 들어 잠원동이라고 검색하면 나오지만 잠원이라고 검색하면 나오지 않는다. 하지만 압구정동이라고 검색하면 나오고 압구정이라고 검색해도 나온다.
2. 옷의 적정 기온 조절 폭이 너무 크거나 작을 수 있다.
3. 사용자가 실수로 xml 파일을 지웠을 경우 다시 초기 설정으로 돌아간다.
