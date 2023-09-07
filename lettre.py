poids = 0
PRIX_VERTE = [1.16, 2.32, 4, 6, 7.50, 10.50, 0.5]


type = input("Entrer un type de lettre : verte, ecopli, prioritaire : ")
if type != 'verte' and type != 'ecopli' and type != 'prioritaire' : 
    print("Entrer un type de lettre valide")
if type =='verte':
    poids = input('entrer un poid : ')
if poids <= '20':    
    print(PRIX_VERTE[0])
if poids <= '100':    
    print(PRIX_VERTE[1])
if poids <= '250':    
    print(PRIX_VERTE[2])
if poids <= '500':    
    print(PRIX_VERTE[3])
if poids <= '1000':    
    print(PRIX_VERTE[4])
if poids <= '30000':    
    print(PRIX_VERTE[5])
    
# Initialisation d'une variable
compteur = 0

# Boucle while
while compteur < 5:
    print("Compteur =", compteur)
    compteur += 1  # Incrémente le compteur à chaque itération

print("Boucle terminée")
