// if-else 사용

var score = prompt("점수를 입력해주세요 : ", 100);

score = parseInt(score); // 문자열 타입을 정수 타입으로 변경한다.

if (score >= 90) { // score가 90이상일 때

    grade = "A";

} else if (score >= 80) { // score가 80이상일 때

    grade = "A";

} else if (score >= 70) { // score가 70이상일 때

    grade = "C";

} else {

    grade = "ERROR";

}

document.write(score + "는 " + grade + "입니다. <br>");