import os

def analyse_directory(path="."):
    sizes = {}
    for root, _, files in os.walk(path):
        for f in files:
            sizes[os.path.join(root, f)] = os.path.getsize(os.path.join(root, f))
    return sizes