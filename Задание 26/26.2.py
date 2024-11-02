#5. Тип 26 № 27887
# Системный администратор раз в неделю создаёт архив пользовательских файлов.
# Однако объём диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов.
# Известно, какой объём занимает файл каждого
# пользователя.
# По заданной информации об объёме файлов пользователей и свободном объёме на архивном диске
# определите максимальное число пользователей, чьи файлы можно сохранить в архиве,
# а также максимальный размер имеющегося файла, который может быть сохранён в архиве,
# при условии, что сохранены файлы максимально возможного числа пользователей.
# Входные данные.
# Задание 26
# В первой строке входного файла находятся два числа: S — размер свободного места на диске (натуральное число,
# не превышающее 10 000) и N — количество пользователей (натуральное число, не превышающее 2000). В следующих
# N строках находятся значения объёмов файлов каждого пользователя (все числа натуральные, не превышающие 100),
# каждое в отдельной строке.
# Запишите в ответе два числа: сначала наибольшее число пользователей, чьи файлы могут быть помещены в архив,
# затем максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что сохранены
# файлы максимально возможного числа пользователей.
# Пример входного файла:
# 100 4
# 80
# 30
# 50
# 40
# При таких исходных данных можно сохранить файлы максимум двух пользователей. Возможные объёмы этих двух
# файлов — 30 и 40, 30 и 50 или 40 и 50. Наибольший объём файла из перечисленных пар — 50,
# поэтому ответ для приведённого примера:
# 2 50



f = open('26.2.txt')

storage = int(f.readline().split(' ')[0])


array_of_files = []

files = sorted([int(v) for v in f.readlines()])

for file in files:
    if sum(array_of_files) < storage:
        array_of_files.append(file)


excluded_elements = [array_of_files[-1], array_of_files[-2]]

max_available_size = storage - (sum(array_of_files) - sum(excluded_elements))

max_available_length = len(array_of_files) - 1

max_file_size = -1

for f in files[::-1]:
    if f <= max_available_size:
        max_file_size = f
        break

print(max_available_length)
print(max_file_size)
