import torch
import torch.nn as nn
from torch.utils.data import TensorDataset,DataLoader

print('Nyxara Ai - Day 7')
print('Training Loops and Validation')
print('-----------------------------')

torch.manual_seed(42)
x=torch.linspace(-5,5,100).reshape(-1,1)
y=3*x+2

indices=torch.randperm(100)
train_indices=indices[:80]
validation_indices=indices[80:]

x_train=x[train_indices]
y_train=y[train_indices]
x_validation=x[validation_indices]
y_validation=y[validation_indices]
train_dataset=TensorDataset(x_train,y_train)
validation_dataset=TensorDataset(x_validation,y_validation)

train_loader=DataLoader(
    train_dataset,
    batch_size=10,
    shuffle=True
)

validation_loader=DataLoader(
    validation_dataset,
    batch_size=10,
    shuffle=False
)

model=nn.Linear(1,1)
loss_function=nn.MSELoss()
optimizer=torch.optim.SGD(model.parameters(),lr=0.1)

epochs=100
for epoch in range(epochs):
    model.train()
    total_train_loss=0.0

    for inputs,targets in train_loader:
        optimizer.zero_grad()
        predictions=model(inputs)
        loss=loss_function(predictions,targets)
        loss.backward()
        optimizer.step()
        total_train_loss+=loss.item()*inputs.size(0)
    average_train_loss=total_train_loss/len(train_dataset)

    model.eval()
    total_validation_loss=0.0
    with torch.no_grad():
        for inputs,targets in validation_loader:
            predictions=model(inputs)
            loss=loss_function(predictions,targets)
            total_validation_loss+=loss.item()*inputs.size(0)
        average_validation_loss=total_validation_loss/len(validation_dataset)
    if (epoch+1)%10==0:
        print(f"Epoch{epoch+1:3d}/{epochs} | ")
        print(f'Training Loss : {average_train_loss:.6f}')
        print(f'Validation Loss : {average_validation_loss:.6f}')

print("\nLEARNED PARAMETERS")
print("------------------")
print("Learned weight:", model.weight.item())
print("Learned bias:", model.bias.item())

test_input = torch.tensor([[4.0]])

model.eval()
with torch.no_grad():
    test_prediction = model(test_input)

print("\nNEW PREDICTION")
print("--------------")
print("Input:", test_input.item())
print("Predicted output:", test_prediction.item())
print("Expected output:", 14.0)