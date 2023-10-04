package Java.Atelier0.exercice1;

public class TestRobot {
      public static void main(String[] args) {
        Robot r1 = new Robot("toto", 10, 20, Robot.SUD);
        Robot r2 = new Robot("titi", 0, 0, Robot.NORD);
        Robot r3 = new Robot("tata", 0, 0, Robot.NORD);

        r1.affichetToi();
        r1.modificationRobot(Robot.EST);
        r1.deplacer();
        r1.affichetToi();
        r2.affichetToi();
        System.out.println(r1);
        System.out.println(r3);


    }
}
  