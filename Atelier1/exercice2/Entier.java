package Java.Atelier1.exercice2;

public class Entier {
    protected int valeur=0;
    protected int MIN;
    protected int MAX;

    public int getValeur(){
        return valeur;
    }
    public void setValeur(int valeur){
        this.valeur= valeur;

    }
    public Entier(int valeur, int MIN, int MAX){
        this.valeur = valeur;
        this.MIN = MIN;
        this.MAX = MAX;
    }
    public int incremente(){
        if ((valeur+1) >= MIN && (valeur+1) <= MAX){
            valeur++;
            
        }
        return valeur;
        
    }
    public int incremente(int n){
        if ((valeur+1) >= MIN && (valeur+1) <= MAX){
            valeur+=n;
        }
        return valeur;
    }
}
