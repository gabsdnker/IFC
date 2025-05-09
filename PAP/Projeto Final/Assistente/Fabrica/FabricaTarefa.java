package Fabrica;

import Modelo.Tarefa;

public class FabricaTarefa {
    // Método para criar uma tarefa
    // Este método é responsável por criar uma nova tarefa com o título fornecido
    public static Tarefa criarTarefa(String titulo) {
        return new Tarefa(titulo);
    }
}