from pathlib import Path

def count_files(path):
    path_obj = Path(path)
    if not path_obj.is_dir():
        print(f"'{path}' не является папкой.")
        return 0

    return sum(1 for _ in path_obj.rglob('*') if _.is_file())
