// 지역 변수와 전역 변수

var x = 100;

function f() { // 함수 f 선언

    var x;

    x = 10; // 지역변수 x에 10대입

    document.write("지역 변수 x = ", x);
    document.write("<br>");

    this.x = 1000; // 전역 변수 x에 1000대입

    document.write("전역 변수 x = ", this.x);

}

f(); // 함수 f()호출