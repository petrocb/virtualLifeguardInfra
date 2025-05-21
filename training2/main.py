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
                        'cls': int(id_),
                        'xywh': [float(x), float(y), float(width), float(height)],
                        # 'x': float(x),
                        # 'y': float(y),
                        # 'width': float(width),
                        # 'height': float(height),
                        'id': obj if obj is not None else None,
                        'filename': filename
                    })
    return data

# Load the data
pre = dataLoader("pre-labels")
track = dataLoader("track-labels")

# Print to verify
print(pre[:5])  # Only show first 5 to avoid overload
print(track[:5])
print(len(pre), len(track))

# Step 1: Normalize and index the track list
track_index = {}

for o in track:
    if o['cls'] not in [0, 37]:
        continue
    o_cls = 0 if o['cls'] == 37 else o['cls']
    key = (o['filename'], o_cls, o['xywh'][0], o['xywh'][1])
    track_index[key] = {
        'cls': 0,
        'xywh': o['xywh'],
        'id': o['id'],
        'filename': o['filename']
    }

max_id = max(
    (int(obj['id']) for obj in track if obj['id'] is not None and str(obj['id']).isdigit()),
    default=None
) + 1
print(f"The largest number in the last column (ID) across all files is: {max_id}")
# Step 2: Loop through pre and match using the index
combined = []

for i in pre:
    if i['cls'] not in [0, 37]:
        continue
    i_cls = 0 if i['cls'] == 37 else i['cls']
    key = (i['filename'], i_cls, i['xywh'][0], i['xywh'][1])

    if key in track_index:
        combined.append(track_index[key])
        # print(f"Matched: {i['filename']} - cls: 0 - {i['xywh']}")
    else:
        combined.append({
            'cls': 0,
            'xywh': i['xywh'],
            'id': max_id,
            'filename': i['filename']
        })
        max_id += 1
        # print(f"No match: {i['filename']}")

        # print(f"No match: {i_filename}")

        # print(f"No match: {i['filename']}")

print(len(combined), len(pre), len(track))
# print("track: ", track)
# print("track: ", track[-1])





# print("combined: ", combined)
# for o in pre:
#     if any(o['filename'] == i['filename'] and
#            o['cls'] == i['cls'] and
#            o['xywh'][0] == i['xywh'][0] and
#            o['xywh'][1] == i['xywh'][1] for i in track):
#         combined.append({
#             'cls': i['cls'],
#             'xywh': i['xywh'],
#             'id': i['id'],
#             'filename': i['filename']})
#     else:
#         combined.append({
#             'cls': o['cls'],
#             'xywh': o['xywh'],
#             'id': None,
#             'filename': o['filename']})
# Tracker logic
tracker_instance = tracker.tracker()

# Process data grouped by filename
from collections import defaultdict

grouped = defaultdict(list)
for entry in combined:
    grouped[entry['filename']].append(entry)

for filename, group in grouped.items():
    tracker_instance.track(group)