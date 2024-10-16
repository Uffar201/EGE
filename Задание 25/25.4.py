# Тип 25 № 28123
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [125 256; 125 330], числа,
# имеющие ровно шесть различных чётных натуральных делителей.
# Для каждого найденного числа запишите эти шесть делителей
# в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.

# Например, в диапазоне [2; 48] ровно шесть чётных различных натуральных делителей имеют числа 24, 36 и 40, поэтому
# для этого диапазона вывод на экране должна содержать следующие значения:

# 2 4 6 8 12 24
# 2 4 6 12 18 36
# 2 4 8 10 20 40

results = []
for i in range(125256, 125331):
    deli = [i]
    for q in range(1, i):
        if i % q == 0 and q % 2 == 0:
            deli.append(q)
    if len(set(deli)) == 6:
        results.append(sorted(set(deli)))
print(results)