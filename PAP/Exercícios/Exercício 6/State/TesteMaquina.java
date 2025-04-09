// Interface Estado
interface Estado {
    void inserirMoeda(MaquinaBolinhas maquina);
    void ejetarMoeda(MaquinaBolinhas maquina);
    void virarManivela(MaquinaBolinhas maquina);
    void entregar(MaquinaBolinhas maquina);
}

// Estados da Máquina
class SemCredito implements Estado {
    public void inserirMoeda(MaquinaBolinhas maquina) {
        System.out.println("Moeda inserida.");
        maquina.setEstado(maquina.getComCredito());
    }

    public void ejetarMoeda(MaquinaBolinhas maquina) {
        System.out.println("Nenhuma moeda para devolver.");
    }

    public void virarManivela(MaquinaBolinhas maquina) {
        System.out.println("Você girou a manivela, mas não há crédito.");
    }

    public void entregar(MaquinaBolinhas maquina) {
        System.out.println("Nenhuma bolinha foi entregue.");
    }
}

class ComCredito implements Estado {
    public void inserirMoeda(MaquinaBolinhas maquina) {
        System.out.println("Você já inseriu uma moeda.");
    }

    public void ejetarMoeda(MaquinaBolinhas maquina) {
        System.out.println("Moeda devolvida.");
        maquina.setEstado(maquina.getSemCredito());
    }

    public void virarManivela(MaquinaBolinhas maquina) {
        System.out.println("Você girou a manivela...");
        if (maquina.getEstoque() == 0) {
            maquina.setEstado(maquina.getEsgotado());
        } else {
            if (Math.random() < 0.1) {
                maquina.setEstado(maquina.getVencedor());
            } else {
                maquina.setEstado(maquina.getVendido());
            }
        }
        maquina.getEstado().entregar(maquina);
    }

    public void entregar(MaquinaBolinhas maquina) {
        System.out.println("Nenhuma bolinha foi entregue.");
    }
}

class Vendido implements Estado {
    public void inserirMoeda(MaquinaBolinhas maquina) {
        System.out.println("Aguarde, estamos entregando sua bolinha.");
    }

    public void ejetarMoeda(MaquinaBolinhas maquina) {
        System.out.println("Você já acionou a alavanca.");
    }

    public void virarManivela(MaquinaBolinhas maquina) {
        System.out.println("Girar novamente não dará outra bolinha.");
    }

    public void entregar(MaquinaBolinhas maquina) {
        System.out.println("Uma bolinha foi entregue!");
        maquina.decrementarEstoque();
        if (maquina.getEstoque() == 0) {
            maquina.setEstado(maquina.getEsgotado());
        } else {
            maquina.setEstado(maquina.getSemCredito());
        }
    }
}

class Vencedor implements Estado {
    public void inserirMoeda(MaquinaBolinhas maquina) {
        System.out.println("Aguarde, estamos entregando suas bolinhas.");
    }

    public void ejetarMoeda(MaquinaBolinhas maquina) {
        System.out.println("Você já acionou a alavanca.");
    }

    public void virarManivela(MaquinaBolinhas maquina) {
        System.out.println("Girar novamente não dará outra bolinha.");
    }

    public void entregar(MaquinaBolinhas maquina) {
        System.out.println("Parabéns! Você ganhou duas bolinhas!");
        maquina.decrementarEstoque(2);
        if (maquina.getEstoque() == 0) {
            maquina.setEstado(maquina.getEsgotado());
        } else {
            maquina.setEstado(maquina.getSemCredito());
        }
    }
}

class Esgotado implements Estado {
    public void inserirMoeda(MaquinaBolinhas maquina) {
        System.out.println("A máquina está vazia. Não é possível inserir moeda.");
    }

    public void ejetarMoeda(MaquinaBolinhas maquina) {
        System.out.println("Nenhuma moeda inserida.");
    }

    public void virarManivela(MaquinaBolinhas maquina) {
        System.out.println("A máquina está vazia.");
    }

    public void entregar(MaquinaBolinhas maquina) {
        System.out.println("Nenhuma bolinha foi entregue.");
    }
}

class MaquinaBolinhas {
    private Estado semCredito = new SemCredito();
    private Estado comCredito = new ComCredito();
    private Estado vendido = new Vendido();
    private Estado vencedor = new Vencedor();
    private Estado esgotado = new Esgotado();

    private Estado estadoAtual;
    private int estoque;

    public MaquinaBolinhas(int estoque) {
        this.estoque = estoque;
        this.estadoAtual = (estoque > 0) ? semCredito : esgotado;
    }

    public void setEstado(Estado estado) { this.estadoAtual = estado; }
    public Estado getEstado() { return estadoAtual; }
    public int getEstoque() { return estoque; }
    public void decrementarEstoque() { estoque--; }
    public void decrementarEstoque(int quantidade) { estoque -= Math.min(quantidade, estoque); }

    public Estado getSemCredito() { return semCredito; }
    public Estado getComCredito() { return comCredito; }
    public Estado getVendido() { return vendido; }
    public Estado getVencedor() { return vencedor; }
    public Estado getEsgotado() { return esgotado; }

    public void inserirMoeda() { estadoAtual.inserirMoeda(this); }
    public void ejetarMoeda() { estadoAtual.ejetarMoeda(this); }
    public void virarManivela() { estadoAtual.virarManivela(this); }
    public void entregar() { estadoAtual.entregar(this); }
}

public class TesteMaquina {
    public static void main(String[] args) {
        MaquinaBolinhas maquina = new MaquinaBolinhas(5);
        maquina.inserirMoeda();
        maquina.virarManivela();
        maquina.inserirMoeda();
        maquina.virarManivela();
        maquina.ejetarMoeda();
        maquina.inserirMoeda();
        maquina.virarManivela();
        maquina.inserirMoeda();
        maquina.virarManivela();
        maquina.inserirMoeda();
        maquina.virarManivela();
    }
}
