import cv2 

cap = cv2.VideoCapture('video.mp4') #비디오를 사용하기 위해서 VideoCapture함수를 선언한다. (0을 입력하면 카메라를 사용하여 영상을 출력하고 비디오 영상의 디렉터리를 입력하면 해당 동영상을 실행한다.)

while(True): #영상 캡쳐와 화면에 보여주는 것을 반복하도록 무한 루프를 추가한다. 
    ret, img_color = cap.read() #cap.read()함수를 이용하여 카메라로부터 이미지 한개를 받아온다. 

    cv2.imshow("img", img_color) #캡쳐된 이미지를 화면에 보여준다.

    if cv2.waitKey(1)&0xFF == 27: #esc(0xFF)를 누르면 무한루프가 빠져나오게 하고 waitKey를 1로 지정해서 1초마다 다음 문으로 넘어가게 한다. 
        break

#비디오 캡쳐 객체와 윈도우를 위한 자원을 해제한다. 
cap.release()
cv2.destroyAllWindows()
