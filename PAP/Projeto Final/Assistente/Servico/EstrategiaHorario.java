package Servico;

import java.time.LocalTime;

public class EstrategiaHorario implements EstrategiaSugestao {
    public String sugerir() {
        LocalTime agora = LocalTime.now();
        if (agora.isBefore(LocalTime.NOON)) return "Revisar conteúdos da manhã!";
        if (agora.isBefore(LocalTime.of(18, 0))) return "Fazer exercícios práticos!";
        return "Planejar o dia seguinte!";
    }
}