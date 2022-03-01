package main 

import "fmt"

func main() {

	const SettingVar int = 20

	var UserVar int

	if SettingVar == UserVar {

		fmt.Println("SettingVar과 UserVal이 일치합니다.")

	} else if SettingVar < UserVar {

		fmt.Println("SettingVar보다 UserVal이 더 큽니다.")

	} else if SettingVar > UserVar {
		
		fmt.Println("SettingVar이 UserVal보다 큽니다.")

		} else {

		fmt.Println("값이 올바르지 않습니다.")

	}

}