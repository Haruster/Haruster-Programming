package main

import "fmt"

func main() {

	const PI = 3.14

	var data float64

	fmt.Scanf("%f", &data)

	var user float64 = data * PI

	fmt.Println("사용자가 입력한 원의 PI값은 : ", user)

}
