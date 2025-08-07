import argparse
import sys

from feature.copy import copy_file
from feature.delete import delete_path
from feature.count import count_files
from feature.search import search_files
from feature.analyse import analyse_directory
from feature.add_date import add_creation_date


def main():
    parser = argparse.ArgumentParser(
        description="FileSystem Manager — CLI-инструмент для работы с файлами и папками.",
        epilog="""
Примеры:
  python main.py copy file.txt backup/file.txt
  python main.py delete folder/
  python main.py count ./folder
  python main.py search . --pattern ".*\\.txt"
  python main.py add_date folder/ --recursive
  python main.py analyse
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")

    # copy
    copy_parser = subparsers.add_parser("copy", help="Копировать файл")
    copy_parser.add_argument("src", help="Путь к исходному файлу")
    copy_parser.add_argument("dst", help="Путь для копии")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Удалить файл или папку")
    delete_parser.add_argument("target", help="Файл или папка для удаления")

    # count
    count_parser = subparsers.add_parser("count", help="Подсчитать количество файлов (в том числе вложенные)")
    count_parser.add_argument("path", help="Путь к папке")

    # search
    search_parser = subparsers.add_parser("search", help="Поиск файлов по шаблону (в том числе вложенные)")
    search_parser.add_argument("path", help="Путь к папке")
    search_parser.add_argument("--pattern", required=True, help="Шаблон (регулярное выражение)")

    # add_date
    add_date_parser = subparsers.add_parser("add_date", help="Добавить дату создания в название файла")
    add_date_parser.add_argument("path", help="Файл или папка")
    add_date_parser.add_argument("--recursive", action="store_true", help="Рекурсивно для вложенных папок")

    # analyse
    analyse_parser = subparsers.add_parser("analyse", help="Анализ размеров файлов в текущей директории")

    args = parser.parse_args()  # ← Эта строка ОБЯЗАТЕЛЬНО должна быть

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "copy":
        copy_file(args.src, args.dst)
    elif args.command == "delete":
        delete_path(args.target)
    elif args.command == "count":
        count_files(args.path)
    elif args.command == "search":
        search_files(args.path, args.pattern)
    elif args.command == "add_date":
        add_creation_date(args.path, recursive=args.recursive)
    elif args.command == "analyse":
        analyse_directory()
