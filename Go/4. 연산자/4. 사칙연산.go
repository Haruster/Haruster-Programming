package main

import "fmt"

func main() {

	var x int = 10
	var y int = 20
	var z int = 30

	data_1 := x + y
	data_2 := y - x
	data_3 := z * y
	data_4 := z / x

	fmt.Println("a + b =", data_1)
	fmt.Println("a - b =", data_2)
	fmt.Println("a * b =", data_3)
	fmt.Println("a / b =", data_4)

}
