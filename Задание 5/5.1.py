
for n in range(105,1000):
    b = str
    q = bin(n)
    b = q[2:]
    b = str(b)
    for i in range(3):
        if b.count('1') == b.count('0'):
            b += b[-1]
        elif b.count('0') > b.count('1'):
            b += '1'
        elif b.count('0') < b.count('1'):
            b += '0'

    R = int(b,2)
    
    if R % 4 == 0:
        print(n)
        break
