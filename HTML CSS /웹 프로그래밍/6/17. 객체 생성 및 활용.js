// 객체 생성 및 활용

// Date 객체 생성

var today = new Date();

// Date 객체의 toGMTString() 메소드 호출

document.write("현재 시간 : " + today.toGMTString() + "<br>");

// String 객체 생성

var mystr = new String("자바스크립트 공부하기");

document.write("mystr의 내용 : " + mystr + "<br>");
document.write("mystr의 길이 : " + mystr.length + "<br>");

// mystr.length = 10; // 이 문장은 오류이다.