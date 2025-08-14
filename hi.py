import cv2
import os


video_path = 'wallpaper.mp4'
output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = 24
frame_count = 0

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f'frame_{frame_count}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f'{frame_count} fps "{output_folder}"')
