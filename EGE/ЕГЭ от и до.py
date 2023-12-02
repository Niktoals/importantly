start = 586132
end = 586430
k=2
ls=[]
ls2=[]
ls3=[]
ls4=[]
ls_max_in=[]
for i in range(start, end + 1): 
    deliteli=[1, i]
    k=2
    while k * k <= i:
        if i % k==0:
            deliteli.append(k)
            if i // k < i: 
                deliteli.append(i // k)
        k = k + 1
    ls.append(len(sorted(deliteli)))
    ls2.append(i)
maxim=max(ls)
minim=min(ls)
for j in ls:
    if j==maxim:
        ls_max_in.append(ls.index(j))
        ls.remove(j)
l=0
for i in ls_max_in:
    ls3.append(ls2[i+ls_max_in.index(i)])

for i in ls3: 
    k=2
    deliteli=[1, i]
    while k * k <= i:
        if i % k==0:
            deliteli.append(k)
            if i // k < i: 
                deliteli.append(i // k)
        k = k + 1
    ls4.append(sorted(deliteli))
count=0
answer=[]
for i in ls4:
    if len(i)>2:
        answer.append(len(i))
        for j in range(0, 2):
            f=max(i)
            answer.append(max(i))
            ls4[count].remove(f)
    count+=1
c=0
del answer[3:6:]
for i in range(len(answer)//3):
    print(answer[0], end=' ')
    answer.remove(answer[0])
    x=sorted(answer[:2:])
    x.reverse()
    print(x[0], end=' ')
    print(x[1], end='\n')
    del answer[:2:]


