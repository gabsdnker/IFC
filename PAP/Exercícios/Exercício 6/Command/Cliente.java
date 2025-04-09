interface Pedido {
    void executar();
}


class PedidoHamburguer implements Pedido {
    private Cozinheiro cozinheiro;

    public PedidoHamburguer(Cozinheiro cozinheiro) {
        this.cozinheiro = cozinheiro;
    }

    @Override
    public void executar() {
        cozinheiro.fazerHamburguer();
    }
}


class PedidoMilkshake implements Pedido {
    private Cozinheiro cozinheiro;

    public PedidoMilkshake(Cozinheiro cozinheiro) {
        this.cozinheiro = cozinheiro;
    }

    @Override
    public void executar() {
        cozinheiro.fazerMilkshake();
    }
}


class Cozinheiro {
    public void fazerHamburguer() {
        System.out.println("Cozinheiro está preparando um hambúrguer...");
    }

    public void fazerMilkshake() {
        System.out.println("Cozinheiro está preparando um milkshake...");
    }
}


class Garconete {
    private Pedido pedido;

    public void setPedido(Pedido pedido) {
        this.pedido = pedido;
    }

    public void processarPedido() {
        if (pedido != null) {
            pedido.executar();
        } else {
            System.out.println("Nenhum pedido foi feito.");
        }
    }
}

public class Cliente {
    public static void main(String[] args) {

        Cozinheiro cozinheiro = new Cozinheiro();
        Garconete garconete = new Garconete();

        Pedido pedidoHamburguer = new PedidoHamburguer(cozinheiro);
        Pedido pedidoMilkshake = new PedidoMilkshake(cozinheiro);

        System.out.println("Cliente: Quero um hambúrguer!");
        garconete.setPedido(pedidoHamburguer);
        garconete.processarPedido();

        System.out.println("Cliente: Quero um milkshake!");
        garconete.setPedido(pedidoMilkshake);
        garconete.processarPedido();
    }
}
