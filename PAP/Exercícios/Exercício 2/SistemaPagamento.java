// 1. Classe Abstrata para Pagamento (Polimorfismo e Alta Coesão)
abstract class Pagamento {
    public abstract void processarPagamento(double valor);
}

// 2. Classe que representa o pagamento por Cartão de Crédito
class PagamentoCartaoCredito extends Pagamento {
    @Override
    public void processarPagamento(double valor) {
        System.out.println("Pagamento de R$ " + valor + " realizado com Cartão de Crédito.");
    }
}

// 3. Classe que representa o pagamento por Dinheiro
class PagamentoDinheiro extends Pagamento {
    @Override
    public void processarPagamento(double valor) {
        System.out.println("Pagamento de R$ " + valor + " realizado com Dinheiro.");
    }
}

// 4. Classe que representa o pagamento por Pix
class PagamentoPix extends Pagamento {
    @Override
    public void processarPagamento(double valor) {
        System.out.println("Pagamento de R$ " + valor + " realizado com Pix.");
    }
}

// 5. Classe Pedido (Controller)
class Pedido {
    private double valorTotal;
    private Pagamento pagamento;

    public Pedido(double valorTotal) {
        this.valorTotal = valorTotal;
    }

    // 6. Método para definir o método de pagamento (Controller)
    public void definirPagamento(Pagamento pagamento) {
        this.pagamento = pagamento;
    }

    // 7. Método para processar o pagamento (Information Expert)
    public void finalizarPedido() {
        if (pagamento != null) {
            pagamento.processarPagamento(valorTotal);
        } else {
            System.out.println("Método de pagamento não definido.");
        }
    }
}

public class SistemaPagamento {
    public static void main(String[] args) {
        // Criando um pedido de R$ 100,00
        Pedido pedido = new Pedido(100.0);
        
        // Definindo o pagamento como Cartão de Crédito
        pedido.definirPagamento(new PagamentoCartaoCredito());
        pedido.finalizarPedido(); // Processa o pagamento com Cartão de Crédito
        
        // Criando outro pedido de R$ 50,00
        Pedido pedido2 = new Pedido(50.0);
        
        // Definindo o pagamento como Dinheiro
        pedido2.definirPagamento(new PagamentoDinheiro());
        pedido2.finalizarPedido(); // Processa o pagamento com Dinheiro

        // Criando outro pedido de R$ 20,00
        Pedido pedido3 = new Pedido(20.0);

        // Definindo o pagamento como Pix
        pedido3.definirPagamento(new PagamentoPix());
        pedido3.finalizarPedido(); // Processa o pagamento com Pix
    }
}

