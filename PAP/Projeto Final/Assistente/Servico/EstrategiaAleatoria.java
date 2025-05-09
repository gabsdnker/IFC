package Servico;

public class EstrategiaAleatoria implements EstrategiaSugestao {
    // Método que sugere uma ação aleatória
    // Este método retorna uma sugestão aleatória de uma lista de sugestões
    public String sugerir() {
        String[] sugestoes = {
            "Estudar um novo tópico!",
            "Revisar anotações!",
            "Resolver questões antigas!"
        };
        int index = (int)(Math.random() * sugestoes.length);
        return sugestoes[index];
    }
}