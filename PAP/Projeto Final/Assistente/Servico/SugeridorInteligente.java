package Servico;

import java.time.LocalTime;

public class SugeridorInteligente{
    public String sugerirTarefa(){
        LocalTime agora = LocalTime.now();

        if(agora.isBefore(LocalTime.NOON)){
            return "Revisar conteúdos da manhã!";
        } else if (agora.isBefore(LocalTime.of(18, 0))){
            return "Fazer exercícios práticos!";
        } else{
            return "Planejar o dia seguinte!";
        }
    }
}