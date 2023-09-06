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
    jeu1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=nom_joueur1))
    if jeu1 != 'pierre'and jeu1 !='papier'and jeu1 !='ciseaux'and jeu1 !='puit':
                choix_1_vrai = False
                print("Je n'ai pas compris votre réponse")
                while choix_1_vrai == False :
                    print("Joueur ", nom_joueur1)
                    jeu1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                    choix_1_vrai = True
                    if jeu1 != 'pierre'and jeu1 !='papier'and jeu1 !='ciseaux'and jeu1 !='puit': 
                                choix_1_vrai = False

    if nom_joueur2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        jeu2 = ['papier','pierre','ciseaux','puit'][random.randint(0, 3)]

    
    if nom_joueur2 != 'Machine':
        print("Joueur", nom_joueur2)
        jeu2 = input("faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
        if jeu2 != 'pierre'and jeu2!= 'papier'and jeu2!='ciseaux'and jeu2!='puit':
                    choix_2_bon = False
                    print("Je n'ai pas compris votre réponse")
                    while not choix_2_bon :
                        print("Joueur ", nom_joueur2)
                        jeu2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                        choix_2_bon = True
                        if jeu2 != 'pierre'and jeu2 !='papier'and jeu2 !='ciseaux'and jeu2 !='puit': 
                                    choix_2_bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom_joueur1, jeu1, "et", nom_joueur2, jeu2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if jeu1 == 'papier' and jeu2 == 'papier' :
        gagnant = "aucun de vous, vous être ex æquo"
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and jeu2 == 'papier' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and jeu2 == 'pierre' :
        gagnant = "aucun de vous, vous être ex æquo"
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and jeu2 == 'ciseaux' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'papier' and jeu2 == 'ciseaux' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'papier' and jeu2 == 'pierre' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and jeu2 == 'pierre' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and jeu2 == 'ciseaux' :
        gagnant = "aucun de vous, vous être ex æquo"
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and jeu2 == 'papier' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and jeu2 == 'papier' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")
        
    if jeu1 == 'puit' and jeu2 == 'pierre' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'puit' and jeu2 == 'ciseaux' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'puit' and jeu2 == 'papier' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'ciseaux' and jeu2 == 'puit' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'pierre' and jeu2 == 'puit' :
        gagnant = nom_joueur2
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'papier' and jeu2 == 'puit' :
        gagnant = nom_joueur1
        joueur1 = joueur1 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom_joueur1, joueur1, "et", nom_joueur2, joueur2, "\n")

    if jeu1 == 'puit' and jeu2 == 'puit' :
        gagnant = "aucun de vous, vous être ex æquo"
        print("le gagnant est",gagnant)
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