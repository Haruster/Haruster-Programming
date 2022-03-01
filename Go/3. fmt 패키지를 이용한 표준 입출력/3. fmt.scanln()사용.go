package main

import "fmt"

func main() {

	var a int
	var b int

	c, d := fmt.Scanln(&a, &b)

	fmt.Println(c)
	fmt.Println(d)

}

// fmt.Scanln(&변수1, &변수2) // 변수 2개 동시 선언할 때 주로 사용