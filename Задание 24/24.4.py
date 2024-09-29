# Задача 27698
# Текстовый файл состоит не более чем из 10
# 6 символов L, D и R. Определите длину самой длинной последовательности,
# состоящей из символов R. Хотя бы один символ R находится в последовательности.

s = open('24.4.txt').readline()

count = maxi = 0

for i in range(len(s)):
    if s[i] == 'R':
        count += 1
        maxi = max(count, maxi)
    else:
        count = 0
print(maxi)