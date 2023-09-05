# Parallel Wav2Lip Data Preprocessing 

### 1. Run convert video to standard 25 FPS
assume dataset is located "your-folder-dataset"
```bash
python3 1_convert_25fps.py <your-folder-dataset> <presenter_name> <n_processes>
```
it will automatically create new folder name ***your-folder-dataset/full_voice_25fps***

the  folder structure: 
```
your-folder-dataset
|---full_voice
|       video1.mp4
|       video2.mp4
|       ..........
|---full_voice_25fps
|       video1.mp4
|       video2.mp4
|       ..........
```


### 2. Run to crop video

```bash
python3 2_crop_video.py <your-folder-dataset> <presenter_name> <n_processes>
```
it will automatically create new folder name ***your-folder-dataset/videos_crop*** 

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|       video1.mp4
|       video2.mp4
|       ..........
```


### 3. Run to split each video into 10s videos

```bash
python3 3_segment.py <your-folder-dataset> <presenter_name> <n_processes>
```
it will automatically create new folder name ***your-folder-dataset/videos_segment***  and ***your-folder-dataset/audios_segment*** 

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|---videos_segment
|---------video1
|             0_10.mp4
|             10_20.mp4
|             .........
|---------video2
|             0_10.mp4
|             10_20.mp4
|             .........
|---------.............
|---audios_segment
|---------video1
|             0_10.wav
|             10_20.wav
|             .........
|---------video2
|             0_10.wav
|             10_20.wav
|             .........
|---------.............
```


### 4. Run face detection 

```bash
python3 4_detection.py <your-folder-dataset> <presenter_name> <n_processes>
```
it will automatically create new folder name ***your-folder-dataset/output*** 

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|---videos_segment
|---audios_segment
|---output
|---------video1
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|-------------...........
|---------video2
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|-------------...........
|---------.......
```


### 5. Create filelist structure for wav2lip training 

```bash
python3 5_create_filelist.py <your-folder-dataset>
```
it will automatically create new folder name ***your-folder-dataset/filelist*** 

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|---videos_segment
|---audios_segment
|---output
|---filelist
|       raw_filelist.txt
|       raw_filelist_errors.txt
```

### 6. Correct audio with video (audio lenght less than video length after converting to 25fps)

```bash
python3 6_au_sync.py <your-folder-dataset>
```
it will automatically create new folder name ***your-folder-dataset/filelist/temp*** 

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|---videos_segment
|---audios_segment
|---output
|---------video1
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|-------------...........
|---------video2
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|-------------...........
|---------.......
|---filelist
|       raw_filelist.txt
|       raw_filelist_errors.txt
|-------temp
|         output_synced_<start>_<len(data)>.txt
|         output_synced_errors_<start>_<len(data)>.txt
```

### 7. Convert audio to mel spectrogram

```bash
python3 7_to_mel.py <your-folder-dataset>
```

the  folder structure: 
```
your-folder-dataset
|---full_voice
|---full_voice_25fps
|---videos_crop
|---videos_segment
|---audios_segment
|---output
|---------video1
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|               mel.npy
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|               mel.npy
|-------------...........
|---------video2
|-------------0_10
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|               mel.npy
|-------------10_20
|               00000.jpg
|               00001.jpg
|               00002.jpg
|               .........
|               audio.wav
|               synced_audio.wav
|               mel.npy
|-------------...........
|---------.......
|---filelist
|       raw_filelist.txt
|       raw_filelist_errors.txt
|-------temp
|         output_synced_<start>_<len(data)>.txt
|         output_synced_errors_<start>_<len(data)>.txt
|         output_data_mel_errors_<start>_<len(data)>.txt
```
