package main

import "fmt"

var a int = 21 // int형 전역변수 a를 선언한다.(초기값 21)
var b int = 20 // int형 전역변수 b를 선언한다. (초기값 20)

func main() {

	var name string = "haruster"
	var team_name string = "Phantester"

	fmt.Println("이름은 ", name, "입니다.")
	fmt.Println("2021년도의 나이는 ", b, "입니다.")
	fmt.Println("2022년도의 나이는 ", a, "입니다.")
	fmt.Println("팀이름은 ", team_name, "입니다.")

}