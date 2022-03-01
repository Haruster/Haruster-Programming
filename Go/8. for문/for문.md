# for문 (반복문)

## for문 문법

for 초기문; 조건문; 후처리 {

    실행문

}

ex)

for i := 0: i < 10; i++ { 
    
    // i는 0이고 i가 10미만일 때까지 1씩 증가(조건문이 true인 경우 실행된다. -> 조건문이 거짓이 되면 실행이 되지 않음)

    print("현재 i의 값은 ", i, "입니다.")

}


## 반복문 무한 루프

- 반복문을 항상 true값이 되게 하여 계속 실행문을 계속 반복하여 실행하는 것을 무한루프라고 한다.

ex)

for true {

    fmt.Println("I'm Programmer")

}

## 중첩 for문 

- for문 안에 for문을 반복해서 사용하는 것이다.

ex)

for i := 0; i < 3; i++ {

    for j := 0; j < 5; j++ {

        fmt.Print("*")

    }

    fmt.Println("")

}