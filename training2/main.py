import tracker
import os

def dataLoader(folder_path):
    data = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    values = line.strip().split()
                    if len(values) == 5:
                        id_, x, y, width, height = values
                        obj = None
                    elif len(values) == 6:
                        id_, x, y, width, height, obj = values
                    else:
                        continue  # Skip malformed lines
                    data.append({
                        'id': int(id_),
                        'x': float(x),
                        'y': float(y),
                        'width': float(width),
                        'height': float(height),
                        'object': obj if obj is not None else None,
                        'filename': filename
                    })
    return data

# Load the data
pre = dataLoader("pre-labels")
track = dataLoader("track-lables")

# Print to verify
print(pre[:5])  # Only show first 5 to avoid overload
print(track[:5])

# Tracker logic
tracker_instance = tracker.tracker()

# Process data grouped by filename
from collections import defaultdict

grouped = defaultdict(list)
for entry in pre:
    grouped[entry['filename']].append(entry)

x= 0
for filename, group in grouped.items():
    print(f"\nProcessing file: {filename}")
    print(type(group))  # Should be a list of dicts
    print(x)
    x+=1
    tracker_instance.track(group)