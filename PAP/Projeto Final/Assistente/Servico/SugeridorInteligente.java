// Padrão GRASP Strategy
package Servico;

public class SugeridorInteligente {
    private EstrategiaSugestao estrategia;

    // Construtor da classe SugeridorInteligente
    public SugeridorInteligente(EstrategiaSugestao estrategia) {
        this.estrategia = estrategia;
    }
    // Método para definir a estratégia de sugestão
    public void setEstrategia(EstrategiaSugestao estrategia) {
        this.estrategia = estrategia;
    }

    // Método que sugere uma tarefa com base na estratégia definida
    public String sugerirTarefa() {
        return estrategia.sugerir();
    }
}
