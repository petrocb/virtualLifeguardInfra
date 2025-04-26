import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\petro\Desktop\videos\20241123.mp4")

# Verify if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Original FPS
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*"mp4v")

print(f"FPS: {fps}, Width: {width}, Height: {height}, Codec: {codec}")

# Define crop dimensions (bottom half of the video)
x1, y1, x2, y2 = 0, height - 400, width, height  # Crop from the middle to the bottom

# Output video writer with reduced FPS and cropped frame size
output_size = (x2 - x1, y2 - y1)  # Width and height of cropped frame
out = cv2.VideoWriter(r"C:\Users\petro\Desktop\videos\20241123edit.mp4", codec, 1, output_size)  # Set new FPS to 1

frame_count = 0
frames_to_skip = fps  # Number of frames to skip to get 1 FPS

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Only process every `fps`-th frame to reduce to 1 FPS
    if frame_count % frames_to_skip == 0:
        # Crop the frame to the bottom half
        cropped_frame = frame[y1:y2, x1:x2]  # Crop from y = height//2 to height, x = 0 to width

        # Write the cropped frame to the output file
        out.write(cropped_frame)

    frame_count += 1

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing complete. Bottom half saved at 1 FPS.")
