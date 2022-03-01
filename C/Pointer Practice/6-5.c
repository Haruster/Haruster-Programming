#include <stdio.h>

int main(void) {

    char id[20], *pEntry[][2] = {
        {"swlee", "1111"},
        {"ikkim", "qwer1234"},
        {"jckim", "881100"}
    };

    int i, found = 0;

    printf("Enter your ID : ");
    gets(id);

    for(i = 0; *pEntry[i][0]; i++) {

        if(!strcmp(pEntry[i][0], id)) {

            printf("Your password is %s\n", pEntry[i][1]);
            found = 1;
            break;

        }

    }

    if(!found)

        printf("Your id %s is not registered..... \n", id);

    return 0;

}