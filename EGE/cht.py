data2=[0,0,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,]

def foo(ls, d, m):
    x,y=ls
    if y-x<3:
        del d[x-m:y-m]
        return y-x
    else:
        return m

check_list=[]
cheker=[]
flag=False
for x in range(len(data2)):

    if data2[x]==0 and len(cheker)==0:
        cheker.append(x)

    if data2[x]!=0 and len(cheker)!=0:
        cheker.append(x)
        check_list.append(cheker)
        cheker=[]
cheker.append(len(data2))
check_list.append(cheker)
c=0
for i in check_list:
    print(c)
    c=foo(i, data2, c)
print(data2)
print(check_list)