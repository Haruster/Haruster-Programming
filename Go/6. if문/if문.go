package main

import "fmt"

func main() {

	const SettingNum int = 10

	var UserNum int

	fmt.Scanf("%d", &UserNum)

	if UserNum == SettingNum {

		fmt.Println("UserNum과 SettingNum이 일치합니다.")

	} else {

		fmt.Println("UserNum과 SettingNum이 일치하지 않습니다.")

	}

}
