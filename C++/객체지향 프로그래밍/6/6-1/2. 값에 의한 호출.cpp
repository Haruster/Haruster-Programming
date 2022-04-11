// 값에 의한 호출 (Call by value)

#include <iostream>

using namespace std;

void swap(int a, int b) {

    int tmp;

    tmp = a;

    a = b;

    b = tmp;

}

int main() {

    int m = 2;
    int n = 9;

    swap(m, n);

    cout << m << ' ' << n;

    return 0;

}