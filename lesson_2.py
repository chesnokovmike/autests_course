def task_1(length):
    per = length * 4
    square = length ** 2
    diagonal = (length ** 2 + length ** 2) ** 0.5
    return per, square, diagonal


def task_2(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x_1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
    x_2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
    return x_1, x_2


def task_3(str1, str2):
    union = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    return union


def task_4(file):
    disk = file[0]
    root = file[file.index('/', 2) + 1:file.index('/', 3)]
    file_name = file[file.rfind('/') + 1:file.rfind('.')]
    return disk, root, file_name


def task_5(num_1, num_2):
    amount = num_1 + num_2
    prod = num_1 * num_2
    return f'{num_1} + {num_2} = {amount}\n{num_1} * {num_2} = {prod}'


def task_6(text):
    return text[::2]


def task_7(search, text_str):
    sym_1_index = text_str.index(search[0])
    sym_2_index = text_str.index(search[1])
    sym_3_index = text_str.index(search[2])
    min_index = min(sym_1_index, sym_2_index, sym_3_index)
    max_index = max(sym_1_index, sym_2_index, sym_3_index)
    new_slice = text_str[min_index:max_index + 1]
    return new_slice
