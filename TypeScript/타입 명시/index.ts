// 함수 선언
//(void는 빈공간을 의미한다. 또한 void는 함수의 인자들이 어떤 타입의 값을 돌려주는지를 나타내기 위해서 사용한다.) 최종적으로 void형을 반환함
const SayHello = (name:string, age:number, addr:string):void => { // name, age, addr이 매개변수인 함수 SayHello 선언(타입을 명시한 상태이다.)

    console.log(`name = ${name}, age = ${age}, addr = ${addr}`);

};

SayHello("haru", 21, "seoul"); // 3개의 인자 중 하나라도 받지 않는다면 TypeScript에서는 실행되지 않는다.

export {}; // 해당 파일이 모듈이 된다는 것을 이해할 수 있게 함. (export를 하지 않으면 name변수를 선언할 수 없다고 뜬다.)

