import torch
import torch.nn as nn

torch.manual_seed(42)

# XOR training data
x = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Neural network with a hidden layer
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.Tanh(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

# Loss and optimizer
loss_function = nn.BCELoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.05
)

print("NYXARA AI - DAY 4")
print("XOR LEARNING EXPERIMENT")
print("----------------------")

print("Initial parameters:", sum(
    p.numel() for p in model.parameters()
))

# Training loop
for epoch in range(2000):

    prediction = model(x)

    loss = loss_function(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 400 == 0:
        print(
            f"Epoch {epoch + 1}, "
            f"Loss: {loss.item():.6f}"
        )

# Test the trained model
print("\nFINAL XOR PREDICTIONS")

with torch.no_grad():
    predictions = model(x)

    for i in range(len(x)):
        a = int(x[i][0].item())
        b = int(x[i][1].item())
        probability = predictions[i].item()
        predicted_class = int(probability >= 0.5)

        print(
            f"{a} XOR {b} = {predicted_class} "
            f"(probability: {probability:.4f}, "
            f"expected: {int(y[i].item())})"
        )
