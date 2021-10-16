# dtype 배열 예저
import numpy as np

arr = np.array([0, 1, 2, 3, 4], dtype = float)

print(arr) # [0. 1. 2. 3. 4.]
print(arr.dtype) # 'float64'
print(arr.astype(int)) #[0 1 2 3 4]

#astype를 이용해서 다른 타입으로 바꿀 수 있다.