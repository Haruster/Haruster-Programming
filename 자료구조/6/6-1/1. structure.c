#include <stdio.h>

typedef struct Users {

    char name[20];
    int age;
    char addr[10];
    int year;
    int month;
    int day;

} users;

int main(void) {

    users a = {"Haruster", 21, "Suwon", 2002, 12, 4};
    users b = {"Rayser", 20, "Jeonju", 2003, 8, 20};

    printf("user = %s, 나이는 %d, 거주지는 %s, %d %d %d\n", a.name, a.age, a.addr, a.year, a.month, a.day);
    printf("user = %s, 나이는 %d, 거주지는 %s, %d %d %d\n", b.name, b.age, b.addr, b.year, b.month, b.day);


    return 0;

}