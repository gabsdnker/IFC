public class RealVideo implements Video {
    private String filename;

    public RealVideo(String filename) {
        this.filename = filename;
        loadVideo(); // carrega o vídeo ao criar
    }

    public void loadVideo() {
        System.out.println("Carregando o vídeo: " + filename);
    }

    @Override
    public void play() {
        System.out.println("Reproduzindo o vídeo: " + filename);
    }
}
