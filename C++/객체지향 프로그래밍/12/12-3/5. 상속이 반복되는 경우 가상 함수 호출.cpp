// 상속이 반복되는 경우 가상 함수 호출

#include <iostream>

using namespace std;

class Base {

public:

    virtual void f() { cout << "Base::f() called" << endl; }

};

class Derrived : public Base {

public:

    void f() { cout << "Derived::f() called" << endl; }

};

class GrandDerived : public Derrived {

public:

    void f() { cout << "GrandDerrived::f() called" << endl; }

};

int main() {

    GrandDerived g;

    Base *bp;

    Derrived *dp;

    GrandDerived *gp;

    bp = dp = gp = &g;

    bp->f();
    dp->f();
    gp->f();

}