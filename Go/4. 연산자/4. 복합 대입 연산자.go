package main

import "fmt"

func main() {

	var x int = 80
	var y int = 10
	var z int = 1
	var i int = 50
	var j int = 70
	var k int = 90
	var l int = 100
	var h int = 120
	var t int = 909
	var e int = 120

	x += y
	y -= z
	z *= i
	i /= j
	j %= i
	k &= z
	l |= j
	h ^= z
	t <<= 2
	e >>= 2

	fmt.Println("x + y = ", x)
	fmt.Println("y - z =", y)
	fmt.Println("z * i =", z)
	


	
}