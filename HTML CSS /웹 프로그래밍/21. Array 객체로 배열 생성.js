// Array 객체로 배열 생성

var degrees = new Array(); // 빈 배열 생성

degrees[0] = 15.1;
degrees[1] = 15.4;
degrees[2] = 16.1;
degrees[3] = 17.5;
degrees[4] = 19.2;
degrees[5] = 21.4;

var sum = 0;

for (i = 0; i < degrees.length; i++) {

    sum += degrees[i];

}

document.write("평균 온도는 " + sum / degrees.length + "<br>");