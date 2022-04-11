// 전역 함수

function evalParseIntIsNaN() {

    var res = eval("2 * 3 + 4 * 6"); // res는 32

    document.write("eval(\"2 * 3 + 4 * 6\")는 32 <br> ");

    var m = parseInt("32");

    document.write("parseInt(\"32\)는 " + m + "<br>");

    var n = parseInt("0x32");

    document.write("parseInt(\"0x32\")는 " + n + "<br> <br>");

    // "hello"는 정수로 변환할 수 없으므로 parseInt("hello")는 NaN 리턴

    n = parseInt("hello");

    if (isNaN(n)) // true

        document.write("hello는 숫자가 아닙니다.");

}

evalParseIntIsNaN();