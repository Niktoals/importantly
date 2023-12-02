#1
'''for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % a != 0) <= ((x % 6 == 0) <= (x % 3 != 0)):
            k += 1
    if k == 999:
        print(a)
        break'''
#2
'''for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a != 0) and (x % 15 == 0)) <= ((x % 18 != 0) or (x % 15 != 0)):
            k += 1
    if k == 999:
        print(a)
        break'''
#3
'''for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % 18 == 0) <= ((x % 54 == 0) <= (x % a == 0)):
            k += 1
    if k == 999:
        print(a)
        break'''
#4
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % a == 0) <= ((x % a == 0) <= (x % 34 == 0) and (x % 51 == 0)):        !Возможно есть ошибка в условии(ну или я туплю:))
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#5
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a == 0) and (x % 50 != 0)) <= ((x % 18 != 0) or (x % 50 == 0)):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#6
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#7
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a == 0) and (x % 16 == 0)) <= ((x % 16 != 0) or (x % 24 == 0)):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#8
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % 34 == 0) and (x % 51 != 0)) <= ((x % a != 0) or (x % 51 == 0)):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#9
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0)):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
#10
'''ls=[]
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % a == 0) and (x % 15 != 0)) <= ((x % 18 == 0) or (x % 15 == 0)):
            k += 1
    if k == 999:
        ls.append(a)
print(min(ls))'''
