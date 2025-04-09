public class VideoProxy implements Video {
    private RealVideo realVideo;
    private String filename;

    public VideoProxy(String filename) {
        this.filename = filename;
    }

    @Override
    public void play() {
        if (realVideo == null) {
            realVideo = new RealVideo(filename); // só carrega se necessário
        }
        realVideo.play();
    }
}
