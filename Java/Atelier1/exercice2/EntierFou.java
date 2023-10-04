package Java.Atelier1.exercice2;


public class EntierFou extends Entier{
    protected int niveauDeFolie;

    public EntierFou(int valeur, int min, int max, int niveauDeFolie){
        super(valeur,min,max);
        this.niveauDeFolie = niveauDeFolie;
    }
    public int incremente(){
    int resultat = super.incremente(r.nextInt(niveauDeFolie));
    return resultat;
        


    }
}
