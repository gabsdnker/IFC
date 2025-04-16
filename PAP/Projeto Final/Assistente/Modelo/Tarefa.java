//Padrão Arquitetural MVC (Model)
package Modelo;

public class Tarefa{
    private String titulo;

    public Tarefa(String titulo){
        this.titulo = titulo;
    }
    public String getTitulo(){
       return titulo;
    }
    public void exibir() {
        System.out.println("- " + titulo);
    }
}
