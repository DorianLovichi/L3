import random

intro = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
if intro != 'O':
    if intro != 'N':
        print("Je n'ai pas compris votre réponse")
if intro == 'O':
    nom_joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ",nom_joueur1, " nous allons jouer ensemble \n")
    nom_joueur2 = 'Machine'
joueur1 = 0
nombre_partie = 0
if intro == 'N':
    nom_joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ",nom_joueur1, " nous allons jouer ensemble")
    nom_joueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenue ",nom_joueur2, " nous allons jouer ensemble \n")

jeu = True
joueur2 = 0
while jeu == True:
    nombre_partie += 1 
    jeu1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nom_joueur1))
    if jeu1 != 'pierre'and 'papier'and'ciseaux':
                c1ok = False
                print("Je n'ai pas compris votre réponse")
                while c1ok == False :
                    print("Joueur ", nom_joueur1)
                    jeu1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                    c1ok = True
                    if jeu1 != 'pierre'and 'papier'and'ciseaux': 
                                c1ok = False

    if nom_joueur2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        e2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]

    
    if nom_joueur2 != 'Machine':
        print("Joueur", nom_joueur2)
        e2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if e2 != 'pierre'and 'papier'and'ciseaux':
                    j2bon = False
                    print("Je n'ai pas compris votre réponse")
                    while not j2bon :
                        print("Joueur ", nom_joueur2)
                        e2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                        j2bon = True
                        if e2 != 'pierre'and 'papier'and'ciseaux': 
                                    j2bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom_joueur1, jeu1, "et", nom_joueur2, e2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if jeu1 == 'papier' and e2 == 'papier' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and e2 == 'papier' :
        w12 = nom_joueur2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and e2 == 'pierre' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and e2 == 'ciseaux' :
        w12 = nom_joueur1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'papier' and e2 == 'ciseaux' :
        w12 = nom_joueur2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'papier' and e2 == 'pierre' :
        w12 = nom_joueur1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and e2 == 'pierre' :
        w12 = nom_joueur2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and e2 == 'ciseaux' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and e2 == 'papier' :
        w12 = nom_joueur1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if nombre_partie ==1 or nombre_partie ==2 or nombre_partie==3 or nombre_partie==4:
        jeu = True
    if nombre_partie ==5:
        jeu = False
        
    if nombre_partie ==1 or nombre_partie ==2 or nombre_partie==3 or nombre_partie==4:
        #On propose de c ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom_joueur1,nom_joueur2))
        if go == 'O':
            jeu = True
        if go == 'N':
            jeu = False
        if go != 'O' and go != 'N':
            jeu = True
            print("Vous ne répondez pas à la question, on continue ")
  
        
if jeu == False :
    print("Merci d'avoir joué ! A bientôt")