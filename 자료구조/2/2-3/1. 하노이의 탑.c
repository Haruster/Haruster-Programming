// n -1개로 원판을 A에서 B로 옮기고, n번째 원판을 A에서 C로 옮긴 다음, n - 1개의 원판을 B에서 C로 옮기면 된다.

#include <stdio.h>

void hanoi_tower(int n, char from, char tmp, char to) {

    if(n == 1) printf("원판 1을 %c에서 %c로 옮긴다.\n", from, to);

    else {

        hanoi_tower(n -1, from, to, tmp);
        printf("원판 %d을 %c에서 %c로 옮긴다.\n", n, from, to);
        hanoi_tower(n - 1, tmp, from, to);

    }
}

int main() {

    hanoi_tower(4, 'A', 'B', 'C');

    return 0;

}