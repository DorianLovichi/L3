def racine_unique(a:int,b:int) -> int: 
    x = -b/(2*a)
    return x

a = int(input("entrer a : "))
b = int(input("entrer b : "))
resultat = racine_unique(a,b)
print (resultat)