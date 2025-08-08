## FileSystem Manager — CLI-инструмент для работы с файлами и папками.
#### В командной строке перейти в папку программы и запустить python main.py

##### usage: main.py [-h] {copy,delete,count,search,add_date,analyse} ...
###### copy                Копировать файл
###### delete              Удалить файл или папку
###### count               Подсчитать количество файлов (в том числе вложенные)
###### search              Поиск файлов по шаблону (в том числе вложенные)
###### add_date            Добавить дату создания в название файла
###### analyse             Анализ размеров файлов в текущей директории

##### options:
  -h, --help

##### Примеры:
######  python main.py copy file.txt backup/file.txt
######  python main.py delete folder/
######  python main.py count ./folder
######  python main.py search . --pattern ".*\.txt"
######  python main.py add_date folder/ --recursive
######  python main.py analyse

##### Запуск тестов
###### python -m unittest tests/test_interface.py -v
###### python -m unittest discover -s tests

