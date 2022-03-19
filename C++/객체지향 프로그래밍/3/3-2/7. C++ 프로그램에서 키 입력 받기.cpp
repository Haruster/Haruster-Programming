// c++ 프로그램에서 키입력 받기

#include <iostream>

using namespace std;

int main() {

    int width;
    int height;

    cout << "너비를 입력해주세요 : " << endl;

    cin >> width; // width를 입력받는다.

    cout << "높이를 입력해주세요 : " << endl;

    cin >> height; // height를 입력받는다.

    cout << "너비는 " << width << "이고" << "높이는" << height << "입니다." << endl;

    int area = width * height;

    cout << "면적은 " << area << "입니다." << endl;

    return 0;


    

}