var a = new String("Boys and Girls");
var b = "!!";

document.write("a : " + a + "<br>");
document.write("b : " + b + "<br> <hr>");

document.write(a.charAt(0) + "<br>");
document.write(a.concat(b, "입니다.") + "<br>");
document.write(a.indexOf("s") + "<br>");
document.write(a.indexOf("And") + "<br>");
document.write(a.slice(5, 8) + "<br>");
document.write(a.substr(5, 3) + "<br>");
document.write(a.toUpperCase() + "<br>");
document.write("    Kitae   ".trim() + "<br><hr>");

var sub = a.split(" ");

document.write("a를 빈칸으로 분리 <br> ");

for (var i = 0; i < sub.length; i++) {

    document.write("sub" + i + "=" + sub[i] + "<br>");

}

document.write(" <hr> String메소드를 실행 후 a와 b 변함 없음 <br>");
document.write(" a : " + a + "<br>");
document.write(" b : " + b + "<br>");