import argparse
from core.copy import copy_file
from core.delete import delete_path
from core.count import count_files
from core.search import search_files
from core.add_date import add_date
from core.analyse import analyse_directory

def main():
    parser = argparse.ArgumentParser(
        description="FileSystem Manager — CLI-инструмент для работы с файлами и папками."
    )
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    # copy
    copy_parser = subparsers.add_parser("copy", help="Копировать файл")
    copy_parser.add_argument("src", help="Исходный файл")
    copy_parser.add_argument("dst", help="Путь назначения")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Удалить файл или папку")
    delete_parser.add_argument("path", help="Путь к файлу или папке")

    # count
    count_parser = subparsers.add_parser("count", help="Посчитать количество файлов")
    count_parser.add_argument("path", help="Путь к папке")

    # search
    search_parser = subparsers.add_parser("search", help="Поиск файлов по шаблону")
    search_parser.add_argument("path", help="Путь к папке")
    search_parser.add_argument("--pattern", required=True, help="Регулярное выражение")

    # Команда add_date
    add_date_parser = subparsers.add_parser(
        "add_date", help="Добавить дату создания в имя файла"
    )
    add_date_parser.add_argument("path", help="Файл или папка")
    add_date_parser.add_argument("--recursive", action="store_true", help="Рекурсивно переименовать вложенные файлы")

    # В parser:
    analyse_parser = subparsers.add_parser("analyse", help="Анализ размера содержимого директории")

    args = parser.parse_args()

    if args.command == "copy":
        copy_file(args.src, args.dst)
    elif args.command == "delete":
        delete_path(args.path)
    elif args.command == "count":
        count = count_files(args.path)
        print(f"Файлов найдено: {count}")
    elif args.command == "search":
        matches = search_files(args.path, args.pattern)
        print("Найденные файлы:")
        for m in matches:
            print(m)
    elif args.command == "add_date":
        add_date(args.path, args.recursive)
    elif args.command == "analyse":
        analyse_directory()
    else:
        parser.print_help()
