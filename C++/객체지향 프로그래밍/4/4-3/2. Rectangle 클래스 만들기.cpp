#include <iostream>

using namespace std;

class Rectangle {

    public:

        int width, height;

        Rectangle();
        Rectangle(int w, int h);
        Rectangle(int length);

        bool isSquare();

};

Rectangle :: Rectangle() {

    width = height = 1;

}

Rectangle :: Rectangle(int w, int h) {

    width = w; height = h;

}

Rectangle :: Rectangle(int length) {

    width = height = length;

}

// 정사각형이면 true를 리턴하는 멤버 함수

bool Rectangle :: isSquare() {

    if (width == height) return true;

    else return false;

}

int main() {

    // 3개의 생성자가 호출됨.

    Rectangle rect1;
    Rectangle rect2(3, 5);
    Rectangle rect3(3);

    if (rect1.isSquare()) {

        cout << "rect1은 정사각형이다." << endl;

    }

    if (rect2.isSquare()) {

        cout << "rect2는 정사각형이다." << endl;

    }

    if (rect3.isSquare()) {

        cout << "rect3는 정사각형이다." << endl;

    }

    return 0;

}