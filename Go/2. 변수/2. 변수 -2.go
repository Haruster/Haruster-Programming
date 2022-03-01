package main

import "fmt"

func main() {

	var a int = 2013; // int형 변수 a를 선언하고 초깃값으로 2013을 넣는다.
	var b int // int형 변수 b를 선언한다.

	b = 21 // 변수 b에 21을 저장한다.

	var c = "haru" // 변수 c를 선언하고 "haru"라는 값을 저장한다.

	d := "Phantester" // 변수 d를 선언하고 "Phantester라는 값을 저장한다."

	fmt.Println("since", a)
	fmt.Println("name", c)
	fmt.Println("age", b)
	fmt.Println("team", d)

}