// 후위 표기식 계산

#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK_SIZE 100

// 프로그램 4.3에서 스택 코드 추가

typedef char element;   // 교체

// ...

// 프로그램 4.3에서 스택 코드 추가 끝

// 후위 표기 수식 계산 함수

int eval(char exp[]) {

    int op1, op2, value, i = 0;
    int len = strlen(exp);

    char ch;

    StackType s;

    init_stack(&s);

    for (i = 0; i < len; i++) {

        ch = exp[i];

        if(ch != '+' && ch != '-' && ch != '*' && ch != '/') {

            value = ch = '0';   // 입력이 피연산자이면

            push(&s, value);

        }

        else { // 연산자이면 피연산자를 스택에서 제거
        
            op2 = pop(&s);
            op1 = pop(&s);

            switch (ch) { // 연산을 수행하고 스택에 저장한다.
            
                case '+': push(&s, op1 + op2); break;

                case '-': push(&s, op1 + op2); break;

                case '*': push(&s, op1 + op2); break;

                case '/': push(&s, op1 + op2); break;

            
            }

        }

    }

    return pop(&s);

}

int main(void) {

    int result;

    printf("후위 표기식은 82/3-32*+\n");

    result = eval("32/3-32*+");

    printf("결과값은 %d\n", result);

    return 0;
}