// 오버라이딩된 함수를 호출하는 동적 바인딩

#include <iostream>

using namespace std;

class Shape {

public:

    void paint() {

        draw();

    }

    virtual void draw() {

        cout << "Shape::draw() called" << endl;

    }

};

class Circle : public Shape {

public:

    virtual void draw() {

        cout << "Circle::draw() called" << endl;

    }

};

int main() {

    Shape *pShape = new Circle();   // 업캐스팅

    pShape->paint();

    delete pShape;

}