package main

import "fmt"

func plus(a int, b int) int { // 함수 선언

	return a + b

}

func main() {

	var x int
	var y int

	fmt.Println("정수 두개를 입력해주세요.")
	fmt.Scanf("%d", &x)
	fmt.Scanf("%d", &y)

	fmt.Println(plus(x, y)) // 함수 호출

}
