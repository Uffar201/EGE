# Задача 28120
# Напишите программу, которая ищет среди целых чисел,
# принадлежащих числовому отрезку [201455; 201470], числа, имеющие ровно 4 различных натуральных делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.

count = 0
deli = []
results = []
for i in range(201455,201471):
    for q in range(1,i):
        if i % q == 0:
            deli.append(q)
        if len(deli) == 4:
            results.append(deli)
a = None
for j in range(len(results)):
    a = set(results[j])
print(sorted(a))