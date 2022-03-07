const name = "Haruster",
    age = 21,
    addr = "seoul";

// 함수 선언

const SayHello = (name, age, addr) => { // name, age, addr이 매개변수인 함수 SayHello 선언

    console.log(`name = ${name}, age = ${age}, addr = ${addr}`);

};

SayHello(name, age, addr); // 3개의 인자 중 하나라도 받지 않는다면 TypeScript에서는 실행되지 않는다.

export {}; // 해당 파일이 모듈이 된다는 것을 이해할 수 있게 함. (export를 하지 않으면 name변수를 선언할 수 없다고 뜬다.)

/*

const name = "Haruster",
    age = 21,
    addr = "seoul";

// 함수 선언

const SayHello = (name, age, addr?) => { // name, age, addr이 매개변수인 함수 SayHello 선언

    console.log(`name = ${name}, age = ${age}, addr = ${addr}`);

};

SayHello(name, age, addr); // 위의 코드와는 다르게 ?가 붙으면 그 인자는 선택적 인자이기 때문에 오류가 발생하지 않는다.

export {}; // 해당 파일이 모듈이 된다는 것을 이해할 수 있게 함. (export를 하지 않으면 name변수를 선언할 수 없다고 뜬다.)

*/