// 반복문 continue

var sum = 0;

for (i = 1; i <= 10; i++) {

    if (i % 3 != 1) { // 3으로 나눈 나머지가 1이 아닌 경우 

        continue; // 다음 반복으로 점프

    }

    document.write(i + " ");

    sum += i;

}

document.write("합은 " + sum);