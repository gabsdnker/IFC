package Controle;

import Modelo.Tarefa;

public class GerenciadorDeTarefas{
    private static GerenciadorDeTarefas instancia;
    private List<Tarefa> tarefas:

    private GerenciadorDeTarefas(){
        tarefas = new ArrayList<>();
    }

    public static GerenciadorDeTarefas getInstancia(){
        if (instancia == null) {
            instancia = new GerenciadorDeTarefas();
        }
        return instancia;
    }
    public void adicionar(Tarefa tarefa){
         tarefas.add(tarefa);
    }
    System.out.println("Tarefa adicionada: " + tarefa.getTitulo());
    public List<Tarefa> getTarefas(){
        return tarefas;
    }
}
