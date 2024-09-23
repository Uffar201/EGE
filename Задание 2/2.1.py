print('x y z w')
for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(x) or y or z) == (not(y) and z and w)
                if F == 1:
                    print(x,y,z,w)
print('Ответ: y w z x')