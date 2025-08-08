import argparse
import sys
from feature.copy import copy_file
from feature.delete import delete_path
from feature.count import count_files
from feature.search import search_files
from feature.add_date import add_creation_date
from feature.analyse import analyse_directory


def main():
    parser = argparse.ArgumentParser(
        description="FileSystem Manager — CLI-инструмент для работы с файлами и папками."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Команды",
        description="Доступные команды"
    )

    # copy
    parser_copy = subparsers.add_parser("copy", help="Копировать файл")
    parser_copy.add_argument("src", help="Путь к исходному файлу")
    parser_copy.add_argument("dst", help="Путь к новому файлу")

    # delete
    parser_delete = subparsers.add_parser("delete", help="Удалить файл или папку")
    parser_delete.add_argument("target", help="Путь к файлу или папке")

    # count
    parser_count = subparsers.add_parser("count", help="Подсчитать количество файлов")
    parser_count.add_argument("path", help="Путь к папке")

    # search
    parser_search = subparsers.add_parser("search", help="Найти файлы по регулярному выражению")
    parser_search.add_argument("path", help="Путь к папке")
    parser_search.add_argument("--pattern", required=True, help="Регулярное выражение")

    # add_date
    parser_date = subparsers.add_parser("add_date", help="Добавить дату создания в имена файлов")
    parser_date.add_argument("path", help="Путь к файлу или папке")
    parser_date.add_argument("--recursive", action="store_true", help="Рекурсивно для всех вложенных папок")

    # analyse
    subparsers.add_parser("analyse", help="Анализ размера файлов и папок")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    try:
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
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

