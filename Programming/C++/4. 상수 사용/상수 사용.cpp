#include <iostream>

using namespace std;

int main(void) {
	const int kone = 1;
	const int ktwo = 2;

	const int ksum = kone * ktwo;

	cout << "sum의 값은 :" << ksum << "입니다." << endl;

	return 0;
}



//구글에서는 변수와 상수를 구분하기 위해서 변수명 앞에 k를 붙이는 것을 권장한다.