# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
goods_list = []
tmp_goods = 0
with open('D:\\autotest_course\Homework9\\test_file\\task_3.txt', 'r') as file:
    for goods in file.readlines():
        if str(goods) == '\n':
            goods_list.append(tmp_goods)
            tmp_goods = 0
        else:
            tmp_goods += int(goods)
goods_list.sort(reverse=True)
three_most_expensive_purchases = goods_list[0] + goods_list[1] + goods_list[2]

assert three_most_expensive_purchases == 202346
