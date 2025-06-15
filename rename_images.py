import os

def rename_images(folder, label):
    files = [f for f in os.listdir(folder)
             if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    files.sort()
    for i, fname in enumerate(files, start=1):
        ext = os.path.splitext(fname)[1]
        new_name = f"{label}_{i:04d}{ext}"
        os.rename(os.path.join(folder, fname),
                  os.path.join(folder, new_name))
    print(f"Renamed {len(files)} files in '{folder}'")

# ← Replace these with your actual folder paths
rename_images(r"C:\Users\lachi\Documents\PetImages\Cat", "cat")
rename_images(r"C:\Users\lachi\Documents\PetImages\Dog", "dog")
