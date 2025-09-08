import argparse
import sys
from feature.copy import copy_file
from feature.delete import delete_path
from feature.count import count_files
from feature.search import search_files
from feature.add_date import add_creation_date
from feature.analyse import analyse_directory


def build_parser():
    parser = argparse.ArgumentParser(description="FS-CLI — инструмент для работы с файлами")
    subparsers = parser.add_subparsers(dest="command", title="Команды")

    parser_copy = subparsers.add_parser("copy", help="Копировать файл")
    parser_copy.add_argument("src")
    parser_copy.add_argument("dst")

    parser_delete = subparsers.add_parser("delete", help="Удалить файл или папку")
    parser_delete.add_argument("target")

    parser_count = subparsers.add_parser("count", help="Подсчитать файлы")
    parser_count.add_argument("path")

    parser_search = subparsers.add_parser("search", help="Найти файлы")
    parser_search.add_argument("path")
    parser_search.add_argument("--pattern", required=True)

    parser_date = subparsers.add_parser("add_date", help="Добавить дату к файлам")
    parser_date.add_argument("path")
    parser_date.add_argument("--recursive", action="store_true")

    subparsers.add_parser("analyse", help="Анализ размеров файлов")

    return parser


def run_command(args=None):
    parser = build_parser()
    if args is None:
        args = sys.argv[1:]
    args = parser.parse_args(args)

    if not args.command:
        parser.print_help()
        return "Не выбрана команда."

    try:
        if args.command == "copy":
            copy_file(args.src, args.dst)
        elif args.command == "delete":
            delete_path(args.target)
        elif args.command == "count":
            return str(count_files(args.path))
        elif args.command == "search":
            return str(search_files(args.path, args.pattern))
        elif args.command == "add_date":
            add_creation_date(args.path, recursive=args.recursive)
        elif args.command == "analyse":
            return str(analyse_directory())
        return f"Команда '{args.command}' выполнена успешно."
    except Exception as e:
        return f"Ошибка: {e}"


def main():
    result = run_command()
    if result:
        print(result)


if __name__ == "__main__":
    main()


