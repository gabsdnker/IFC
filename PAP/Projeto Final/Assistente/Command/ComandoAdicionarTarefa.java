package Command;

import Controle.ControladorDeTarefas;

public class ComandoAdicionarTarefa implements Comando {
    private String titulo;
    private ControladorDeTarefas controlador;

    public ComandoAdicionarTarefa(String titulo, ControladorDeTarefas controlador) {
        this.titulo = titulo;
        this.controlador = controlador;
    }

    public void executar() {
        controlador.criarTarefa(titulo);
    }
}
