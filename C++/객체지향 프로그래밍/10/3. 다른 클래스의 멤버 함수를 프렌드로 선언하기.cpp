// 다른 클래스의 멤버 함수를 프렌드로 선언하기

#include <iostream>

using namespace std;

class Rect; // Rect 클래스가 선언되기 전에 먼저 참조되는 컴파일 오류를 막기 위한 선언문이다.

class RectManager { // RectManager 클래스 선언

public:

    bool equals(Rect r, Rect s);

};

class Rect {    // Rect 클래스 선언

    int width, height;

public:

    Rect(int width, int height) { this->width = width; this->height = height; }

    friend bool RectManager::equals(Rect r, Rect s);

};

bool RectManager::equals(Rect r, Rect s) {

    if (r.width == s.width && r.height == s.height) return true; // RectManager 클래스의 equals() 멤버를 프렌드로 선언

    else return false;

}

int main() {

    Rect a(3, 4), b(3, 4);

    RectManager man;

    if (man.equals(a, b)) cout << "equal" << endl;

    else cout << "not equal" << endl;

}