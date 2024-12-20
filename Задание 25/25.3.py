# Тип 25 № 64955
# Маска числа — это последовательность цифр, в которой могут встречаться специальные символы
# «?» и «*». Символ «?» означает ровно одну произвольную цифру,
# символ «*» означает произвольную (в том числе пустую) последовательность цифр.
# Например, маске 123*4?5 соответствуют числа 123405 и 12376415.
# Найдите все натуральные числа, не превышающие 10 ** 10,
# которые соответствуют маске 1*4182?7 и
# при этом без остатка делятся на 1991.
# В ответе запишите все найденные числа в порядке возрастания.

mask = '1 000 4182 0 7'
nu = '0123456789'
R = []
for i in nu:
    for q in ' ' + nu:
        for f in nu:
            for y in nu:
                if q != ' ':
                    star = q + f + y
                else:
                    star = ''
                mask = int('1' + star + '4182' + i + '7')
                if mask % 1991 == 0:
                    R.append(mask)

print(sorted(set(R)))