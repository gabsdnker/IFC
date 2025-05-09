//Padrão Arquitetural MVC (Model)
package Modelo;

import java.util.ArrayList;
import java.util.List;

public class Projeto{
    private String nome;
    private List<Tarefa> tarefas;
        private List<Observer.ObservadorTarefa> observadores = new ArrayList<>();

    // Construtor da classe Projeto
    // Inicializa a lista de tarefas e o nome do projeto
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

    // Método para adicionar um observador
    public void adicionarObservador(Observer.ObservadorTarefa o) {
        observadores.add(o);
    }

    public void notificarObservador() {
        for (Observer.ObservadorTarefa o : observadores) {
            o.atualizar();
        }
    }
}
