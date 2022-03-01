package main

import "fmt"

func main() {

	var x int = 10
	var y int = 30
	var z int = 100

	and := x & y
	or := y | z
	xor := x ^ z

	fmt.Println("and연산 결과 :", and)
	fmt.Println("or연산 결과 :", or)
	fmt.Println("xor연산 결과 :", xor)

}
