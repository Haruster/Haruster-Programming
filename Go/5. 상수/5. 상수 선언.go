package main

import "fmt"

func main() {

	const a int = 30
	const c string = "hello world"

	var b int = 40
	var d int = 30

	fmt.Println("상수 a의 값은 :", a)
	fmt.Println("상수 c에 들어가 있는 문자열은? :", c)
	
	fmt.Println("변수 b에 들어가 있는 값은? :", b)
	fmt.Println("변수 d에 들어가 있는 값은? :", d)

}

// 상수는 const를 통해서 선언할 수 있다.
