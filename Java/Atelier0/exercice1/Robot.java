package Java.Atelier0.exercice1;

public class Robot {
    private String referenceRobot;
    private String nomRobot;
    private int x;
    private int y;
    static int compteurRobot =1;
    private int orientation;
    public final static int NORD = 1;
    public final static int SUD = 2;
    public final static int EST = 3;
    public final static int OUEST = 4;


    public Robot(String nomRobot, int coordonneeX, int coordonneeY, int orientation) {
        this.nomRobot = nomRobot;
        this.x = coordonneeX;
        this.y = coordonneeY;
        this.orientation = orientation;
        referenceRobot = "Rob"+compteurRobot;
        compteurRobot++;      

}
    public Robot(String nomRobot){
        this.nomRobot = nomRobot;
        referenceRobot = "Rob"+compteurRobot++;
        orientation =NORD;
    }


    public void modificationRobot(int orientation) {
        this.orientation = orientation;
    }
    public void deplacer() {
        if (this.orientation == NORD){
            this.y ++;
        }
        else if (this.orientation == SUD){
            this.y --;
        }
        else if (this.orientation == OUEST){
            this.x --;
        
        }
        else{
            this.x++;
        }
        
    }
    public void affichetToi(){
        System.out.println(nomRobot);
        System.out.println(referenceRobot);
        System.out.println(x);
        System.out.println(y);
        System.out.println(orientation);
    }
    public String toString(){
        return("le nom du robot est : "+nomRobot+"\n\rLa référence du robot est : "
        +referenceRobot+"\n\rSa coordonnées X est : "+x+"\n\rSa coordonnéeY est : "+y+"\n\rSon orientation est : "+orientation);
    }

}

