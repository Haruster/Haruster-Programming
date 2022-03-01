// 중첩 for문이란 for문안에 for문을 넣는 것을 말한다.

package main

import "fmt"

func main() {

	for i := 0; i < 3; i++ {

		for j := 0; j < 5; j++ {

			fmt.Print("*")

		}

		fmt.Println("")

	}

}