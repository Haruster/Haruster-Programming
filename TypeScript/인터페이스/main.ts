interface Human { // 인터페이스는 자바스크립트에서는 작동하지 않고 타입스크립트에서만 작동한다.

    name:string; 
    age: number;
    addr: string;

}

const person = {

    name: "haruster",
    age : 22,
    addr: "seoul"

};

const SayHello = (person: Human): string => {

    return `name = ${person.name}, age = ${person.age}, addr = ${person.addr}`;

};

console.log(SayHello(person));

export {};