
import torch

print("NYXARA AI - DAY 5")
print("GRADIENT DESCENT EXPERIMENT")
print("---------------------------")

learning_rates = [0.1, 0.5, 1.1]

for lr in learning_rates:
    weight = torch.tensor(0.0, requires_grad=True)

    print(f"\nLearning Rate: {lr}")
    print("Initial weight:", weight.item())

    for step in range(10):
        # Calculate the loss
        loss = (weight - 3) ** 2

        # Calculate the gradient
        loss.backward()

        # Update the weight
        with torch.no_grad():
            weight -= lr * weight.grad

        # Clear the old gradient
        weight.grad.zero_()

        print(
            f"Step {step + 1:02d} | "
            f"Weight: {weight.item():.6f} | "
            f"Loss: {((weight - 3) ** 2).item():.6f}"
        )

    print("Final weight:", weight.item())
