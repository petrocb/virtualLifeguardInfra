import os
import random
import shutil

# Define paths
image_dir = r"C:\Users\petro\Desktop\fames"
label_dir = r"C:\Users\petro\Desktop\trainingData\edited"
train_image_dir = "dataset/images/train/"
val_image_dir = "dataset/images/val/"
train_label_dir = "dataset/labels/train/"
val_label_dir = "dataset/labels/val/"

# Create directories if they don't exist
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]

# Shuffle and split
random.shuffle(image_files)
split_idx = int(len(image_files) * 0.8)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Copy files for training set
for file in train_files:
    try:
        # Copy image
        shutil.copy(os.path.join(image_dir, file), os.path.join(train_image_dir, file))
        # Copy label
        shutil.copy(os.path.join(label_dir, file.replace(".png", ".txt")), os.path.join(train_label_dir, file.replace(".png", ".txt")))
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Error copying file {file}: {e}")

# Copy files for validation set
for file in val_files:
    try:
        # Copy image
        shutil.copy(os.path.join(image_dir, file), os.path.join(val_image_dir, file))
        # Copy label
        shutil.copy(os.path.join(label_dir, file.replace(".png", ".txt")), os.path.join(val_label_dir, file.replace(".png", ".txt")))
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Error copying file {file}: {e}")

print("Dataset split completed!")
