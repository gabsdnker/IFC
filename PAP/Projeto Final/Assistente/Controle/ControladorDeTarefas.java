package Controle;

import Modelo.Tarefa;

public class ControladorDeTarefas{
    private GerenciadorDeTarefas gerenciador = GerenciadorDeTarefas.getInstancia();

    public void  criarTarefa(String titulo){
        Tarefa tarefa = new Tarefa(titulo);
        gerenciador.adicionar(tarefa);
    }
}