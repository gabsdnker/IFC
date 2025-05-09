//Padrão de Projeto Singleton
//Padrão Arquitetural MVC (Controller)
//Construtor privado para evitar instâncias externas
package Controle;

import Modelo.Tarefa;
import java.util.ArrayList;
import java.util.List;

public class GerenciadorDeTarefas{
    private static GerenciadorDeTarefas instancia;
    private List<Tarefa> tarefas;
    private List<Observer.ObservadorTarefa> observadores = new ArrayList<>();

    private GerenciadorDeTarefas(){
        tarefas = new ArrayList<>();
    }

    //Método estático para obter a instância única
    public static GerenciadorDeTarefas getInstancia(){
        if (instancia == null) {
            instancia = new GerenciadorDeTarefas();
        }
        return instancia;
    }

    //Método para adicionar uma tarefa
    public void adicionar(Tarefa tarefa){
         tarefas.add(tarefa); 
    }

    public List<Tarefa> getTarefas(){
        return tarefas;
    }
    
    // Método para adicionar um observador
    public void adicionarObservador(Observer.ObservadorTarefa o) {
        observadores.add(o);
    }
    // Método para notificar os observadores sobre mudanças
    public void notificarObservador() {
        for (Observer.ObservadorTarefa o : observadores) {
            o.atualizar();
        }
    }
}
