package main

import "fmt"

func PrintNo(n int) {

	if n == 0 { // 재귀호출 탈출 조건

		return 

	}

	fmt.Println(n)
	PrintNo(n - 1) // 재귀호출
	fmt.Println("After", n) // 재귀호출 이후의 출력

}

func main() {

	PrintNo(3)

}