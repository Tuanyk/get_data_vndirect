import os
import tarfile
import pathlib
current_path = str(pathlib.Path(__file__).parent.parent.absolute())

def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))

tardir(current_path + "/data/vndirect", current_path + "/data/compress.tar.gz")