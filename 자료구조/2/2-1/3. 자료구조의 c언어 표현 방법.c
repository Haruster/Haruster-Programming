// 자료구조의 c언어 표현방법

// 자료구조 스텍과 관련된 자료들을 정의

    typedef int element; // 자료구조의 요소
    typedef struct {

        int top;
        element stack[MAX_STACK_SIZE]; // 관련된 데이터를 구조체로 정의

    } StackType;

    // 자료구조 스택과 관련된 연산들을 정의

    void push(StackType *s, element item) { // 연산을 호출할 때 구조체를 함수의 파라미터로 전달 

        if( s -> top >= (MAX_STACK_SIZE - 1)) {

            stack_full();
            return;

        }

        s -> stack[++(s->top)] = item;

    }