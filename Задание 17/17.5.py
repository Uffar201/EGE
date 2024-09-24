# Задача 68250
#
#
# Определите количество четвёрок, для которых выполняются следующие условия:
# — в четвёрке есть хотя бы два пятизначных числа и хотя бы одно не пятизначное;
# — в четвёрке больше чисел, кратных 3, чем чисел, кратных 7;
# — сумма элементов четвёрки больше максимального элемента последовательности, запись которого заканчивается на 538,
# но меньше удвоенного значения этого элемента.
# Гарантируется, что в последовательности есть хотя бы один элемент, запись которого заканчивается на 538.
# В ответе запишите два числа: сначала количество найденных четвёрок,
# затем максимальную величину суммы элементов этих четвёрок.


f = open('17.5.txt')
values = [int(v) for v in f]

# 1 условие
def usl(n4):
    count5 = 0
    not5 = 0
    for number in n4:
        if 9999 < number < 100000:
            count5 += 1
        if len(str(number)) != 5:
            not5 += 1
    return (count5 == 2 or count5 == 3) and (not5 == 1 or not5 == 2)

# 2 Условие
def d7(n4):
    count3 = 0
    count7 = 0
    for number in n4:
        if number % 3 == 0:
            count3 += 1
        if number % 7 == 0:
            count7 += 1
    return count3>count7

# наибольшее число
max_el = None
for q in values:
    if q % 1000 == 538:
        if max_el is None or q > max_el:
            max_el = q

# 3 Условие
def max1(n4):
    if (sum(n4) > max_el) and (sum(n4) < 2 * max_el):
        return True
    return False

results = []
for i in range(len(values) - 3):
    cn4 = [values[i], values[i+1], values[i+2], values[i+3]]
    if usl(cn4) and d7(cn4) and max1(cn4):
        n4s = sum(cn4)
        results.append(n4s)

print(len(results), max(results))