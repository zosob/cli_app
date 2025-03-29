import torch
import torch.backends
import torch.backends.mps 

#Initialize a tensor...

device = "mps" if torch.backends.mps.is_available() else "cpu"
my_tensor = torch.tensor([[1,2,3],[4,5,6]], dtype = torch.float32, device=device, requires_grad= True)
print(my_tensor)

print(my_tensor.device)
print(my_tensor.shape)
print(my_tensor.requires_grad)

#Other initialization methods...
x = torch.empty(size= (3,3)) #Garbage values
x = torch.zeros((3, 3)) #Zero values
x = torch.rand((3,3)) #Values from uniform distribution 
x = torch.ones((3,3))
x = torch.eye(5,5) #Identity matrix
x = torch.arange(start=0, end=5, step=1)
x = torch.linspace(start=0.1, end=1, steps=10)
x = torch.empty(size=(1,5)).normal_(mean=0, std=1)
x = torch.empty(size=(1,5)).uniform_(0,1)
x = torch.diag(torch.ones(3))
print(x)


#Initialize and convert tenros to other types

tensor = torch.arange(4)
print(tensor.bool())
print(tensor.short()) #Int16
print(tensor.long()) #Int64
print(tensor.half()) #Float16
print(tensor.float())
print(tensor.double())


#Convert
import numpy as np
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)
np_array_back = tensor.numpy()
print(np_array)