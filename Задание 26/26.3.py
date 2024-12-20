# Тип 26 33771

# Предприятие производит оптовую закупку некоторых изделий A и B, на которую выделена определённая сумма денег.
# У поставщика есть в наличии партии этих изделий различных модификаций по различной цене.
# На выделенные деньги необходимо приобрести как можно больше изделий B независимо от модификации.
# Если у поставщика закончатся изделия B, то на оставшиеся деньги необходимо приобрести как можно больше изделий A.
# Известны выделенная для закупки сумма, а также количество и цена различных модификаций данных изделий у поставщика.
# Необходимо определить, сколько будет закуплено изделий A и какая сумма останется неиспользованной.
# Входные данные.
# Первая строка входного файла содержит два целых числа: N — общее количество партий изделий у поставщика
# и M — сумма выделенных на закупку денег (в рублях).
# Каждая из следующих N строк описывает одну партию и содержит два целых числа
# (цена одного изделия в рублях и количество изделий в партии) и один символ (латинская буква A или B),
# определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом.

# В ответе запишите два целых числа: сначала количество закупленных изделий типа A, затем оставшуюся неиспользованной сумму денег.

# Пример входного файла:
# 4 1000
# 30 8 A
# 50 12 B
# 40 14 A
# 20 10 B
# В данном случае сначала нужно купить изделия B: 10 изделий по 20 рублей и 12 изделий по 50 рублей.
# На это будет потрачено 800 рублей. На оставшиеся 200 рублей можно купить 6 изделий A по 30 рублей.
# Таким образом, всего будет куплено 6 изделий A и останется 20 рублей. В ответе надо записать числа 6 и 20.

f = open('26.3.txt')

# lines = f.readlines()
# ar = []
# for i in range(len(lines)):
#     ar.append(lines[i].strip().split(' '))

ar = [[4, 1000], [30, 8, 'A'], [50, 12, 'B'], [40, 14, 'A'], [20, 10, 'B']]
ar_b = []
ar_bp = []
ar_a = []
ar_ap = []
# Получил список из B
for q in range(1,len(ar)):
    if ar[q][2] == 'B':
        B = [ar[q][0], ar[q][1],q]
        ar_b.append(B)
        ar_bp.append([ar[q][0]* ar[q][1],q]) # список произведений B
    else:
        A = [ar[q][0], ar[q][1], q]
        ar_a.append(A)
        ar_ap.append([ar[q][0] * ar[q][1],q])  # список произведений A
ar_bp = sorted(ar_bp) # отсортировал
ar_ap = sorted(ar_ap)

# Бюджет после B
bud = ar[0][1]
cur_bud = 0
for g in range(len(ar_b)):
    if cur_bud < bud:
        cur_bud += ar_bp[g][0]
bud = bud - cur_bud
cur_bud = 0

for b in range(len(ar_a)):
    if cur_bud < bud:
        cur_bud += ar_ap[b][0]
    else:
        print(ar_b)
        print(ar_bp)
        if ar_b[b][2] == ar_bp[1]:
            print(ar_b[b])