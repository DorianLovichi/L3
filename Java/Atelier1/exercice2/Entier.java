package Java.Atelier1.exercice2;
import java.util.*;


public class Entier {
    protected int valeur=0;
    protected int min;
    protected int max;
    protected static Random r = new Random();


    public int getValeur(){
        return valeur;
    }
    public void setValeur(int valeur){
        this.valeur= valeur;

    }
    public Entier(int valeur, int min, int max){
        this.valeur = valeur;
        this.min = min;
        this.max = max;
    }
    public int incremente(){
        if ((valeur+1) >= min && (valeur+1) <= max){
            valeur++;
            
        }
        return valeur;
        
    }
    public int incremente(int n){
        if ((valeur+1) >= min && (valeur+1) <= max){
            valeur+=n;
        }
        return valeur;
    }
     public boolean equals(Object o) {
        boolean resultat =false;
        if ((o != null) && (o instanceof Entier)) {
            Entier e = (Entier) o;
            resultat = (this.valeur == e.valeur) && (this.min == e.min) && (this.max == e.max);
            
        }
        return resultat;
    }
    public String toString(){
        return("La valeur est : "+valeur);
      
    }
}

