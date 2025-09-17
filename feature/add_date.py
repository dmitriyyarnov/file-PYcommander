import os
import datetime

def add_creation_date(path, recursive=False):
    paths = []
    if os.path.isfile(path):
        paths.append(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                paths.append(os.path.join(root, f))
            if not recursive:
                break

    for f in paths:
        dir_name = os.path.dirname(f)
        base, ext = os.path.splitext(os.path.basename(f))
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(f))
        new_name = f"{base}_{ctime.strftime('%Y%m%d')}{ext}"
        os.rename(f, os.path.join(dir_name, new_name))