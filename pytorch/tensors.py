import torch
import numpy as np

### Creating tensors
# Scalar
scalar = torch.tensor(7)
print("Scalar:", scalar)

# Vector
vector = torch.tensor([7, 7])
print("Vector:", vector)

# Matrix
MATRIX = torch.tensor([[7, 8],
                       [9, 10]])
print("MATRIX:", MATRIX)

# Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
print("TENSOR:", TENSOR)

# Random tensors
random_tensor = torch.rand(size=(3, 3))
print("Random Tensor:", random_tensor)

# All zeros tensor
zeros = torch.zeros(size=(3, 4))
print("All Zeros Tensor:", zeros)

# Range of tensors
range_tensor = torch.arange(0, 10)
print("Range Tensor:", range_tensor)

range_step = torch.arange(start=1, end=10, step=2) 
print("Range Tensor with step:", range_step)

### Tensor datatypes
# Float 32 tensor
float_32_tensor = torch.tensor([3.0, 6.0, 9.0],
                               dtype=None, 
                               device=None, 
                               requires_grad=False)
print("Float32 Tensor:", float_32_tensor)

# Float 16 tensor
float_16_tensor = float_32_tensor.type(torch.float16)
print("Float16 Tensor:", float_16_tensor)

### Manipulating tensors
# Tensor operations
tensor = torch.tensor([1, 2, 3])

# Addition
tensor += 10
print("Addition:", tensor)

# Multiplication
tensor *= 10
print("Multiplication:", tensor)

# Subtraction
tensor -= 10
print("Subtraction:", tensor)

# Division
tensor = tensor / 3  # /= not working
print("Division:", tensor)

# Element-wise multiplication
tensor = torch.tensor([1, 2, 3])
tensor *= tensor
print(tensor)

# Matrix multiplication
mul_tensor = torch.matmul(tensor, tensor)
print("Mul Tensor:", mul_tensor)

# Matrix multiplication with transpose
tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]])

tensor_B = torch.tensor([[7, 10],
                         [8, 11],
                         [9, 12]])

print(f'Original shapes: tensor_A = {tensor_A.shape}, tensor_B = {tensor_B.shape}')
print(f'New shapes: tensor_A = {tensor_A.shape}, tensor_B.T = {tensor_B.T.shape}')
print(f'Multiplying: {tensor_A.shape} @ {tensor_B.T.shape} <-- inner dimensions must match')
print("Output:\n")

output = torch.matmul(tensor_A, tensor_B.T)
print(output)
print(f"\nOutput shape: {output.shape}")

### Finding the min, max, mean & sum
# Create a Tensor
x = torch.arange(0, 100, 10)
print(x)

# Find the min
print("Min:", torch.min(x), x.min())

# Find the max
print("Max:", torch.max(x), x.max())

# Find the mean (requires tensor of float32)
print("Mean:", torch.mean(x.type(torch.float32)), x.type(torch.float32).mean())

# Find the sum
print("Sum:", torch.sum(x), x.sum())

### Finding the positional min and max
print("Position of Min:", x.argmin())
print("Position of Max:", x.argmax())

### Reshaping, stacking, squeezing and unsqueezing tensors
''' 
Reshaping - reshapes input tensor to defined shape
View - returns a view of input tensor but keeps same memory as original tensor
Stacking - combines multiple tensors on top of each other (vstack) or side by side (hstack)
Squeeze - removes all "1" dimensions from a tensor
Unsqueeze - adds a "1" dimension to a target tensor
Permute - returns a view of input with dimensions permuted (swapped) in a certain way
'''

### Reshaping
# Create a tensor
x = torch.arange(1., 10.)
print(x, x.shape)

# Add extra dimension
x_reshaped = x.reshape(1, 9)
print(x_reshaped)

### View 
# Change the view
z = x.view(1, 9)
print(z, z.shape)

