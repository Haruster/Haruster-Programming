// []로 배열 만들기

var plots = [20, 5, 8, 15, 20]; // 원소 5개의 배열 생성

document.write("var plots = [20, 5, 8, 15, 20] <br>");

for (i = 0; i < 5; i++) {

    var size = plots[i]; // plots 배열의 i번째 원소

    while (size > 0) {

        document.write("*");

        size--;

    }

    document.write(plots[i] + "<br>");

}