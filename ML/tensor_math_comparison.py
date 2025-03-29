import torch
x = torch.tensor([1,2,3])
y = torch.tensor([9,8,7])

#Addition
z1 = torch.empty(3)
torch.add(x, y, out=z1)

z2 = torch.add(x,y)

z3 = x + y

#Subtraction

z4 = x - y

#Division
z5 = torch.true_divide(x, y)

#inplace operations
t = torch.zeros(3)
t.add_(x) #_ is inplace opertaions.
t += x 

#Exponentiation
z = x.pow(2)
z = x ** 2 

#Simple comparisons
z = x > 100
print(z)

#Matrix multiplication
x1 = torch.rand((2,5))
x2 = torch.rand((5,3))
x3 = torch.mm(x1,x2)
#x3 = x1.mm(x2)

#Matrix exponentiattion
matrix_exponent = torch.rand(5,5)
matrix_exponent.matrix_power(4)


#Element-wise multiplication

z = x * y 
print(z)

#Dot product
z = torch.dot(x, y) #Summation of the multiplication

#Batch matrix multiplication
batch = 32
n = 10
m = 20
p = 30

tensor1 = torch.rand((batch, n , m))
tensor2 = torch.rand((batch, m, p))
out_bmm = torch.bmm(tensor1, tensor2) #results in (batch, n, p)


#Examples of bradcasting
x1 = torch.rand((5,5))
x2 = torch.rand((1, 5)) #Automatically expands

z = x1 - x2 
z = x1 ** x2

sum_x = torch.sum(x, dim=0)
values, indices = torch.max(x, dim=0) #Since we only have a vector
values, indices = torch.min(x, dim=0) #Since we only have a vector
abs_x = torch.abc(x)
z = torch.argmax(x, dim=0)
z = torch.argmin(x, dim=0)
mean_x = torch.mean(x.float(), dim=0)
z = torch.eq(x, y) #Checks for equality.
torch.sort(y, dim=0, descending=False)

torch.clamp(x, min=0) #all elements lesser than 0 will be set to 0, can work for max as well

x = torch.tensor([1,0,1,1,1,1], dtype=torch.bool)
z = torch.any(x)
z = torch.all(x) #All will be false.
