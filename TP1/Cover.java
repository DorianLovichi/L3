public class Cover extends TitreMusical {
    private TitreMusical titreOriginal;
    private Artiste artisteOriginal;
    public Cover(String nom, int duree, int tempo, Album album, Style style, TitreMusical titreOriginal,
            Artiste artisteOriginal) {
        super(nom, duree, tempo, album, style);
        this.titreOriginal = titreOriginal;
        this.artisteOriginal = artisteOriginal;
    }

    
}
