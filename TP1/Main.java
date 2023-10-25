public class Main {
    public static void main(String[] args) {
        Utilisateur u1 = new Utilisateur("Nico", 10, null, null);
        TitreMusical t1 = new TitreMusical("java", 150, 180, null, null);
        u1.ecoute(t1);
    }
}
