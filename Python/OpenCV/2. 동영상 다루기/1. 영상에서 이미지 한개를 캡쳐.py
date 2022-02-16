import cv2

cap = cv2.VideoCapture(0) #비디오를 사용하기 위해서 VideoCapture함수를 선언한다. (0을 입력하면 카메라를 사용하여 영상을 출력하고 비디오 영상의 디렉터리를 입력하면 해당 동영상을 실행한다.)

ret, img_color = cap.read() # cap.read 함수를 이용하여 카메라로부터 이미지 한개를 받아온다.

cv2.imshow("img", img_color) #캡쳐된 이미지를 화면에 보여준다.
cv2.waitKey(0) #아무키를 누를 때까지 무한히 대기한다(0은 무한 최대 1000까지 숫자 지정가능)

#비디오 캡쳐 객체와 윈도우를 위한 자원을 해재한다.
cap.release()
cv2.destroyAllWindows()

