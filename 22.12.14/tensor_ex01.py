import torch
import numpy as np

data = [[1,2], [3,4]]
x_data = torch.tensor(data)
# print(x_data)
# print(x_data.shape)

# x_ones = torch.ones_like(x_data)
# print(f"ones Tensor >> \n", x_ones)
#
# x_rand = torch.rand_like(x_data, dtype=torch.float)
# print(x_rand)
# torch.randn()

# shape = (3, 3)
# randn_tensor = torch.rand(shape)
# ones_tensor = torch.ones(shape)
# zeros_tensor = torch.zeros(shape)
#
# print(f"Random Tensor >> \n {randn_tensor} \n")
# print(f"ones Tensor >> \n {ones_tensor} \n")
# print(f"zeros Tensor >> \n {zeros_tensor} \n")

# tensor = torch.rand(3,4)
# print(f"shape of tensor: {tensor.shape}")
# print(f"data type of tensor :{tensor.dtype}")
# print(f"device tensor is stored on : {tensor.device}") #어느 장치에 저장되는지

# if  torch.cuda.is_available():
#     tensor = tensor.to("cuda")
# else:
#     tensor = tensor.to("cpu")
# print(f"Device tensor is stored on : {tensor.device}")

# tensor = torch.ones(4,4)
# tensor[:, 1] = 3
# print(tensor)


#tensor 합치기
# t1 =torch.cat([tensor,tensor,tensor],dim=1)
# print(t1)
#
# print(tensor * tensor)

#tensor 곱하기 (두 방법 중 하나 택)
# print(tensor.matmul(tensor.T))
# print(tensor @ tensor.T)

#tensor 바꿔치기  1111이던 것이 6666으로 바뀜을 확인
# tensor.add_(5)
# print(tensor)

### 텐서 numpy 배열 변환
# t = torch.ones(5)
# print("tensor >> ", t)
# n = t.numpy()
# print("numpy >> ", n)

# t.add_(1)
# n = t.numpy()
# print(t)
# print(n)

### numpy 텐서 변환
# n = np.ones(5)
# t = torch.from_numpy(n)
#
# print(n)
# print(t)
# np.add(n,1,out=n)
# print(t)
# print(n)

#view
t = np.array([[[0,1,2], [3,4,5]], [[6,7,8], [9,10,11]]])
ft = torch.FloatTensor(t)
# print(ft.shape)
# print(ft)

# 3차원 텐서를 2차원 텐서로 변환
# print(ft.view([-1,3]))
# print(ft.view([-1,3]).shape)

# 3차원 텐서에서 3차원 텐서로 차원은 유지하되, 크기는 변환
# print(ft.view([-1,1,3]))
# print(ft.view([-1,1,3]).shape)

# # sqeeze - 1인 차원을 제거
# # 3X1
# ft = torch.FloatTensor([[0],[1],[2]])
# print(ft)
# print(ft.shape)
#
# print(ft.squeeze)
# print(ft.squeeze().shape)

#unsqueeze - 특정 위치에 1인 차원을 추가
ft = torch.FloatTensor([0,1,2])
print(ft)
print(ft.shape)

print(ft.unsqueeze(0))
print(ft.unsqueeze(0).shape)

print(ft.view(1,-1))
print(ft.view(1,-1).shape)