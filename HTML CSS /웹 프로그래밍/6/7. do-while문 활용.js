// do while문 활용

var n = prompt("0보다 큰 정수를 입력하세요", 0);

n = parseInt(n);

var i = 0;
var sum = 0;

do {

    sum += i;
    i++;

} while (i <= n);

document.write("0에서 " + n + "까지의 합은 " + sum);