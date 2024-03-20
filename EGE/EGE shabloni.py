# Номер 2
'''print('x', 'y', 'z', 'w', 'F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                pass
                #Функция (F)
                #Условия через If/else
                print(x, y, z, w, F)'''

"""from itertools import *
def f(a,b,c,d):
    return (a or (not b)) and ((not a) or c) or (d== (a or b))

for a in product([0,1], repeat=7):
    table=[(a[0], a[1],1,a[2]), (1,1,a[3],a[4]),(1,a[5],1,a[6])]
    if len(table) == len(set(table)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p,r))) for r in table] == [0,0,0]:
                print(p)"""

#Номер 4
'''Условие Фано - кодировка каждого символа не является началом кодировки другого символа
    Обратное Фано - кодировка каждого символа не является концом кодировки другого симпвола'''
#Номер 5
'''for n in range(1000):
    r=bin(n)[2::]
    if n%2==0:
        r+='*'
    else:
        r+='*'
    if int(r, 2)>'*':
        print(int(r, 2))
        break'''
#Номер 6
''' '''
#Номер 7
'''Вес одного пикселя(отчеты) * на количество пикселей(отчеты) = вес всего изображения(музыка)
    вес одного пикселя это i(количество цветов=2^i)'''
#Номер 8
'''import itertools
s='01234567'
k=0
not_use=['16', '61', '36', '63', '56', '65', '76', '67', '96', '69']
for i in itertools.product(s, repeat=5): #Длинна вариации
    a=''.join(i)
    if a.count('6')==1 and a[0]!='0' and sum((x in a) for x in not_use)==0:
        k+=1
print(k)'''

'''answer = 0
not_use = ['16', '61', '36', '63', '56', '65', '76', '67']
 
for i1 in '1234567':
   for i2 in '01234567':
       for i3 in '01234567':
           for i4 in '01234567':
               for i5 in '01234567':

                       numb = i1 + i2 + i3 + i4 + i5 
 
                       if numb.count('6') == 1 and sum([int(x in numb) for x in not_use]) == 0:
                           answer += 1
 
print(answer)'''
#Номер 12
'''s=70*'8'
while "2222" in s or "8888" in s:
    if "2222" in s:
        s=s.replace("2222", "88", 1)
    else:
        s=s.replace("8888", "22", 1)
print(s)'''
#Номер 14
'''x=49**7+7**21-7
count6=0
while x:
    if x%7==6:
        count6+=1
    x//=7
print(count6)'''
#Номер 15
'''s1='123x5'
s2='1x233'
for x in range(1, 1000):
    if (int(('123' + str(x) + '5'), 15) + int(('1' + str(x) + '233'), 15))%14==0:
        z=x
        break
print((int(('123' + str(z) + '5'), 15) + int(('1' + str(z) + '233'), 15))//14)'''
# Номер 22
'''arr=[0]
f=open("*")
for s in f.readlines():
    num, time, need = s.split("\t")
    arr.append(0)
    for j in need.split(";"):
        arr[int(num)]= max(arr[i nt(num)], arr[int(j)])
    arr[int(num)]+= int(time)'''
# ХЗ

'''s=open('Py/9.txt')
f=0
for i in s:
    a=sorted(int(x) for x in i.split('\t'))
    print(a)
    n=sum(a)-sum(set(a))
    print(n)
    if (sum(set(a))==sum(a)-n) and n*2>=(sum(set(a))-n)/len(set(a))-1:
        f+=1
print(f)'''

'''import itertools


s='01234567'
not_use = ['16', '61', '36', '63', '56', '65', '76', '67']
k=0
for i in itertools.product(s, repeat=5): #Длинна вариации
    a=''.join(i)  
    if a.count('6')==1 and sum([int(x in a) for x in not_use])==0 and a[0]!=0:
        k+=1
print(k)'''

