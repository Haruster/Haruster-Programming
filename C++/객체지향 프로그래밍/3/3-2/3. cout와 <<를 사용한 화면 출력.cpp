#include <iostream>

double area(int r);

double area(int r) {

    return 3.14 * r * r;

}

int main() {

    int n = 3;
    
    char c = '#';

    std::cout << c << 5.5 << '_' << n << "hello" << true; // #5.5-3hello1 이 출력된다. (true는 정수로 1이기 때문)
    std::cout << "n + 5 =" << n + 5;
    std::cout << "면적은" << area(n); // 함수 area()의 리턴 값 출력

    return 0;


}