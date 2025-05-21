from pathlib import Path
import shutil

# Define source and destination paths
frames_path = Path("frames")
labels_path = Path("results")

train_img_dst = Path("images/train")
val_img_dst = Path("images/val")
train_lbl_dst = Path("labels/train")
val_lbl_dst = Path("labels/val")

# Create destination folders
for path in [train_img_dst, val_img_dst, train_lbl_dst, val_lbl_dst]:
    path.mkdir(parents=True, exist_ok=True)

# List and sort image and label files
image_files = sorted(frames_path.glob("*.jpg"))
label_files = sorted(labels_path.glob("*.txt"))

# Split 80/20
split_idx = int(len(image_files) * 0.8)
train_imgs, val_imgs = image_files[:split_idx], image_files[split_idx:]
train_lbls, val_lbls = label_files[:split_idx], label_files[split_idx:]

# Copy image files
for f in train_imgs:
    shutil.copy(f, train_img_dst / f.name)
for f in val_imgs:
    shutil.copy(f, val_img_dst / f.name)

# Copy corresponding label files
for f in train_lbls:
    shutil.copy(f, train_lbl_dst / f.name)
for f in val_lbls:
    shutil.copy(f, val_lbl_dst / f.name)

(train_img_dst, val_img_dst, train_lbl_dst, val_lbl_dst)
