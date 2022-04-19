// sum() 함수 중복

#include <iostream>

using namespace std;

int sum(int a, int b) { // a에서 b까지 합하기

    int s = 0;

    for(int i = a; i <= b; i++) {

        s += i;

    }

    return s;

}

int sum(int a) { // 0에서 a까지 합하기

    int s = 0;

    for(int i = 0; i <= a; i++) {

        s += i;

    }

    return s;

}

int main() {

    cout << sum(3, 5) << endl;
    cout << sum(3) << endl;
    cout << sum(100) << endl;

}

int main() {



}