import cv2
from pathlib import Path

# Video file path
video_path = Path("bondiRamp2_20241207_225001.mp4")  # Replace with your actual video path
output_dir = Path("frames")
output_dir.mkdir(parents=True, exist_ok=True)

# Open video
cap = cv2.VideoCapture(str(video_path))
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = output_dir / f"bondiRamp2_20241207_225001_{frame_count+1}.jpg"
    cv2.imwrite(str(frame_filename), frame)
    frame_count += 1

cap.release()

