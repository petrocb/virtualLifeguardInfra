import os

image_dir = r"C:\Users\petro\Desktop\fames"
label_dir = r"C:\Users\petro\Desktop\trainingData\edited"

# Check image files
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
print(f"Found {len(image_files)} image files in {image_dir}.")

# Check label files
label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]
print(f"Found {len(label_files)} label files in {label_dir}.")