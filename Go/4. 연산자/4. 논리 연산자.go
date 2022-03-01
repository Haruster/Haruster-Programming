package main

import "fmt"

func main() {

	var a int = 10
	var b int = 20
	var c int = 30
	var d int = 40

	and := (a < b) && (b >= c)
	or := (b > c) || (c <= d)
	not := !((b > c) || (c <= d))

	fmt.Println("and =", and)
	fmt.Println("or =", or)
	fmt.Println("not =", not)

}