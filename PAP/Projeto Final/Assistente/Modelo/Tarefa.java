//Padrão Arquitetural MVC (Model)
package Modelo;

public class Tarefa {
    private String titulo;

    // Construtor da classe Tarefa
    public Tarefa(String titulo){
        this.titulo = titulo;
    }
    public String getTitulo(){
       return titulo;
    }
}
