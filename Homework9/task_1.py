# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# Здесь пишем код
from pathlib import Path


first_task_data_path = Path('test_file/task1_data.txt')
first_task_answer_path = Path('test_file/task1_answer.txt')

first_task_data = open(first_task_data_path, 'r', encoding='utf-8')
with open(first_task_answer_path, 'w', encoding='utf-8') as first_task_answer:
    for one_line in first_task_data.readlines():
        for symbol in one_line:
            if symbol.isdigit():
                symbol = symbol.replace(symbol, '')
            first_task_answer.write(symbol)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
