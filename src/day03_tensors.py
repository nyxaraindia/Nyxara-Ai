import torch

# 1. Scalar
scalar = torch.tensor(5)

# 2. Vector
vector = torch.tensor([1, 2, 3])

# 3. Matrix
matrix = torch.tensor([
    [1, 2],
    [3, 4]
])

# 4. Display tensors
print("NYXARA AI - DAY 3")
print("-----------------")

print("Scalar:")
print(scalar)

print("\nVector:")
print(vector)

print("\nMatrix:")
print(matrix)

# 5. Matrix shape
print("\nMatrix shape:", matrix.shape)

# 6. Matrix addition
print("\nMatrix addition:")
print(matrix + matrix)

# 7. Matrix multiplication
print("\nMatrix multiplication:")
print(matrix @ matrix)
