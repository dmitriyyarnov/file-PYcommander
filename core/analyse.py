from pathlib import Path


def get_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    elif path.is_dir():
        return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
    return 0


def format_size(size_bytes):
    units = ['b', 'kb', 'mb', 'gb', 'tb']
    size = float(size_bytes)
    for unit in units:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}tb"


def analyse_directory(path="."):
    base = Path(path)
    if not base.exists():
        print(f"Путь '{path}' не существует.")
        return

    total_size = get_size(base)
    print(f"> full size: {format_size(total_size)}")

    for item in sorted(base.iterdir()):
        item_size = get_size(item)
        name = item.name.ljust(20)
        print(f"> - {name} {format_size(item_size)}")
