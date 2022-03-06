# 수행시간 측정 예 -2(time()함수 사용)

#include <time.h>

start = time(NULL);

...

stop = time(NULL);

double duration = (double) difftime(stop, start);