# Changing z changes x (because a view of a tensor shares the same memory as the original input)
z[:, 0] = 5
print(z, x)

### Stacking
x_stacked = torch.stack([x, x, x, x], dim=1)
print(x_stacked)

### Squeeze
# Removes all single dimensions from a target tensor
x = torch.zeros(2, 1, 2, 1, 2)
print("Original Size:", x.size())
y = torch.squeeze(x)
print("Squeezed Size:", y.size())

y = torch.squeeze(x, 0)
print("After Squeeze at dim 0:", y.size())

y = torch.squeeze(x, 1)
print("After Squeeze at dim 1:", y.size())

y = torch.squeeze(x, (1, 2, 3))
print("After Squeeze at multiple dims:", y.size())

print(f"Previous tensor: {x_reshaped}")
print(f"Previous shape: {x_reshaped.shape}")

# Remove extra dimension from x_reshaped
x_squeezed = x_reshaped.squeeze()
print(f"\nNew tensor: {x_squeezed}")
print(f"New shape: {x_squeezed.shape}")

### Unsqueeze
# Adds a single dimension to a target tensor at a specific dimension
print(f"Previous target: {x_squeezed}")
print(f"Previous shape: {x_squeezed.shape}")

# Add an extra dimension with unsqueeze
x_unsqueezed = x_squeezed.unsqueeze(dim=0)
print(f"\nNew tensor: {x_unsqueezed}")
print(f"New shape: {x_unsqueezed.shape}")

### Permute 
# Rearranges the dimensions of a tensor in a specified order
x_original = torch.rand(size=(224, 224, 3))  # [height, width, colour_channels]

# Permute the original tensor to rearrange the axis (or dim) order
x_permuted = x_original.permute(2, 0, 1)  # shifts axis 0->1, 1->2, 2->0

print(f"Previous shape: {x_original.shape}")
print(f"New shape: {x_permuted.shape}")  # [colour_channels, height, width]

### Indexing (selecting data from tensors)
# Create a tensor
x = torch.arange(1, 10).reshape(1, 3, 3)
print(x, x.shape)

# Index on new tensor
print(x[0])

# Index on middle bracket (dim=1)
print(x[0][0])

# Index on most inner bracket (last dimension)
print(x[0][0][0])

# ":" to select all of a target dimension
print(x[:, 0])

# Get all values of 0th and 1st dimensions but only index of 1 of 2nd dimension
print(x[:, :, 1])

# Get all values of the 0 dimension but only the 1 index value of 1st and 2nd dimension
print(x[:, 1, 1])

# Get the index 0 of 0th and 1st dimension and all values of 2nd dimension
print(x[0, 0:])

### PyTorch tensors & NumPy
# NumPy array to tensor
array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array)  # When converting from numpy to pytorch, pytorch reflects numpy's default datatype of float64 unless specified otherwise.
print("NumPy Array:", array)
print("Tensor from NumPy:", tensor)

# Change the value of array
array = array + 1
print("Modified NumPy Array:", array)
print("Tensor remains unchanged:", tensor)

# Tensor to NumPy array 
tensor = torch.ones(7)
numpy_tensor = tensor.numpy()
print("Tensor:", tensor)
print("NumPy Array from Tensor:", numpy_tensor)

### Reproducibility
# Create two random tensors
random_tensor_A = torch.rand(3, 4)
random_tensor_B = torch.rand(3, 4)

print("Random Tensor A:", random_tensor_A)
print("Random Tensor B:", random_tensor_B)
print("Are they equal?", random_tensor_A == random_tensor_B)

# Random reproducible tensors
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
random_tensor_C = torch.rand(3, 4)
torch.manual_seed(RANDOM_SEED)
random_tensor_D = torch.rand(3, 4)

print("Random Tensor C:", random_tensor_C)
print("Random Tensor D:", random_tensor_D)
print("Are they equal?", random_tensor_C == random_tensor_D)
