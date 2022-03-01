package main

import "fmt"

func main() {

	const con1 int = 30

	var var1 int 

	fmt.Scanf("%d", &var1)

	if (var1 == 30) && (var1 <= 30) && (var1 >= 30) { // 3개의 조건이 다  true여야 한다.

		fmt.Println("var1은 30입니다.")

	} else if (var1 == 1) || (var1 == 0) { // 조건 중 하나하도 맞으면 true

		fmt.Println("var1은 0아니면 1입니다.")

	}

}