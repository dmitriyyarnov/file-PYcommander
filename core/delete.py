import shutil
from pathlib import Path

def delete_path(path):
    path_obj = Path(path)
    try:
        if path_obj.is_dir():
            shutil.rmtree(path_obj)
            print(f"Папка '{path}' удалена.")
        elif path_obj.is_file():
            path_obj.unlink()
            print(f"Файл '{path}' удалён.")
        else:
            print(f"Путь '{path}' не найден.")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
