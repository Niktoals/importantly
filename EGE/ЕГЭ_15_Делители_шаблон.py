def Function(x, y, a):
    return ((x < 6)<= (x**2<a)) and ((y**2<=a)<=(y<=6)) # Сюда пишем выражение)

count=0
for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if not (Function(x, y, a)):
                fl = False
                break
        if fl == False:
            break
    if fl:
        count+=1
          # Убрать 'break' для подсчета максимального числа
print(count)

'''def Function(x, a):
    return  # Сюда пишем выражение)


for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if not (Function()):
            fl = False
            break
    if fl:
        print(a)
        break  # Убрать 'break' для подсчета максимального числа'''
