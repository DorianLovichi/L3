public class Remix extends TitreMusical {
    private Artiste artisteOriginal;

    public Remix(String nom, int duree, int tempo, Album album, Style style, Artiste artisteOriginal) {
        super(nom, duree, tempo, album, style);
        this.artisteOriginal = artisteOriginal;
    }
  
    
}
