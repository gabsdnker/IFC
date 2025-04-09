// Interface para definir o comportamento de cálculo do valor do imóvel
interface DefinirValorComportamento {
    float definirValor(float espaco, int comodos, char localizacao);
}

// Implementação para imóveis com edificação
class DefinirValorComEdificacao implements DefinirValorComportamento {
    public float definirValor(float espaco, int comodos, char localizacao) {
        float precoBase = getPrecoPorM2(localizacao) * espaco;
        return precoBase + (comodos * 1000);
    }

    private float getPrecoPorM2(char localizacao) {
        return switch (localizacao) {
            case 'A' -> 3000;
            case 'B' -> 1000;
            case 'C' -> 500;
            default -> 0;
        };
    }
}

// Implementação para terrenos sem edificação
class DefinirValorSemEdificacao implements DefinirValorComportamento {
    public float definirValor(float espaco, int comodos, char localizacao) {
        return getPrecoPorM2(localizacao) * espaco;
    }

    private float getPrecoPorM2(char localizacao) {
        return switch (localizacao) {
            case 'A' -> 1500;
            case 'B' -> 750;
            case 'C' -> 200;
            default -> 0;
        };
    }
}

// Classe abstrata Imóvel
abstract class Imovel {
    protected int comodos;
    protected float espaco;
    protected char localizacao;
    protected DefinirValorComportamento estrategiaValor;

    public Imovel(char localizacao, float espaco, int comodos) {
        this.localizacao = localizacao;
        this.espaco = espaco;
        this.comodos = comodos;
    }

    public void setEstrategiaValor(DefinirValorComportamento estrategia) {
        this.estrategiaValor = estrategia;
    }

    public float calcularValor() {
        return estrategiaValor.definirValor(espaco, comodos, localizacao);
    }
}

// Classes concretas Casa, Apartamento e Terreno
class Casa extends Imovel {
    public Casa(char localizacao, float espaco, int comodos) {
        super(localizacao, espaco, comodos);
        this.estrategiaValor = new DefinirValorComEdificacao();
    }
}

class Apartamento extends Imovel {
    public Apartamento(char localizacao, float espaco, int comodos) {
        super(localizacao, espaco, comodos);
        this.estrategiaValor = new DefinirValorComEdificacao();
    }
}

class Terreno extends Imovel {
    public Terreno(char localizacao, float espaco) {
        super(localizacao, espaco, 0);
        this.estrategiaValor = new DefinirValorSemEdificacao();
    }
}

// Classe principal para testar o cálculo do valor dos imóveis
public class CalculadoraImoveis {
    public static void main(String[] args) {
        Imovel casa = new Casa('A', 100, 3);
        System.out.println("Valor da casa: R$ " + casa.calcularValor());
        
        Imovel apartamento = new Apartamento('B', 80, 2);
        System.out.println("Valor do apartamento: R$ " + apartamento.calcularValor());
        
        Imovel terreno = new Terreno('C', 200);
        System.out.println("Valor do terreno: R$ " + terreno.calcularValor());
    }
}
