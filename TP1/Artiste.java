import java.util.List;

public class Artiste {
    private String nom;
    private List<TitreMusical> titres;
    private List<Album> albums;

    public Artiste(String nom, List<TitreMusical> titres, List<Album> albums) {
        this.nom = nom;
        this.titres = titres;
        this.albums = albums;
    }
    public String getNom() {
        return nom;
    }
    public void setNom(String nom) {
        this.nom = nom;
    }
    public List<TitreMusical> getTitres() {
        return titres;
    }
    public void setTitres(List<TitreMusical> titres) {
        this.titres = titres;
    }
    public List<Album> getAlbums() {
        return albums;
    }
    public void setAlbums(List<Album> albums) {
        this.albums = albums;
    }

    public void ajoutTitre(TitreMusical titre){
        Spotizer.getTitres().add(0, titre);
    }
    
}
