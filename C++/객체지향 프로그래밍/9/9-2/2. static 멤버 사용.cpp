#include <iostream>

using namespace std;

class Person {

public:

    int money;  // 개인 소유의 돈

    void addMoney(int money) {

        this->money += money;

    }

    static int sharedMoney;     // 공급

    static void addShared(int n) {

        sharedMoney += n;

    }

};

// static 변수 생성. 전연 공간에 생성한다.

int person::sharedMoney = 10;   // 10으로 초기화한다.

// main함수

int main() {

    Person han;

    han.money = 100;    // han의 개인 돈 = 100  
    han.sharedMoney = 200;  // static 멤버 접근, 공급 = 200

    Person lee;

    lee.money = 150;    // lee의 개인돈 = 150
    lee.addMoney(200);  // lee의 개인돈 = 350
    lee.addShared(200); // static 멤버 접근, 공급 = 400

    cout << han.money << ' ' << lee.money << endl;
    cout << han.sharedMoney << ' ' << lee.sharedMoney << endl;

}