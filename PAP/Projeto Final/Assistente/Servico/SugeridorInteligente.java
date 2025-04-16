// Padrão GRASP Strategy
package Servico;

public class SugeridorInteligente {
    private EstrategiaSugestao estrategia;

    public SugeridorInteligente(EstrategiaSugestao estrategia) {
        this.estrategia = estrategia;
    }

    public void setEstrategia(EstrategiaSugestao estrategia) {
        this.estrategia = estrategia;
    }

    public String sugerirTarefa() {
        return estrategia.sugerir();
    }
}
