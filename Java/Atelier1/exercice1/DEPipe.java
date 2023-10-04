package Java.Atelier1.exercice1;

public class DEPipe extends De {
    protected final int MIN;

    
    public DEPipe(String nom, int nbFace, int MIN){
        super(nom,nbFace);
        this.MIN = MIN;
    }
    public int getMIN() {
        return MIN;
    }
    public int lancer(){
        super.lancer();
        return r.nextInt(nbFace-MIN+1)+MIN;
    }
}
