package main

import "fmt"

func main() {

	var setVar int

	fmt.Scanf("%d", &setVar)

	if setVar <= 100  {


		fmt.Println("setVar는 100보다 작거나 같습니다.")

		if setVar == 100 {

			fmt.Println("setVar는 100입니다.")

		} else if setVar < 100 {

			fmt.Println("setVar는 100보다 작습니다.")

		}

	}

	 if setVar >= 100 {

		fmt.Println("setVar는 100보다 크거나 같습니다.")

		if setVar == 100 {

			fmt.Println("setVar는 100입니다.")

		} else if setVar > 100 {

			fmt.Println("setVar는 100보다 큽니다.")

		}

	}


}