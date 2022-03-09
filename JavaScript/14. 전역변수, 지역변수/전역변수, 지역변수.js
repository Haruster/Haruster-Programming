let msg = "welcome"; // 전역 변수 (global variable)
console.log(msg); // 전역변수 msg를 출력함

function SayHello(name) {

    let msg = "Hello"; // 지역 변수 (local variable)

    console.log(msg + ' ' + name); // 지역변수 msg를 출력함

}

console.log(msg); // 전역변수 msg를 출력함