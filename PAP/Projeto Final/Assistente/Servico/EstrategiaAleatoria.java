package Servico;

public class EstrategiaAleatoria implements EstrategiaSugestao {
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