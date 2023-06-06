# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path


goods_list = []
tmp_goods = 0
task3_file_path = Path('test_file/task_3.txt')

with open(task3_file_path, 'r', encoding='utf-8') as file:
    for goods in file.readlines():
        if str(goods) == '\n':
            goods_list.append(tmp_goods)
            tmp_goods = 0
        else:
            tmp_goods += int(goods)

goods_list.sort(reverse=True)
three_most_expensive_purchases = goods_list[0] + goods_list[1] + goods_list[2]

assert three_most_expensive_purchases == 202346
