import os
import sys
import subprocess
import concurrent.futures

dataset_path = sys.argv[1]
presenter_name = sys.argv[2]
n_processes = int(sys.argv[3])

input_video_path = os.path.join(dataset_path, presenter_name, 'videos_crop')
output_video_path = os.path.join(dataset_path, presenter_name, 'videos_segment')
if not os.path.exists(output_video_path):
    os.makedirs(output_video_path)
source_dir = os.listdir(input_video_path)

def segment(name_video):
    video_path = os.path.join(input_video_path, name_video)
    split_video_path = video_path.replace('videos_crop', 'videos_segment').replace('.mp4', '').replace('.MP4', '')
    if not os.path.exists(split_video_path):
        os.makedirs(split_video_path)
    split_audio_path = video_path.replace('videos_crop', 'audios_segment').replace('.mp4', '').replace('.MP4', '')
    if not os.path.exists(split_audio_path):
        os.makedirs(split_audio_path)
    command = f"ffmpeg -nostdin -y -i {video_path} 2>&1 | grep Duration | sed 's/Duration: \(.*\), start/\\1/g'"
    output_terminal = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
    duration_video = int(float(output_terminal.split(":")[1]) * 60 + float(output_terminal.split(":")[2]))
    segment_time = list(range(0, duration_video, 10))
    for i in range(0, len(segment_time) - 1):
        small_video_path = os.path.join(split_video_path, f'{segment_time[i]}_{segment_time[i+1]}.mp4')
        small_audio_path = os.path.join(split_audio_path, f'{segment_time[i]}_{segment_time[i+1]}.wav')
        vid_command = f"ffmpeg -nostdin -y -ss {segment_time[i]} -i {video_path} -t 10 -filter:v fps=25 -b:v 4M {small_video_path}"
        vid_status = os.system(vid_command)
        # aud_command = f"ffmpeg -ss {segment_time[i]} -i {audio_path} -t 10 -ar 16000 {small_audio_path}"
        aud_command = f"ffmpeg -nostdin -y -i {small_video_path} -ar 16000 {small_audio_path}"
        aud_status = os.system(aud_command)
        print(small_video_path, vid_status, aud_status)
        
with concurrent.futures.ProcessPoolExecutor(n_processes) as executor:
    inputs = [x for x in source_dir]
    executor.map(segment, inputs)
