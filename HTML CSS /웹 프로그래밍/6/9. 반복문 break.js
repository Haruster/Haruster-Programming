// 반복문 continue, break문

var i = 0;
var sum = 0;

while (true) { // 무한 반복

    sum += i;

    if (sum > 3000) {

        break; // 합이 3000보다 크면 반복문을 벗어난다.

    }

    i++;

}

document.write(i + "까지 더하면 3000을 넘음 : " + sum);