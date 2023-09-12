#1
'''
def somme(L:list) -> int :  
  resultat = 0
  for i in range(len(L)) :
    resultat = resultat+ L[i]
  print(resultat)

somme( L = [4,8,12])



def sommes(L:list) ->list :
    resultat = 0
    for e in L :
        resultat = resultat+e
    print (resultat)

sommes (L = [4,8,12])


def somme(L:list) -> int :  
  resultat = 0
  x = 0
  while x < len(L) :
    resultat = resultat+L[x]
    return resultat
  print(resultat)

somme (L = [4,8,12])

#2

def somme(L:list) ->list :
    resultat = 0
    for e in L :
        resultat = resultat+e


def test_exercice1 ():
    print("TEST SOMME")
#test liste vide
    print("Test liste vide : ", somme([]))
#test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme(lst2test1))
    
test_exercice1()

#3
def moyenne(L:list) -> int:
    resultat = 0
    for i in range(len(L)) :
        resultat = (resultat+L[i])
        print(resultat)
    resultat = resultat/len(L)
    print(resultat)
moyenne (L = [4,8,12])
'''
#4
'''
def nb_sup(L:list,e:int) -> int:
    resultat = 0
    for i in range(len(L))  :
      if L[i] >e:
         resultat+=1
    return resultat
        
def nb_sup2(L:list,e:int) -> int:
    resultat = 0
    for i in L  :
        if i >e:
         resultat+=1
    return resultat



#5
def moy_sup(L:list,e:float) -> float:
    resultat = 0
    nbValSup = nb_sup(L,e)
    if nbValSup>0 :
        for i in range(len(L))  :
            if e <L[i]:
                resultat+=L[i]
        resultat = resultat/nbValSup
        return resultat

print(moy_sup ([4,8,12,14],10))
'''
#6
def val_max(L:list) -> int :
   resultat = L[0]
   for i in range(len(L)) :
        if resultat < L[i] :
            resultat = L[i]
            return resultat
   
print(val_max([1,6,5,2]))
   