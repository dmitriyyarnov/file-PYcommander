import flet as ft
import traceback
import shlex

from feature.copy import copy_file
from feature.delete import delete_path
from feature.count import count_files
from feature.search import search_files
from feature.add_date import add_creation_date
from feature.analyse import analyse_directory


def main(page: ft.Page):
    page.title = "FS-CLI GUI"
    page.window_width = 700
    page.window_height = 500

    commands = ["copy", "delete", "count", "search", "add_date", "analyse"]
    selected_command = ft.Dropdown(
        label="Выберите команду",
        options=[ft.dropdown.Option(cmd) for cmd in commands],
        tooltip="Выберите инструмент для работы с файлами",
        expand=True,
    )

    args_input = ft.TextField(
        label="Аргументы",
        tooltip="Введите параметры (пути к файлам/папкам, опции)",
        expand=True,
    )

    output_box = ft.TextField(
        label="Результат",
        multiline=True,
        read_only=True,
        expand=True,
        min_lines=10,
        tooltip="Здесь будет показан результат выполнения команды",
    )

    def handle_file_result(e):
        new_args = []
        if e.files:
            for f in e.files:
                path = f.path
                if " " in path:
                    path = f'"{path}"'
                new_args.append(path)
        elif e.path:
            path = e.path
            if " " in path:
                path = f'"{path}"'
            new_args.append(path)

        if args_input.value:
            args_input.value += " " + " ".join(new_args)
        else:
            args_input.value = " ".join(new_args)

        args_input.update()

    file_picker = ft.FilePicker(on_result=handle_file_result)
    page.overlay.append(file_picker)

    pick_file_button = ft.ElevatedButton(
        "Выбрать файл", on_click=lambda _: file_picker.pick_files(allow_multiple=True)
    )

    pick_folder_button = ft.ElevatedButton(
        "Выбрать папку", on_click=lambda _: file_picker.get_directory_path()
    )

    def run_command_gui_logic(cmd, args_list):
        try:
            if cmd == "copy":
                if len(args_list) != 2:
                    return "Ошибка: команда copy требует два аргумента: src dst"
                copy_file(args_list[0], args_list[1])
                return "Файлы скопированы успешно."
            elif cmd == "delete":
                if len(args_list) != 1:
                    return "Ошибка: команда delete требует один аргумент: target"
                delete_path(args_list[0])
                return "Удаление выполнено."
            elif cmd == "count":
                if len(args_list) != 1:
                    return "Ошибка: команда count требует один аргумент: path"
                return f"Количество файлов: {count_files(args_list[0])}"
            elif cmd == "search":
                if "--pattern" not in args_list or len(args_list) < 2:
                    return "Ошибка: команда search требует аргументы path и --pattern PATTERN"
                path_index = 0
                pattern_index = args_list.index("--pattern") + 1
                if pattern_index >= len(args_list):
                    return "Ошибка: не указан PATTERN для search"
                return f"Найдено файлов: {search_files(args_list[path_index], args_list[pattern_index])}"
            elif cmd == "add_date":
                if len(args_list) < 1:
                    return "Ошибка: команда add_date требует аргумент path"
                path = args_list[0]
                recursive = "--recursive" in args_list
                add_creation_date(path, recursive)
                return "Дата добавлена."
            elif cmd == "analyse":
                return analyse_directory()
            else:
                return "Неизвестная команда."
        except Exception as e:
            return f"Ошибка: {e}"

    def run_command_gui(e):
        cmd = selected_command.value
        if not cmd:
            output_box.value = "Сначала выберите команду!"
            page.update()
            return

        try:
            try:
                args_list = shlex.split(args_input.value)
            except ValueError:
                args_list = args_input.value.split()

            result = run_command_gui_logic(cmd, args_list)
            output_box.value = result
        except Exception:
            output_box.value = "Ошибка:\n" + traceback.format_exc()
        page.update()

    run_button = ft.ElevatedButton("Запустить", on_click=run_command_gui)

    page.add(
        ft.Text("FS-CLI — графический интерфейс", size=20, weight="bold"),
        selected_command,
        args_input,
        ft.Row([pick_file_button, pick_folder_button]),
        run_button,
        output_box,
    )


if __name__ == "__main__":
    ft.app(target=main)




