// (구조체의 선언과 초기화를 따로 한다.)
#include <stdio.h>

struct people { //people이라는 이름을 가진 구조체를 정의한다.
    char name[20]; //1차원 배열(20개의 문자 저장가능)
    char address[30]; //1차원 배열 (30개의 문자 저장가능)
    int age;
};

struct people pe1 = {"Moon", "Seoul", 20}; //구조체 초기화(각 변수에 값을 지정)