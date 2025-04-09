public class StreamingApp {
    public static void main(String[] args) {
        Video video1 = new VideoProxy("filme_documentario.mp4");

        System.out.println("Usuário navegando pelo catálogo...");

        // Nenhum carregamento ainda
        System.out.println("Usuário decide assistir ao vídeo:");
        video1.play(); // agora carrega e reproduz
    }
}
