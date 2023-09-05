import cv2
import mediapipe as mp
import os
import sys
import subprocess
import concurrent.futures

dataset_path = sys.argv[1]
presenter_name = sys.argv[2]
n_processes = int(sys.argv[3])

input_video_path = os.path.join(dataset_path, presenter_name, 'videos_segment')
output_video_path = os.path.join(dataset_path, presenter_name, 'output')
if not os.path.exists(output_video_path):
    os.makedirs(output_video_path)
id_vids = os.listdir(input_video_path)
arr_path_vid = []
for id_vid in id_vids:
    path_id_vid = os.path.join(input_video_path, id_vid)
    if not os.path.exists(path_id_vid.replace("videos_segment", "output")):
        os.makedirs(path_id_vid.replace("videos_segment", f"output"))
    split_vids = os.listdir(path_id_vid)
    for split_vid in split_vids:
        if "mp4" in split_vid or "MP4" in split_vid:
            path_split_vid = os.path.join(path_id_vid, split_vid)
            arr_path_vid.append(path_split_vid)
mp_face_mesh = mp.solutions.face_mesh

def detection(path_split_vid):
    path_output = path_split_vid.replace("videos_segment", f"output").replace(".mp4" , "").replace(".MP4", "")
    if not os.path.exists(path_output):
        os.makedirs(path_output)
    cap = cv2.VideoCapture(path_split_vid)
    flag_person = True
    t = 0
    while cap.isOpened():
        path_output_image = f'{path_output}/{str(t).zfill(5)}.jpg'
        print(path_output_image)
        ret, img = cap.read()
        if not ret:
            break
        h, w, _ = img.shape

        with mp_face_mesh.FaceMesh( static_image_mode=True, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:   
            results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # Draw face detections of each face.
            if not results.multi_face_landmarks:
                flag_person = False
                break
            for face_landmarks in results.multi_face_landmarks:
                face_indices = face_landmarks.landmark[:-10]
            x1, x2, y1, y2 = int(face_indices[234].x*w), int(face_indices[454].x*w), int(face_indices[10].y*h), int(face_indices[152].y*h)

            y2 = y2 + int((y2 - y1)*0.14)
            www = x2 - x1
            x1 = x1 - int(0.07*www)
            x2 = x2 + int(0.07*www)
            img_final = img[y1:y2, x1: x2]
            cv2.imwrite(path_output_image, img_final, [cv2.IMWRITE_JPEG_QUALITY, 100])
            t+=1
    cap.release()
    
    # Delete the video if one frame does not include the presenter's face
    if not flag_person:
        command = f'rm -r {path_output}'
        subprocess.call(command, shell=True)
        return
    
    #Copy audio
    old_audio = path_split_vid.replace("videos_segment", 'audios_segment').replace(".mp4",".wav")
    new_audio = path_split_vid.replace("videos_segment", f"output").replace('.mp4', '')
    command = f"cp {old_audio} {new_audio}/audio.wav"
    subprocess.call(command, shell=True)
    
with concurrent.futures.ProcessPoolExecutor(n_processes) as executor:
    inputs = [x for x in arr_path_vid]
    executor.map(detection, inputs)
        


