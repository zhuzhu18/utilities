import tarfile
import os

path = '/media/tl/213/data/GaitDatasetB-silh'
dest_dir = '/media/tl/213/data/CASIA-B'

for file in os.listdir(path):
    with tarfile.open(os.path.join(path, file), 'r:gz') as tar:
        tar.extractall(path=dest_dir)
