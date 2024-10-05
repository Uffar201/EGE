# Задача 36879
# В строках, содержащих менее 25 букв G,
# нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
# Пример:
# GIGA
# GABLAB
# NOTEBOOK
# AGAAA
# В этом примере во всех строках меньше 25 букв G.
# Самое большое расстояние между одинаковыми буквами — в третьей строке между буквами O,
# расположенными в строке на 2-й и 7-й позициях.
# В ответе для данного примера нужно вывести число 5.


s = open('24.6.txt').readlines()
#s = ['GIGA','GABLAB','NOTEBOOK','AGAAA']

def usl(a):
    maxi = 0
    if a.count('G') < 25:
        for i in range(len(a) - 1):
            for j in range(i+1,len(a)):
                if a[i] == a[j]:
                    if abs(i - j) > maxi:
                        maxi = abs(j - i)
    return maxi
ma = 0
for q in range(len(s)):
    ma = max(ma, usl(s[q]))
print(ma)