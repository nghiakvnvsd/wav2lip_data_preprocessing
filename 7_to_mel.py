import os
import sys
import audio
import numpy as np

dataset_path = sys.argv[1]
presenter_name = sys.argv[2]
token = sys.argv[3]

obj_path = os.path.join(dataset_path, presenter_name)

ROOT = os.path.join(obj_path, f"output_{token}")

with open(os.path.join(obj_path, f"filelist_{token}/raw_filelist.txt"), "r") as f:
    data = f.readlines()
data = [line.strip() for line in data]
data.sort()

start = 0
end = len(data)

data = data[start:]
print("Data", start, end, len(data))
sample_rate = 16000
error = []

for d in data:
    try:
        mel_out_path = os.path.join(d, "mel.npy")

        wavpath = os.path.join(d, "synced_audio.wav")

        wav = audio.load_wav(wavpath, sample_rate)

        orig_mel = audio.melspectrogram(wav).T
        with open(mel_out_path, "wb") as f:   
            np.save(f, orig_mel)
    except Exception:
        print("Error", d)
        error.append(d)

with open(os.path.join(obj_path, f"filelist_{token}/temp/output_data_mel_errors_{start}_{end}.txt"), "w") as f:
    for line in error:
        f.write(line + "\n")
