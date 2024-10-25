# Среди целых чисел, принадлежащих числовому отрезку [2031; 14312],
# найдите числа, которые не содержат цифру 2,
# если записать их в системе счисления с основанием 11.
# Ответом будет максимум среди найденных чисел.
# 14312

def to_11(n):
  result = []
  while n > 0:
    digit = n % 11
    if digit == 10:
      digit = 'A'
    result.append(str(digit))
    n //= 11
  return ''.join(result[::-1])  # Соединяем цифры в обратном порядке

def no_two(number_str):
  return not '2' in number_str

max_number = 0
for i in range(2031, 14313):
  number11 = to_11(i)
  if no_two(number11):
    max_number = i

print(max_number)
