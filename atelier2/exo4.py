import matplotlib.pyplot as plt

def histo (F:list) -> list :
    compte = [0]*(max(F)+1)
    for i in range (len(F)) :
        compte[F[i]] += 1
    return compte

myList = [1,5,5,5,9,11,11,15,15,15]



'''def histo (F:list) -> list :
    compte = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(F)) :
        compte[F[i]] += 1
    return compte

liste = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6]
print(histo(liste))'''

def est_injective(F:list) -> bool:
   H=histo(F)  
   for i in H :
       if i>1 :
           return False
   return True


def est_surjective(F:list) -> bool:
   H=histo(F)  
   for i in H :
       if i<1 :
           return False
   return True
print(est_surjective(myList))

def est_bijective(F:list) -> bool:
    return est_injective(F) and est_surjective(F)

def affichage_histo(F:list):
    plt.hist(F, bins=range(max(F)+2))
    plt.title("Histogramme")
    plt.show()

affichage_histo(myList)