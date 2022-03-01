#include <iostream>

using namespace std;
int main() {

int one = 1;
int two = 2;
int three = 3;
int four = 4;

int data_1 = one += two;
int data_2 = two -= one;
int data_3 = four *= two;
int data_4 = four /= three;

cout << "+" << "=" << data_1 << endl;

}