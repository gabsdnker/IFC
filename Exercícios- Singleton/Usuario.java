public class Usuario implements Runnable {
    private String nomeUsuario;
    private String documento;

    public Usuario(String nomeUsuario, String documento) {
        this.nomeUsuario = nomeUsuario;
        this.documento = documento;
    }

    @Override
    public void run() {
        SpoolerDeImpressao spooler = SpoolerDeImpressao.getInstance();
        System.out.println(nomeUsuario + " está tentando enviar o documento '" + documento + "' para a fila de impressão.");
        spooler.adicionarDocumento(documento);
    }

    public static void main(String[] args) {
        Thread usuario1 = new Thread(new Usuario("Usuário 1", "boleto.pdf"));
        Thread usuario2 = new Thread(new Usuario("Usuário 2", "Prova_de_padroes_de_projeto.docx"));
        Thread usuario3 = new Thread(new Usuario("Usuário 3", "FotosMaratona2024.png"));
        Thread usuario4 = new Thread(new Usuario("Usuário 4", "rendimentos.ods"));

        usuario1.start();
        usuario2.start();
        usuario3.start();
        usuario4.start();

        try {
            usuario1.join();
            usuario2.join();
            usuario3.join();
            usuario4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        SpoolerDeImpressao spooler = SpoolerDeImpressao.getInstance();
        spooler.verificarFila();
        spooler.imprimirProximoDocumento();
        spooler.imprimirProximoDocumento();

        System.out.println("Criando várias referências ao Singleton:");
        SpoolerDeImpressao spooler1 = SpoolerDeImpressao.getInstance();
        SpoolerDeImpressao spooler2 = SpoolerDeImpressao.getInstance();
        SpoolerDeImpressao spooler3 = SpoolerDeImpressao.getInstance();

        System.out.println("\nComparando as referências:");
        System.out.println("spooler1 == spooler2? " + (spooler1 == spooler2));
        System.out.println("spooler1 == spooler3? " + (spooler1 == spooler3));
    }
}