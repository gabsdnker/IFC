//Padrão Arquitetural MVC (Model)
package Modelo;

import java.util.ArrayList;
import java.util.List;

public class Projeto{
    private String nome;
    private List<Tarefa> tarefas;

    public Projeto(String nome){
        this.tarefas = new ArrayList<>();
        this.nome = nome;
    }

    public void adicionarTarefa(Tarefa tarefa){
        tarefas.add(tarefa);
    }
    
    public List<Tarefa> getTarefas(){
        return tarefas;
    }

    public void exibir(){
        System.out.println("Projeto: " + nome);
        for(Tarefa  t : tarefas){
            t.exibir();
        }
    }
}
