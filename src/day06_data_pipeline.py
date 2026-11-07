
import torch
from torch.utils.data import TensorDataset, DataLoader

print("NYXARA AI - DAY 6")
print("DATASET AND DATA PIPELINE")
print("-------------------------")

# 1. Create 12 input samples
inputs = torch.arange(
    1, 13, dtype=torch.float32
).unsqueeze(1)

# 2. Create corresponding targets
targets = 2 * inputs + 1

# 3. Combine inputs and targets
dataset = TensorDataset(inputs, targets)

# 4. Create a DataLoader
loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True,
    generator=torch.Generator().manual_seed(42)
)

print("Total samples:", len(dataset))
print("Batch size:", 4)
print("Batches per epoch:", len(loader))

# 5. Process the dataset for 2 epochs
for epoch in range(1, 3):

    print(f"\nEPOCH {epoch}")
    print("----------------")

    for batch_number, (batch_x, batch_y) in enumerate(
        loader, start=1
    ):

        print(
            f"Batch {batch_number} | "
            f"Inputs: {batch_x.squeeze().tolist()} | "
            f"Targets: {batch_y.squeeze().tolist()}"
        )

print("\nDATA PIPELINE COMPLETED")

