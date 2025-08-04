import re
from pathlib import Path

def search_files(path, pattern):
    path_obj = Path(path)
    if not path_obj.is_dir():
        print(f"'{path}' не является папкой.")
        return []

    regex = re.compile(pattern)
    matched = [str(p) for p in path_obj.rglob('*') if p.is_file() and regex.search(p.name)]
    return matched
