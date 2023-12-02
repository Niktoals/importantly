# Номер 7
'''from itertools import product
count=0
not_use=['16', '61', '36', '63', '56', '65', '76', '67']
for i in product('01234567', repeat=5):
    a=''.join(i)
    if a.count('6')==1 and sum([int(x in a) for x in not_use])==0 and a[0]!='0':
        count+=1
print(count)'''

#Номер 8
'''f=open('Py/9.txt')
count=0
for i in f.readlines():
    a=[int(x) for x in i.split('\t')]
    rep=sum(a)-sum(set(a))
    if len(set(a))==5 and (sum(set(a))-rep)/4<=rep*2:
        print(a)
        count+=1
print(count)'''

# Номер 11
'''alf=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'e']
def f(x):
    n1='123x5'
    n2='1x233'
    n1=n1.replace('x', x)
    n2=n2.replace('x', x)
    return int(n1, 15)+int(n2, 15)

for x in alf:
    if f(x)%14==0:
        print(f(x)//14)
        break'''

#  Номер 12
'''for a in range(1, 100):
    k = 0
    for x in range(1, 1000):
        if ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100):
            k += 1
    if k == 999:
        print(a)
        break'''

# Номер 15 
'''f = open('Py/17.txt').readlines()

k=0
max=0
# for i in f:
#     if int(i)>max and int(i)%10==3:
#         max=int(i)
# print(max) !!!9973!!!

for n in range(1, len(f)):
    if ((abs(int(f[n]))%10==3 and abs(int(f[n-1]))%10!=3) or (abs(int(f[n]))%10!=3 and abs(int(f[n-1]))%10==3)) and int(f[n])**2+int(f[n-1])**2>=9973**2:
        k+=1
        if int(f[n])**2+int(f[n-1])**2>max:
            max=int(f[n])**2+int(f[n-1])**2
print(k, max)'''

'''import pymysql
con=pymysql.connect(host='localhost', user='root', passwd='', database='my basedata')
try:
    # with con.cursor() as cur:
    #     create_table_query = "CREATE TABLE `school`(id int AUTO_INCREMENT, name varchar(32), secondname varchar(32), grade int, PRIMARY KEY(id));"
    #     cur.execute(create_table_query)
    with con.cursor() as cur:
        select_query="SELECT idOrder, idProduct, idCustomer, IdSeller FROM `order` WHERE `date`='2014-09-11'"
        cur.execute(select_query)
        d=dict()
        for i in cur.fetchall():
            d[i[0]]=i[1::]
        x=dict()
        for i in d.items():
            cur.execute(f"SELECT * FROM `customer`, `product`, `seller` WHERE `customer`.`idCustomer`={i[1][1]} and `seller`.`idSeller`={i[1][2]} and `product`.`idProduct`={i[1][0]}")
            x[i[0]]=cur.fetchall()
        
finally:
    for i in x.items():
        print(i)
    con.close()'''