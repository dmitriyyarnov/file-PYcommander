import os
import re

def search_files(path, pattern):
    regex = re.compile(pattern)
    matches = []
    for root, _, files in os.walk(path):
        for f in files:
            if regex.search(f):
                matches.append(os.path.join(root, f))
    return matches
