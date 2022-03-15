// fork 명령어 프로그램 예

#include <unistd.h>

main() {

    pid_t pid;

        printf("Before fork ... \n");

    /* fork 명령어 실행 */

    pid = fork();

        if(pid == 0) /* 자식 프로세스 */

            printf("I'm the child... PID is %d \n", pid);

        else if(pid > 0) { /* 부모 프로세스 */

            wait(NULL);
            printf("I'm the parent... PID is %d\n", pid);

        }

        else 

            printf("fork error");

}