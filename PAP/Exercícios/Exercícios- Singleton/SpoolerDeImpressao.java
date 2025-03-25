import java.util.LinkedList;
import java.util.Queue;

public class SpoolerDeImpressao {
    private static SpoolerDeImpressao instance;
    private Queue<String> filaDeImpressao;

    // O construtor é privado
    private SpoolerDeImpressao() {
        filaDeImpressao = new LinkedList<>();
    }

    // Única forma de acessar a instância do spooler é por este método - getInstance
    public static synchronized SpoolerDeImpressao getInstance() {
        if (instance == null)
            instance = new SpoolerDeImpressao();

        System.out.println("Instância do Spooler: " + instance);
        return instance;
    }

    public synchronized void adicionarDocumento(String documento) {
        filaDeImpressao.add(documento);
        System.out.println("Documento '" + documento + "' adicionado à fila de impressão.");
    }

    public synchronized void imprimirProximoDocumento() {
        if (!filaDeImpressao.isEmpty()) {
            String documento = filaDeImpressao.poll();
            System.out.println("Imprimindo: " + documento);
        } else
            System.out.println("Nenhum documento na fila.");
    }

        public synchronized void verificarFila() {
        if (filaDeImpressao.isEmpty())
            System.out.println("A fila de impressão está vazia.");
        else
            System.out.println("Documentos na fila: " + filaDeImpressao);
    }
}
