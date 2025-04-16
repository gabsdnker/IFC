package Fabrica;

import Modelo.Tarefa;

public class FabricaTarefa {
    public static Tarefa criarTarefa(String titulo) {
        return new Tarefa(titulo);
    }
}