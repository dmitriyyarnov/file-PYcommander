### FileSystem Manager
#### FileSystem Manager — это CLI-инструмент для удобной работы с файлами и папками. Позволяет копировать, удалять, считать, искать файлы, добавлять дату создания в название и анализировать размеры файлов в директории.

##### Установка и запуск
Склонируйте репозиторий или скачайте файлы программы.

В командной строке перейдите в папку с программой.

Запустите инструмент командой:
python main.py <команда> [аргументы]

##### Использование
usage: main.py [-h] {copy,delete,count,search,add_date,analyse} ...

##### Команды
copy — Копировать файл

delete — Удалить файл или папку

count — Подсчитать количество файлов (включая вложенные)

search — Поиск файлов по шаблону (включая вложенные)

add_date — Добавить дату создания в название файла

analyse — Анализ размеров файлов в текущей директории

##### Опции
-h, --help — Показать справку по команде

##### Примеры использования
python main.py copy file.txt backup/file.txt
python main.py delete folder/
python main.py count ./folder
python main.py search . --pattern ".*.txt"
python main.py add_date folder/ --recursive
python main.py analyse

##### Запуск тестов
Для запуска тестов используйте команды:
python -m unittest tests/test_interface.py -v
python -m unittest discover -s tests





