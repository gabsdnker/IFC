// Interface para a estratégia de movimentação
interface Movimentacao {
    void mover();
}

// Implementações das estratégias
class MovimentacaoMotor implements Movimentacao {
    public void mover() {
        System.out.println("Movendo-se com motor.");
    }
}

class MovimentacaoRemos implements Movimentacao {
    public void mover() {
        System.out.println("Movendo-se com remos.");
    }
}

class MovimentacaoVela implements Movimentacao {
    public void mover() {
        System.out.println("Movendo-se com vela.");
    }
}

// Classe Barco
class Barco {
    private String nome;
    private Movimentacao movimentacao;

    public Barco(String nome, Movimentacao movimentacao) {
        this.nome = nome;
        this.movimentacao = movimentacao;
    }

    public void exibirMovimento() {
        System.out.print(nome + ": ");
        movimentacao.mover();
    }
}

// Classe principal para teste
public class LocacaoBarcos {
    public static void main(String[] args) {
        Barco bateira = new Barco("Bateira", new MovimentacaoMotor());
        Barco iate = new Barco("Iate", new MovimentacaoMotor());
        Barco canoa = new Barco("Canoa", new MovimentacaoRemos());
        Barco jangada = new Barco("Jangada", new MovimentacaoRemos());
        Barco barcoAVela = new Barco("Barco a Vela", new MovimentacaoVela());

        bateira.exibirMovimento();
        iate.exibirMovimento();
        canoa.exibirMovimento();
        jangada.exibirMovimento();
        barcoAVela.exibirMovimento();
    }
}
