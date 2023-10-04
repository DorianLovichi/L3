package Java.Atelier1.exercice1;

public class DEMemoire extends De {
    protected int valeurActuelle;


    public DEMemoire(String nom,int nbFace){
        valeurActuelle = -1;
    }
    public int lancer(){
       int nouvelleValeur;
        do {
            nouvelleValeur = r.nextInt(nbFace) + 1; // Générer une valeur aléatoire entre 1 et 6 inclus
        } while (nouvelleValeur == valeurActuelle); // Répéter jusqu'à obtenir une valeur différente

        valeurActuelle = nouvelleValeur;
        return valeurActuelle;
    }
}
