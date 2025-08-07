import os
from pathlib import Path
from datetime import datetime


def get_creation_date(file_path: Path) -> str:
    timestamp = os.path.getctime(file_path)
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
def add_creation_date(path, recursive=False):
    # Пример простого вывода для проверки
    print(f"Добавляем дату создания в файлы по пути: {path} (recursive={recursive})")
    # Реальная логика добавления даты должна быть тут


def rename_with_date(file_path: Path):
    if not file_path.is_file():
        return
    date_str = get_creation_date(file_path)
    parent = file_path.parent
    stem = file_path.stem
    suffix = file_path.suffix
    new_name = f"{stem}_{date_str}{suffix}"
    new_path = parent / new_name
    file_path.rename(new_path)
    print(f"Переименован: {file_path.name} → {new_name}")


def add_date(path: str, recursive: bool = False):
    p = Path(path)
    if not p.exists():
        print(f"Путь '{path}' не существует.")
        return

    if p.is_file():
        rename_with_date(p)
    elif p.is_dir():
        files = p.rglob('*') if recursive else p.glob('*')
        for f in files:
            if f.is_file():
                rename_with_date(f)
