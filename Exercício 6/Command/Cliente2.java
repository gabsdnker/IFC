import java.util.LinkedList;
import java.util.Queue;

interface ComandoImpressao {
    void executar();
    void cancelar();
}

class ImprimirDocumento implements ComandoImpressao {
    private Impressora impressora;
    private String documento;

    public ImprimirDocumento(Impressora impressora, String documento) {
        this.impressora = impressora;
        this.documento = documento;
    }

    @Override
    public void executar() {
        impressora.imprimir(documento);
    }

    @Override
    public void cancelar() {
        impressora.cancelarImpressao(documento);
    }

    public String getDocumento() {
        return documento;
    }
}

class Impressora {
    public void imprimir(String documento) {
        System.out.println("Imprimindo documento: " + documento);
    }

    public void cancelarImpressao(String documento) {
        System.out.println("Impressão cancelada: " + documento);
    }
}

class FilaImpressao {
    private static FilaImpressao instancia; 
    private Queue<ComandoImpressao> fila = new LinkedList<>();
    private ComandoImpressao ultimoComando; // Para controle de cancelamento

    private FilaImpressao() {}

    public static synchronized FilaImpressao getInstancia() {
        if (instancia == null) {
            instancia = new FilaImpressao();
        }
        return instancia;
    }

    public void adicionarDocumento(ComandoImpressao comando) {
        fila.add(comando);
        ultimoComando = comando;
        System.out.println("Documento adicionado à fila: " + ((ImprimirDocumento) comando).getDocumento());
    }

    public void processarFila() {
        while (!fila.isEmpty()) {
            ComandoImpressao comando = fila.poll();
            comando.executar();
        }
    }

    public void cancelarUltimoDocumento() {
        if (ultimoComando != null) {
            ultimoComando.cancelar();
            fila.remove(ultimoComando);
            ultimoComando = null;
        } else {
            System.out.println("Nenhum documento para cancelar.");
        }
    }
}

public class Cliente {
    public static void main(String[] args) {
        Impressora impressora = new Impressora();
        FilaImpressao fila = FilaImpressao.getInstancia();

        ComandoImpressao doc1 = new ImprimirDocumento(impressora, "Relatório.pdf");
        ComandoImpressao doc2 = new ImprimirDocumento(impressora, "Contrato.docx");
        ComandoImpressao doc3 = new ImprimirDocumento(impressora, "Imagem.png");

        fila.adicionarDocumento(doc1);
        fila.adicionarDocumento(doc2);
        fila.adicionarDocumento(doc3);

        fila.cancelarUltimoDocumento();

        fila.processarFila();
    }
}
