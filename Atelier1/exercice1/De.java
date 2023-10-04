package Java.Atelier1.exercice1;
import java.util.*;

public class De {
    protected String nom;
    protected int nbFace;
    protected static Random r = new Random();
    static int i =0;

    public int getNbFace() {
        return nbFace;
    }
    public String getNom(){
        return nom;
    }
    public void setNbFace(int nbFace) {
        if (nbFace >= 3 && nbFace <= 120) {
            this.nbFace = nbFace;
        } else {
            System.err.println("Erreur : Le nombre de faces doit être compris entre 3 et 120.");
        }
    
    }

    
    public De(String nom,int nbFace){
        this.nom = nom+i;
        this.nbFace = nbFace;
        i++;
    }
    public De(){
        nbFace = 6;
        nom = "Dé"+i;
    }
    public De(int nbFace){
        this("Dé",nbFace);
    }
    public De(String nom){
        this(nom, 6);
    }

    public int lancer(){
        int nbAleatoire= r.nextInt(nbFace)+1;
        
        return nbAleatoire ;
    }
    public int lancer(int nbLancer){
        int resultat = 0;
        int meilleurLancer = 0;
        for (int i=0; i<= nbLancer; i++){
          resultat = lancer();
          System.out.println("Lancer #" + (i + 1) + ": " + resultat);
          if (resultat>meilleurLancer){
            meilleurLancer = resultat;
          }
        }
        System.out.println("Le meilleur lancer est : "+meilleurLancer);
        return meilleurLancer;
    }


    public boolean equals(Object o){
        boolean result = false;
        if ((o!=null)&&(o instanceof De)){
            De d = (De)o;
            result = ((this.nbFace == d.nbFace)&&(this.nom.equals(d.nom)));

        }
        return result;
    }
    }


