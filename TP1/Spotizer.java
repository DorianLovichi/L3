import java.util.List;

public class Spotizer {
    private List<Artiste> artistes;
    private List<Style> styles;
    private List<Utilisateur> utilisateurs;
    private List<TitreMusical> titres;
    
    public Spotizer(List<Artiste> artistes, List<Style> styles, List<Utilisateur> utilisateurs, List<TitreMusical> titres) {
        this.artistes = artistes;
        this.styles = styles;
        this.utilisateurs = utilisateurs;
        this.titres = titres;
    }

    public List<Artiste> getArtistes() {
        return artistes;
    }

    public void setArtistes(List<Artiste> artistes) {
        this.artistes = artistes;
    }

    public List<Style> getStyles() {
        return styles;
    }

    public void setStyles(List<Style> styles) {
        this.styles = styles;
    }

    public List<Utilisateur> getUtilisateurs() {
        return utilisateurs;
    }

    public void setUtilisateurs(List<Utilisateur> utilisateurs) {
        this.utilisateurs = utilisateurs;
    }

    public List<TitreMusical> getTitres() {
        return titres;
    }

    public void setTitres(List<TitreMusical> titres) {
        this.titres = titres;
    }
    public void facturation()
}
