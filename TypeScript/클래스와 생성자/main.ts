class Human { // 클래스는 코드를 컨트롤 할 수 있도록 해주며 자바스크립트와 타입스크립트 둘 다 사용이 가능하다. (인터페이스와 유사하지만 사스에서 사용 가능)
    // 인터페이스 대신에 클래스를 사용할 수도 있다.
    // 자바스크립트에서는 클래스의 속성(Property)들을 묘사할 필요가 없지만 타입스크립트에서는 클래스가 어떤 속성을 가져야 하는지 선언해야 한다.
public name:string; // 변수 name을 public 변수로 선언한다.
public age: number; // 변수 age를 public 변수로 선언한다.
public addr: string; // 변수 addr을 public 변수로 선언한다.

constructor(name:string, age:number, addr:string) { // construction은 생성자이며 메서드(method)로 클래스가 시작할 때마다 호출된다. 
     // 생성자는 선언될 때 함수와 마찬가지로 인자를 가지고 있다. (해당 생성자는 3개의 인자를 가지고 있다.) (생성자는 메소드임.)

this.name = name; // 같은 속성의 이름을 인자로 준다. (즉, 해당 클래스의 name은 생성자의 name과 같다는 것이다.)
this.age = age; // 같은 속성의 이름을 인자로 준다. (즉, 해당 클래스의 age는 생성자의 age와 같다는 것이다.)
this.addr = addr; // 같은 속성의 이름을 인자로 준다. (즉, 해당 클래스의 addr은 생성자의 addr과 같다는 것이다.)


}
} // 클래스를 사용하는 것보다 인터페이스를 사용하는 것이 타입스크립트 측면에서 좀 더 안전하다.
// 하지만, react, node, express 등을 사용하게 된다면 클래스를 사용하는 것이 더 좋다.
// public 속성은 클래스 내부 뿐만 아니라 외부에서도 해당 변수를 사용할 수 있으며, private 속성은 해당 클래스 내부에서만 해당 변수를 사용할 수 있다.
// private 속성을 사용하면 몇 가지 속성을 보호할 수 있다.

const Haru = new Human("haruster", 21, "seoul"); // name, age, gender 즉, 3개의 인자가 꼭 필요하다.

const SayHello = (person: Human): string => {

return `name = ${person.name}, age = ${person.age}, addr = ${person.addr}`;

};

console.log(SayHello(Haru));

export {};