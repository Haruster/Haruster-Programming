package main

import "fmt"

func main() {

	const var1 int = 90

	switch var1 {

	case 100:

		fmt.Println("var1의 값은 100입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 90:

		fmt.Println("var1의 값은 90입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 80:


		fmt.Println("var1의 값은 80입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 70:

		fmt.Println("var1의 값은 70입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 60:

		fmt.Println("var1의 값은 60입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 50: 

		fmt.Println("var1의 값은 50입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 40:

		fmt.Println("var1의 값은 40입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 30:

		fmt.Println("var1의 값은 30입나다.")
		break // go에서는 break를 생략할 수도 있다.

	case 20:

		fmt.Println("var1의 값은 20입니다.")
		break // go에서는 break를 생략할 수도 있다.

	case 10:

		fmt.Println("var1의 값은 10입니다.")


	default:
		
		fmt.Println("var1의 값이 case 범위를 벗어났습니다.")
		break // go에서는 break를 생략할 수도 있다.

	}

}