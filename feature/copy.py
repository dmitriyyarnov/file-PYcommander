import shutil
from pathlib import Path

def copy_file(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)

    if not src_path.is_file():
        print(f"Ошибка: '{src}' не является файлом.")
        return

    try:
        shutil.copy2(src_path, dst_path)
        print(f"Файл '{src}' скопирован в '{dst}'")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")
