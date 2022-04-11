// 참조 매개 변수로 평균 리턴하기

#include <iostream>

using namespace std;

bool average(int a[], int size, int& avg) { // 참조 매개 변수 avg에 평균 값 전달

    if (size <= 0) {

        return false;

    }

    int sum = 0;

    for (int i = 0; i < size; i++) {

        sum += a[i];

    }

    avg = sum / size;

    return true;

}

int main() {

    int x[] = {0, 1, 2, 3, 4, 5};
    int avg;

    if(average(x, 6, avg)) cout << "평균은 " << avg << endl; // avg에 평균이 넘어오고 average()는 true 리턴

    else cout << "매개 변수 오류" << endl;

    if(average(x, -2, avg)) cout << "평균은 " << avg << endl; // avg의 값은 의미 없고, average()는 false 리턴

    else cout << "매개 변수 오류" << endl;

    return 0;

}