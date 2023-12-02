import copy

def op_3(matrix):
    res=(matrix[0][0]*matrix[1][1]*matrix[2][2])+(matrix[0][1]*matrix[1][2]*matrix[2][0])+(matrix[0][2]*matrix[1][0]*matrix[2][1])-(matrix[0][1]*matrix[1][0]*matrix[2][2])-(matrix[0][0]*matrix[1][2]*matrix[2][1])-(matrix[0][2]*matrix[1][1]*matrix[2][0])                                           
    return res
def change(m1, m2, n):
    c=0
    for i in m1:
        i[n]=m2[0][c]
        c+=1
    return m1

#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A=[]
B=[]
for i in range(3):
    inp=input(f"[[a{i+1}1, a{i+1}2, a{i+1}3]\n").split()
    s=list(map(lambda d: int(d), inp))
    A.append(s)
B.append(list(map(lambda d: int(d), input("[[b1, b2, b3]] \n").split())))
op_a=op_3(A)
new_matrix=[]
if op_a==0:
    list_answers=[0 for x in range(3)]
else:
    list_answers=[]
    for i in range(3):
        a=copy.deepcopy(A)
        new_matrix=change(a, B, i)
        list_answers.append(op_3(new_matrix)/op_a)
        
print(f"Ответ: {list_answers}")

