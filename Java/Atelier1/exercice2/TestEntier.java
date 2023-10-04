package Java.Atelier1.exercice2;

public class TestEntier {
  public static void main(String[] args) {
    Entier e1 = new Entier(10, 0, 20);
    Entier e2 = new EntierFou(10, 0, 100, 50);
    Entier e3 = new Entier(11,0,20);
    System.out.println(e2);
    e2.incremente();
    System.out.println(e1.equals(e3));
    System.out.println(e2);
    
  }
}
