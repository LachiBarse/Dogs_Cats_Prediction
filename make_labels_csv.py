import os
import pandas as pd

# Prepare label data
data = []

# Define your image folders
folders = {
    'cat': r"C:\Users\lachi\Documents\PetImages\Cat",
    'dog': r"C:\Users\lachi\Documents\PetImages\Dog"
}

for label, folder in folders.items():
    for fname in os.listdir(folder):
        if fname.lower().endswith(('.jpg', '.png', '.jpeg')):
            data.append([fname, label])

# Create DataFrame and save
df = pd.DataFrame(data, columns=['filename', 'label'])
df.to_csv('labels.csv', index=False)
print("✅ Created labels.csv with", len(df), "entries")
