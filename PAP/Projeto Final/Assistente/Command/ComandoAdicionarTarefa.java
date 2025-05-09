package Command;

import Controle.ControladorDeTarefas;
import Controle.GerenciadorDeTarefas;
import Modelo.Tarefa;

public class ComandoAdicionarTarefa implements Comando {
    private String titulo;
    private ControladorDeTarefas controlador;
    /// Construtor da classe ComandoAdicionarTarefa
    /// Recebe o título da tarefa e o controlador de tarefas
    public ComandoAdicionarTarefa(String titulo, ControladorDeTarefas controlador) {
        this.titulo = titulo;
        this.controlador = controlador;
    }

    @Override
    /// Método executar da interface Comando
    /// Cria uma nova tarefa com o título fornecido e a adiciona ao gerenciador de tarefas
    public void executar() {
        // Cria uma nova tarefa com o título fornecido
        controlador.criarTarefa(titulo);
        
        GerenciadorDeTarefas.getInstancia().notificarObservador();
    }
}