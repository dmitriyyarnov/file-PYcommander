import os
import shutil

def delete_path(target):
    if os.path.isfile(target):
        os.remove(target)
    elif os.path.isdir(target):
        shutil.rmtree(target)
    else:
        raise FileNotFoundError(f"{target} не существует")
