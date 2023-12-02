import random
def main(rows):
    rows=rows
    seats=[]
    ls_groups=[]
    for i in range(rows):
        seats.append(['...', '...'])
    check='.'
    while check.count('.')!=0:
        check=''
        group=[]
        for i in seats:
            check+=i[0]+i[1]
        group.append(random.choice([1, 2, 3]))
        group.append(random.choice(["left", "right"]))
        group.append(random.choice(["aisle", "window"]))
        free_seats=[]
        new_string=''
        if group[2]=='aisle':
            for f in seats:
                if group[1]=='left' and f[0][-1:-int(group[0])-1:-1].count('.')==int(group[0]):
                    new_string=seats[seats.index(f)][0]  
                    if int(group[0])==3:
                        seats[seats.index(f)][0]='XXX'
                    elif new_string.find('.')==1 and group[0]==1:
                        seats[seats.index(f)][0]='XXX'
                    else:
                        seats[seats.index(f)][0]=new_string[:3-int(group[0]):]+'X'*int(group[0])
                    for h in range(int(group[0])):
                        free_seats.append(str(seats.index(f)+1)+chr(67-h))
                    free_seats.reverse()
                    #print('Passengers can take seats:', *free_seats, end='\n')
                    ls_groups.append([group[0], group[1], group[2]])
                    break
                if group[1]=='right' and f[1][:int(group[0]):].count('.')==int(group[0]):
                    new_string=seats[seats.index(f)][1]
                    if int(group[0])==3:
                        seats[seats.index(f)][1]='XXX'
                    elif new_string.find('.')==1 and group[0]==1:
                        seats[seats.index(f)][1]='XXX'
                    else:
                        new_string=seats[seats.index(f)][1]
                        seats[seats.index(f)][1]='X'*int(group[0])+new_string[-1:int(group[0])-1:-1]
                    for h in range(int(group[0])):
                        free_seats.append(str(seats.index(f)+1)+chr(68+h))
                    #print('Passengers can take seats:', *free_seats, end='\n')
                    ls_groups.append([group[0], group[1], group[2]])
                    break           
        if group[2]=='window':
            for f in seats:
                if group[1]=='left' and f[0][:int(group[0]):].count('.')==int(group[0]):
                    new_string=seats[seats.index(f)][0]
                    if int(group[0])==3:
                        seats[seats.index(f)][0]='XXX'
                    elif new_string.find('.')==1 and group[0]==1:
                        seats[seats.index(f)][0]='XXX'
                    else:
                        seats[seats.index(f)][0]='X'*int(group[0])+new_string[-1:int(group[0])-1:-1]
                    for h in range(int(group[0])):
                        free_seats.append(str(seats.index(f)+1)+chr(65+h))
                    #print('Passengers can take seats:', *free_seats, end='\n')
                    ls_groups.append([group[0], group[1], group[2]])
                    break
                if group[1]=='right' and f[1][-1:-int(group[0])-1:-1].count('.')==int(group[0]):
                    new_string=seats[seats.index(f)][1]
                    if int(group[0])==3:
                        seats[seats.index(f)][1]='XXX'
                    elif new_string.find('.')==1 and group[0]==1:
                        seats[seats.index(f)][1]='XXX'
                    else:
                        seats[seats.index(f)][1]=new_string[:0-int(group[0]):]+'X'*int(group[0])
                    for h in range(int(group[0])):
                        free_seats.append(str(seats.index(f)+1)+chr(70-h))
                    free_seats.reverse()
                    #print('Passengers can take seats:', *free_seats, end='\n')
                    ls_groups.append([group[0], group[1], group[2]])
                    break 
        if len(free_seats)!=0:           
            for k in range(len(seats)):
                #print(*(seats[k][0]+'_'+seats[k][1]), sep='', end='\n')
                seats[k][0]=seats[k][0].replace('X', '#')
                seats[k][1]=seats[k][1].replace('X', '#')
    return len(ls_groups)
    #print(f'Groups can sit: {len(ls_groups)}, all information you can see in file "groups.txt"')
    # f=open('groups.txt', 'w')
    # for i in ls_groups:
    #     f.write(str(i[0])+' '+i[1]+' '+i[2]+'\n')
    # f.close()
if __name__=="__main__":
    rows=int(input())
    avr=[]
    for i in range(100):
        avr.append(main(rows))
    print(sum(avr)//len(avr))