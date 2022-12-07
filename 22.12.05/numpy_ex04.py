import numpy as np
array = np.array([[5,3,9,7],[3,10,5,4]])
print("각 열을 기준으로 정렬 전 \n", array)

array.sort(axis=0)
print("각 열을 기준으로 정렬 후 \n", array)