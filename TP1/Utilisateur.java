import java.util.List;

public class Utilisateur {
    private String nom;
    private double solde;
    private List<TitreMusical> titresEcoutes;
    private List<Playlist> playlists;

    public Utilisateur(String nom, double solde, List<Playlist> playlists) {
        this.nom = nom;
        this.solde = solde;
        this.playlists = playlists;
    }

    public String getNom() {
        return nom;
    }

    public double getSolde() {
        return solde;
    }

    public List<Playlist> getPlaylists() {
        return playlists;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setSolde(double solde) {
        this.solde = solde;
    }


    public void setPlaylists(List<Playlist> playlists) {
        this.playlists = playlists;
    }
    public void ecoute(TitreMusical titre){
        System.out.println("L'utilisateur "+this.nom+" écoute "+titre.getNom() );
    }
    
}
