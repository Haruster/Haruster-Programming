#include <stdio.h>

int main(void) {

    char *books[3];
    char** ptr;

    books[0] = "C/C++";
    books[1] = "Java";
    books[2] = "C#";

    ptr = books;

    printf("books : %s, %s,%s\n", books[0], books[1], books[2]);
    printf("ptr : %s, %s, %s\n", *ptr, *(ptr + 1), *(ptr + 2));

    return 0;

}