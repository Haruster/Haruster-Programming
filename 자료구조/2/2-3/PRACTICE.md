- 순환호출에서는 순환호출을 할 때마다 문제의  크기가 작아져야 한다. 

1. 팩토리얼 계산 문제에서 순환호출이 일어날 때마다 문제가 어떻게 작아지는가?

> n! = n * (n-1)!로 n을 곱한 다음 (n-1)!을 구한다.

2. 하노이의 탑에서 순환호출이 일어날 때마다 문제가 어떻게 작아지는가?

> 하나의 원판을 이동시킨 다음에 나머지 원판에 대하여 순환호출을 한다.