//Padrão de Projeto Singleton
package Controle;

import Modelo.Tarefa;
import java.util.ArrayList;
import java.util.List;

public class GerenciadorDeTarefas{
    private static GerenciadorDeTarefas instancia;
    private List<Tarefa> tarefas;

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
         System.out.println("Tarefa adicionada!"); 
    }
    public List<Tarefa> getTarefas(){
        return tarefas;
    }
}
