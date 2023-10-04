package Java.Atelier1.exercice1;

public class TestDe {
    public static void main(String[] args) {
        De de1 = new De("de1", 6);
        De de2 = new De("de2");
        De de3 = new De(8);
        DEPipe dePipe1 = new DEPipe("pipe",6,3);
        de1.lancer(3);
        System.out.println("Son nom est : "+de1.getNom()+" il contient : "+de1.getNbFace()+" face(s)");
        System.out.println("Son nom est : "+de2.getNom()+" il contient : "+de2.getNbFace()+" face(s)");
        System.out.println("Son nom est : "+de3.getNom()+" il contient : "+de3.getNbFace()+" face(s)");
        int resultat = dePipe1.lancer();
        System.out.println("Lancer du dé pipé : "+resultat);
        System.out.println("Son nom est : "+dePipe1.getNom()+" il contient : "+dePipe1.getNbFace()+" face(s)"+"sa borne minimale est : "+ dePipe1.getMIN());
        DEMemoire deM = new DEMemoire("mem",6);
        for(int i=0;i<6;i++){
        int resultM = deM.lancer();
        System.out.println("Mémoire : "+resultM);
        
        }
        boolean egale = de2.equals(deM);
        System.out.println(egale);
    }
}
