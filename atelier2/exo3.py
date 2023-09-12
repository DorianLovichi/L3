def separer(lst:list) -> list :
    number_neg = []
    number_pos = []
    number_null =[]
    for i in range(len(lst)):
        if lst[i]<0 : 
            number_neg.append(lst[i])
        elif lst[i]==0 : 
            number_null.append(lst[i])
        elif lst[i]>0 : 
            number_pos.append(lst[i])
    LSEP = number_neg+number_null+number_pos
    print(LSEP)

L = [1,-2,3,-4,0,6,-7,8,9]
LSEP = []
entier = 4
print(separer(L))