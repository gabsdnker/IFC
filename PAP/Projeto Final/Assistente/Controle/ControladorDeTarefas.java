//Padrão Arquitetural MVC (Controller)
package Controle;

import Modelo.Tarefa;

public class ControladorDeTarefas{
    private GerenciadorDeTarefas gerenciador = GerenciadorDeTarefas.getInstancia();

    public void  criarTarefa(String titulo){
        // Cria uma nova tarefa e a adiciona ao gerenciador de tarefas
        // e notifica os observadores
        Tarefa tarefa = new Tarefa(titulo);
        gerenciador.adicionar(tarefa);
    }
}
