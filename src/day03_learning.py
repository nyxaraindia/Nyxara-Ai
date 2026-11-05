import torch
import torch.nn as nn

torch.manual_seed(42)

# Training data
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = 2 * x + 1

# Create a model with randomly initialized parameters
model = nn.Linear(1, 1)

# Loss function and optimizer
loss_function = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

print("NYXARA AI - FIRST LEARNING EXPERIMENT")
print("-------------------------------------")

print("Initial weight:", model.weight.item())
print("Initial bias:", model.bias.item())

# Training
for epoch in range(300):

    # Forward pass
    prediction = model(x)

    # Calculate error
    loss = loss_function(prediction, y)

    # Calculate gradients
    optimizer.zero_grad()
    loss.backward()

    # Update parameters
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(
            f"Epoch {epoch + 1}, "
            f"Loss: {loss.item():.6f}"
        )

print("\nTRAINING COMPLETED")

print("Learned weight:", model.weight.item())
print("Learned bias:", model.bias.item())

# Test with new input
test_input = torch.tensor([[6.0]])

with torch.no_grad():
    result = model(test_input)

print("Input:", test_input.item())
print("Predicted output:", result.item())
print("Expected output:", 13.0)
