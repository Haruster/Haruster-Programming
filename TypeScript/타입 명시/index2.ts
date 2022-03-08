// 함수 선언
const SayHello = (name:string, age:number, addr:string): string => { // name, age, addr이 매개변수인 함수 SayHello 선언(타입을 명시한 상태이다.)

    return `name = ${name}, age = ${age}, addr = ${addr}`;

};

SayHello("haru", 21, "seoul"); // 3개의 인자 중 하나라도 받지 않는다면 TypeScript에서는 실행되지 않는다.

export {}; // 해당 파일이 모듈이 된다는 것을 이해할 수 있게 함. (export를 하지 않으면 name변수를 선언할 수 없다고 뜬다.)

