
def position(lst:list, elt:int) -> int :
    for i in range(len(lst)):
        if lst[i] == elt : 
            return i
        return -1
    
    
def nb_occurences(lst:list, e:int) -> int :
    resultat = 0
    for i in range(len(lst)):
        if lst[i] == e : 
            resultat+=1
    return resultat

def est_triee(lst:list) ->bool :
    for i in range(len(lst)-1) : 
        if lst[i] > lst[i+1] : 
            return False
    return True
     
def position_tri(lst:list, elt:int) -> int :
    indice_min = 0
    indice_max = len(lst)
    milieu_indice = indice_max//2
    for e in lst :
        if elt == lst[milieu_indice] :
            return True
        elif elt> lst[milieu_indice] :
            indice_min = milieu_indice
        else :
            indice_max = milieu_indice
        


myList = [1,2,3,4,5,6,7,8,9]
entier = 4
print(position_tri(myList,entier))