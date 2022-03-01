package main

import "fmt"

func main() {

	var i int = 90

	switch i {

		case 100:

			fmt.Println("i의 값은 100입니다.")
			break

		case 90:

			fmt.Println("i의 값은 90입니다.")
			break

		case 80:

			fmt.Println("i의 값은 80입니다.")
			break

		case 70:

			fmt.Println("i의 값은 70입니다.")
			break

		case 60:

			fmt.Println("i의 값은 60입니다.")
			break

		case 50:
			fmt.Println("i읙 값은 50입니다.")
			break

		case 40:
			fmt.Println("i의 값은 40입니다.")
			break

		case 30:
			fmt.Println("i의 값은 30입니다.")
			break

		case 20:
			fmt.Println("i의 값은 20입니다.")
			break

		case 10: 
			fmt.Println("i의 값은 10입니다.")
			break

		case 0:
			fmt.Println("i의 값은 0입니다.")
			fallthrough // continue문과 같다. (break를 잡지 않고 다음 문ㅇ느로 넘어감)

		default:
			fmt.Println("i값을 재설정해주세요")
			break

	}

}