# Рассматриваются целые числа, принадлежащих числовому отрезку [631632; 684934],
# которые представляют собой произведение двух различных простых делителей.
# Найдите такое из этих чисел, у которого два простых делителя больше всего отличаются друг от друга.
# В ответе запишите простые делители этого числа в порядке возрастания. Если подходящих чисел несколько,
# запишите в ответе делители наименьшего из них.


# 2 342467

# Функция для проверки, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция для нахождения простых делителей числа
def prime_factors(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
        if len(factors) > 2:
            return []
    if len(factors) == 1 and is_prime(n // factors[0]) and (n // factors[0]) != factors[0]:
        factors.append(n // factors[0])
    return factors if len(factors) == 2 else []


max_difference = 0
result_factors = []


for number in range(631632, 684935):
    factors = prime_factors(number)
    if factors:
        difference = abs(factors[1] - factors[0])
        if difference > max_difference:
            max_difference = difference
            result_factors = factors
        elif difference == max_difference and factors < result_factors:
            result_factors = factors

# Вывод результата
print(sorted(result_factors))