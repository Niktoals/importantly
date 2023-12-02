'''A=set(range(30, 51))
B=set(range(40, 47))
ls=[]
def f(x):
    return((x not in B) <= (x not in A)) and ((x not in C)<=(x in B))

for N in range(1, 101):
    C=set(range(N, 62))
    count=0
    for x in range(1, 101):
        if f(x):
            count+=1
    if count>25:
        ls.append(N)
print(max(ls))'''
