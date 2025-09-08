import os

def count_files(path):
    count = 0
    for _, _, files in os.walk(path):
        count += len(files)
    return count