'''
def main():
    def f(n):
        if n==1:
            return 1
        if n>1:
            return n*f(n-1)

    F(2023) / F(2020) = (2023 * 2022 * 2021 * 2020!) / 2020! = 2023 * 2022 * 2021
if __name__=="__main__":
    main()'''
# Номер 17
'''s=open('Py/17.txt').readlines()
ls=[]
max=int(s[0])
a1=int(s[0])
for i in range(1, len(s)):
    a2=int(s[i])
    if a1>max and abs(a1)%10==3 and a1>0:
        max=a1
    if (abs(a1)%10==3 and abs(a2)%10!=3) or (abs(a1)%10!=3 and abs(a2)%10==3):
        ls.append([a1, a2])
    a1=a2
n=0
max2=0
for i in ls:
    if abs(i[0])**2 + abs(i[1])**2>9973**2:
        n+=1
        if int(i[0])**2 + int(i[1])**2>max2:
            max2=int(i[0])**2 + int(i[1])**2
print(n, max2)'''

'''s=open('Py/17_1994.txt').readlines()
ls=[]
a1=int(s[0])
n=0
for i in range(1, len(s)):
    a2=int(s[i])
    if a1*a2>0 and abs(a1+a2)%7==0:
        n+=1
        ls.append(a1*a2)
    a1=a2
print(n, min(ls))'''

#Номер 11 (Диагностика)
'''n1=round(int('101101', 2)/4)
n2=round(int('246', 8)/8)
print(hex(n1 + n2)[2::])'''

#Проверка простоты
'''def sipmle_digit(n1):
    x=2
    while x!=n1//2:
        if n1%x==0:
            return False
        x+=1'''

#19
'''def f(x, y, m):
    if x+y>=68: return m%2==0
    # x+y>? : return m%2!=0
    if m==0: return 0
    h=[f(x+1, y, m-1), f(x, y+1, m-1), f(x*3, y, m-1), f(x, y*3, m-1)]
    return any(h) if (m-1)%2==0 else all(h) #any

print([s for s in range(1, 62) if not f(s, 6, 2) and f(s, 6, 4)])'''

#tourtle
"""from turtle import *
color("black", "red")
m = 100
begin_fill()
left(90)
for i in range(2):
    forward(8*m)
    right(90)
    forward(18*m)
    right(90)
end_fill()
canvas= getcanvas()
cnt = 0
for y in range(-100*m,100*m, m) :
    for x in range(-100*m, 100*m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item)==1 and item[0]==5:
            cnt += 1
print(cnt)
done()
exit()"""

#19
"""def f(s,m,p1,p2):
    if s >= 21: return m%2==0
    if m == 0: return 0
    h = []
    if p2 != '+1': h.append(f(s+1,m-1,'+1', p1))
    if p2 != '+2': h.append(f(s+2,m-1,'+2', p1))
    if p2 != '*2': h.append(f(s*2,m-1,'*2', p1))
    return any(h) if (m-1) % 2 == 0 else all(h)


print('1)', [s for s in range(1, 21) if not f(s,1,'','') and f(s,3,'','')])
    """
#27
"""# data_test=[[1,3], [5,12], [6,9], [5,4], [3,3], [1,1]]
f=open("27-A_demo.txt")
n=f.readline()
data=[list(map(int, x[:-1:].split('  '))) for x in f.readlines()]
data_r=[]
summ=0
for i in data:
    summ+=max(i)
    data_r.append(abs(i[0]-i[1]))
data_r.sort()
if summ%3==0:
    for i in data_r:
        if (summ-i)%3!=0:
            summ-=i
            break
print(summ)

f=open("C:/Users/toart/Documents/Py/27-B_2.txt")
n=f.readline()
data=[int(x) for x in f.readlines()]
data.sort(reverse=True)
flag=False
print(data)
for i in range(len(data)):
    maxim=data[0]
    for j in data[i+1::]:
        summ=maxim*j
        if summ%14==0:
            flag=True
            break
    if flag==True:
        break
print(summ)
"""