# 수행 시간 측정 예 -1 (clock()함수)

#include <time.h>

start = clock();

....

stop = clock();

double duration = (double)(stop - start) / CLOCKS_PER_SEC;