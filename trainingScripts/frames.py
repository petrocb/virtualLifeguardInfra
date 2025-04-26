import cv2
import os

def extract_frames(video_path, output_folder, filename_prefix):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    frame_count = 0
    success = True

    while success:
        success, frame = cap.read()
        if success:
            # Generate frame filename
            frame_filename = os.path.join(output_folder, f"{filename_prefix}_{frame_count}.png")
            # Save the frame as an image
            cv2.imwrite(frame_filename, frame)
            # print(f"Saved frame {frame_count}: {frame_filename}")
            frame_count += 1

    cap.release()
    # print(f"Extracted {frame_count} frames to {output_folder}.")

# Example usage
video_path = r"C:\Users\petro\Desktop\videos\edit\20241123edit.mp4"  # Path to your video file
output_folder = r"C:\Users\petro\Desktop\videos\edit\20241123edit"      # Folder to save the frames
filename_prefix = "20241123edit"     # Prefix for frame filenames

extract_frames(video_path, output_folder, filename_prefix)
