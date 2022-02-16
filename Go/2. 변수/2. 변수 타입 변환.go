// 변수 타입을 float64에서 int로 변경

package main

import "fmt"

func main() {

	var a int = 10;

	var b float64 = 3.14

	var c = int(b) // 변수 b를 int형으로 타입 변환한 값을 변수 c에 대입한다..

	var d = a + c

	fmt.Println("a + b =", d)

}