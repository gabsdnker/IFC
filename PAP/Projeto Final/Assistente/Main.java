import Controle.ControladorDeTarefas;
import Modelo.Projeto;
import Modelo.Tarefa;
import Servico.SugeridorInteligente;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ControladorDeTarefas controlador = new ControladorDeTarefas();
        SugeridorInteligente ia = new SugeridorInteligente();

        System.out.println("Bem-vindo ao Assistente de Estudos!");

        // Adiciona tarefas simples
        System.out.print("Quantas tarefas você deseja adicionar? ");
        int quantidade = scanner.nextInt();
        scanner.nextLine(); // Limpa o buffer

        for (int i = 0; i < quantidade; i++) {
            System.out.print("Digite o título da tarefa " + (i + 1) + ": ");
            String titulo = scanner.nextLine();
            controlador.criarTarefa(titulo);
        }

        // Cria um projeto com tarefas
        System.out.print("\nDigite o nome do seu projeto de estudos: ");
        String nomeProjeto = scanner.nextLine();

        Projeto projeto = new Projeto(nomeProjeto);

        System.out.print("Quantas tarefas deseja adicionar ao projeto? ");
        int tarefasProjeto = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < tarefasProjeto; i++) {
            System.out.print("Tarefa " + (i + 1) + ": ");
            String titulo = scanner.nextLine();
            projeto.adicionarTarefa(new Tarefa(titulo));
        }
        //Adicionado
        System.out.println("\nResumo das Tarefas: ");
        controlador.criarTarefa(titulo);

        System.out.println("\nResumo do Projeto:");
        projeto.exibir();

        // IA simulada
        System.out.println("\nSugestão Inteligente: " + ia.sugerirTarefa());

        scanner.close();
    }
}
