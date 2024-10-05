# Задача 27695
# Текстовый файл состоит не более чем из 10
# 6 символов L, D и R. Определите максимальное количество идущих подряд
# символов, среди которых каждые два соседних различны.

s = open('24.5.txt').readline()
#s = 'LDRLD'
count = 1
maxi = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi,count)
    else:
        count =1
print(maxi)