#include <iostream>

using namespace std;

int main(void) {
	int one = 1;
	int two = 2;
	int three = 3;
	int four = 4;

	int data_1 = one + two;
	int data_2 = two - one;
	int data_3 = three * four;
	int data_4 = four / three;
	int data_5 = four % three;

	cout << "+" << data_1 << endl;
	cout << "-" << data_2 << endl;
	cout << "*" << data_3 << endl;
	cout << "-" << data_4 << endl;
	cout << "%" << data_5 << endl;

	return 0;

}