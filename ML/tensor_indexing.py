import torch
batch_size = 10
features = 25
x = torch.rand((batch_size, features))

print(x[0].shape)

print(x[:, 0].shape)

print(x[2,0:10]) #Creates a list from 0 -> 9

x = torch.arange(10)
indices = [2, 5, 8] # 3rd, 6th and 9th value
print(x[indices])

x = torch.rand((3,5))
rows = torch.tensor([1,0])
cols = torch.tensor([4, 0])
print(x[rows, cols].shape)

x = torch.arange(10)
print(x[(x<2) | (x>8)])
print(x[x.remainder(2) == 0])

print(torch.where(x > 5, x, x*2)) #if value is greater than 5, change to x otherwise update.
print(torch.tensor([0,0,1,2,3,4]).unique())
print(x.ndimension()) # 5*5*5 = 3
print(x.numel()) #Number of elements