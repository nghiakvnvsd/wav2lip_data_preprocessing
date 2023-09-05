
import os
import concurrent.futures
import cv2
import dlib
import subprocess
import sys

dataset_path = sys.argv[1]
presenter_name = sys.argv[2]
n_processes = int(sys.argv[3])

input_video_path = os.path.join(dataset_path, presenter_name, 'full_voice_25fps')
output_video_path = os.path.join(dataset_path, presenter_name, 'videos_crop')

if not os.path.exists(output_video_path):
    os.makedirs(output_video_path)
source_dir = os.listdir(input_video_path)
print(source_dir)
def crop_video(name_video):
    vid_path = os.path.join(input_video_path, name_video)
    out_path = os.path.join(output_video_path, name_video)
    
    detector = dlib.get_frontal_face_detector()

    # Load the video
    cap = cv2.VideoCapture(vid_path)

    # Get the first frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        exit()

    # Detect face in the first frame
    faces = detector(frame)

    # Check if any face is detected
    if len(faces) > 0:
        # Get the bounding box of the first face detected
        x, y, w, h = faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height()
        y = max(0, y - int(0.8*w))
        h = 3*h
        x = (2*x + w - h)//2
        w = h
        # Use ffmpeg to crop the video based on the bounding box
        command = f"ffmpeg -y -i {vid_path} -filter:v \"crop={w}:{h}:{x}:{y}\" -b:v 4M {out_path}"
        subprocess.call(command, shell=True)

    cap.release()
    
with concurrent.futures.ProcessPoolExecutor(n_processes) as executor:
    inputs = [x for x in source_dir]
    executor.map(crop_video, inputs)