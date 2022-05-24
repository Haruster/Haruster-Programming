#include <iostream>
#include <string>

using namespace std;

class TV {

    int size;   // 스크린 크기

public:

    TV() {size = 20;}
    TV(int size) {this->size = size;}

    int getSize() {return size;}

};

class WideTV : public TV {  // TV를 상속받는 WideTV 

    bool videoln;

public:

    WideTV(int size, bool videoln) : TV(size) {

        this->videoln = videoln;

    }

    bool getVideoln() { return videoln; }

};

class SmartTV : public WideTV { // WideTV를 상속받는 SmartTV

    string ipAddr;  // 인터넷 주소

public:

    SmartTV(string ipAddr, int size) : WideTV(size, true) {

        this->ipAddr = ipAddr;

    }

    string getipAddr() {return ipAddr;}

};

int main() {

    // 32인치 크기에 "192.0.0.1"의 인터넷 주소를 가지는 스마트 TV 객체 생성

    SmartTV htv("192.0.0.1", 32);

    cout << "size = " << htv.getSize() << endl;
    cout << "videoln = " << boolalpha << htv.getVideoln() << endl;
    cout << "IP = " << htv.getipAddr() << endl;

}