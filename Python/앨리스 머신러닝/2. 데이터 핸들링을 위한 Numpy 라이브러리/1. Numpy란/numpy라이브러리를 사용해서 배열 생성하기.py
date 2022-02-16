# numpy라이브러리를 이용해서 배열 생성하기 
import numpy as np

np_arr = np.array(range(5)) #0부터 5까지의 배열을 생성한다.
 
print(np_arr) # [0 1 2 3 4 5] -> 공백으로 구분된다. (콤마 : 리스트, 배열 : 공백)
print(type(np_arr)) # <class 'numpy.ndarray'> -> ndarray = n차원의 배열을 의미한다.