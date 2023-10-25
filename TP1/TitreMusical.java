public class TitreMusical {
    private String nom;
    private int duree;
    private int tempo;
    private Album album;
    private Style style;
    
    public TitreMusical(String nom, int duree, int tempo, Album album, Style style) {
        this.nom = nom;
        this.duree = duree;
        this.tempo = tempo;
        this.album = album;
        this.style = style;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getDuree() {
        return duree;
    }

    public void setDuree(int duree) {
        this.duree = duree;
    }

    public int getTempo() {
        return tempo;
    }

    public void setTempo(int tempo) {
        this.tempo = tempo;
    }

    public Album getAlbum() {
        return album;
    }

    public void setAlbum(Album album) {
        this.album = album;
    }

    public Style getStyle() {
        return style;
    }

    public void setStyle(Style style) {
        this.style = style;
    }

    
}
