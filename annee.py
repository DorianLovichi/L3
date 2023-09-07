
def est_bissextile(x:int) -> bool :

    return(x%4 ==0 and not x%100==0) or x%400 ==0
    

boucle = [2021,2024,2026]
for i in boucle:
    resultat = est_bissextile(i)
    print("cette année est bixtetile : " +str(resultat))