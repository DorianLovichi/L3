package Java.Atelier0.exercice2;

public class Vecteur3D {
    private int x;
    private int y;
    private int z;


    public Vecteur3D(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public Vecteur3D(){
        x = 0;
        y = 0;
        z = 0;
    }
    public void affichage(){
        System.out.println("<"+x+", "+y+", "+z+">");
    }
    public void norme(){

    }


}
