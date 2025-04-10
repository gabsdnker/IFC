import Controle.ControladorDeTarefas;
import Modelo.Projeto;
import Modelo.Tarefa;
import Servico.SugeridorInteligente;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        ControladorDeTarefas controlador = new ControladorDeTarefas();
        SugeridorInteligente ia = new SugeridorInteligente();

        System.out.println("Bem-vindo a Assistente de Estudos!");
        
        //Adicionar tarefas
        System.out.println("Quantas tarefas você que adicionar?");

        int quantidade = input.nextInt();
        input.nextLine();

        for(int i = 0; i < quantidade; i++){
            System.out.println("Digite o título da tarefa " + (i + 1) + ": ");
            String titulo = input.nextLine();
            controlador.criarTarefa(titulo);
        }

        //Criar projetos
        System.out.println("\nDigite o nome do projeto você quer criar: ");
        String nomeProjeto = input.nextLine();
        Projeto projeto = new Projeto(nomeProjeto);

        System.out.println("Quantas tarefas você deseja adicionar ou projeto?");
        int tarefasProjeto = input.nextInt();
        input.nextLine();

        for( int i = 0; i < tarefasProjeto; i++){
            System.out.println("Tarefa " + (i + 1) + ": ");
            String titulo = input.nextLine();
            projeto.adicionarTarefa(new Tarefa(titulo));
        }

        System.out.println("\nTarefas adicionadas:");
        for(Tarefa t : GerenciadorDeTarefas.getInstancia().getTarefas()){
            System.out.println("- " + t.getTitulo());
        }

        System.out.println("\nProjeto: " + projeto.getTitulo());
        for (Tarefa t : projeto.getTarefas()){
            System.out.println("- " + t.getTitulo());
        }

        System.out.println("\nSugestão Inteligente: " + ia.sugerirTarefa());


    }
}