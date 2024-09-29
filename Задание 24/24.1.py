# Задача 58326
# Текстовый файл состоит не более чем из 106 символов арабских цифр (0,1, ... 9).
# Определите максимальное количество идущих подряд цифр, расположенных в строгом убывающем порядке.

s = open('24.1.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        count += 1
        maxi = max(count,maxi)
    else:
        count = 1
print(maxi)