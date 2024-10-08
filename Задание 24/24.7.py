# Задача 35482
# Текстовый файл содержит строки различной длины.
# Необходимо найти строку, содержащую наименьшее количество букв G
# (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
# Пример:
# GIGA GABLAB AGAAA
# В этом примере в первой строке две буквы G, во второй и третьей — по одной.
# Берём вторую строку, так как она находится в файле раньше.
# В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, так как она
# позже стоит в алфавите. В ответе для этого примера надо записать B.

s = open('24.7.txt').readlines()
#s = ['GIGA','GABLAB','AGAAA']

mini = 1000000000

def miq(a):
    top = 0
    for j in range(len(a)):
        top = a.count('G')
    return top

for i in range(len(s)):
    mini = min(miq(s[i]),mini) # нашёл минимальное G

elm = str
for q in range(len(s)):
    q1 = s[q].count('G')
    if q1 == mini:
        elm = s[q] # нашёл первую строку с минимальным количеством G
        break

count = 1
miy = 0
char = str
el = ''.join(sorted(elm))

for z in range(len(el) - 1):
    if el[z] == el[z+1]:
        count += 1
        if count >= miy:
            miy = count
            char = el[z]
    else:
        count = 1


print(char)