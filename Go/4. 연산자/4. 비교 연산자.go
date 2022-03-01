package main

import "fmt"

func main() {

	var var1 int = 10
	var var2 int = 20
	var var3 int = 30
	var var4 int = 40

	fmt.Println("var1 == var2 =", var1 == var2)
	fmt.Println("var2 != var3 =", var2 != var3)
	fmt.Println("var4 < var2 =", var4 < var2)
	fmt.Println("var3 > var1 =", var3 > var1)
	fmt.Println("var1 <= var2 =", var1 <= var2)
	fmt.Println("var4 >= var3 =", var4 >= var3)

}