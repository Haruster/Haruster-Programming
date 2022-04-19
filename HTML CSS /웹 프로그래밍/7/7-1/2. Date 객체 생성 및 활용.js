// Date 객체 생성 및 활용

var now = new Date(); // 현재 시간 값을 가진 Date 객체 생성

document.write("현재 시간 : " + now.toUTCString() + "<br> <hr>");

document.write(now.getFullYear() + "년도 <br>");
docuement.write(now.getMonth() + 1 + "월 <br>");
docuement.write(now.getDate() + "일 <br>");
docuement.write(now.getHours() + "시 <br>");
docuement.write(now.getMinutes() + "분 <br>");
docuement.write(now.getSeconds() + "초 <br>");
docuement.write(now.getMilliseconds() + "밀리초 <br>");

var next = new Date(2017, 7, 15, 12, 12, 12); // 7은 8월

document.write("next.toLocaleString() : " + next.toLocaleString() + "<br>");