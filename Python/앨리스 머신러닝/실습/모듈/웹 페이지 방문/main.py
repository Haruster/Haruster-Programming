from urllib.request import urlopen #from import 함수를 이용해서 urllib패키지 안 request 모듈에서 urlopen 함수를 import한다.

webpage = urlopen("https://en.wikipedia.org/wiki/Lorem_ipsum").read().decode("utf-8") #웹 페이지 주로를 urlopen하고 read()한 다음 utf-8로 디코드한다.

print(webpage) #변수 webpage를 출력한다