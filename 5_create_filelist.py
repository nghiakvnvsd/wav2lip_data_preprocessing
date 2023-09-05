import os
import sys

dataset_path = sys.argv[1]
presenter_name = sys.argv[2]
token = sys.argv[3]

path = os.path.join(dataset_path, presenter_name)
output_path = os.path.join(path, f'filelist_{token}')
if not os.path.exists(output_path):
    os.makedirs(output_path)
source_path = os.path.join(path, f'output_{token}')
data_list = os.listdir(source_path)

results = []
errors = []
for d in data_list:
    d_path = os.path.join(source_path, d)
    train_list = os.listdir(d_path)
    train_list = [t for t in train_list if os.path.isdir(os.path.join(d_path, t))]
    for t in train_list:
        t_path = os.path.join(d_path, t)

        if os.path.isfile(os.path.join(t_path, "audio.wav")):
            results.append(t_path)
        else:
            errors.append(t_path)

with open(f"{output_path}/raw_filelist.txt", "w") as f:
    for line in results:
        f.write(line + "\n")

with open(f"{output_path}/raw_filelist_errors.txt", "w") as f:
    for line in errors:
        f.write(line + "\n")
        
