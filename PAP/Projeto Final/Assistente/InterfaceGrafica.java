import Command.Comando;
import Command.ComandoAdicionarTarefa;
import Controle.ControladorDeTarefas;
import Controle.GerenciadorDeTarefas;
import Modelo.Projeto;
import Modelo.Tarefa;
import Servico.EstrategiaHorario;
import Servico.SugeridorInteligente;
import java.awt.*;
import javax.swing.*;

public class InterfaceGrafica extends JFrame{
    private JTextField campoTarefa;
    private JTextArea areaTarefas;
    private JTextField campoProjeto;
    private JTextArea areaProjeto;
    private ControladorDeTarefas controlador;
    private SugeridorInteligente ia;
    private Projeto projeto;

    public InterfaceGrafica(){
        super("Assistente de Estudos com Agenda Inteligente");

        controlador= new ControladorDeTarefas();
        ia = new SugeridorInteligente(new EstrategiaHorario());
        projeto = new Projeto("Meu Projeto");

        setLayout(new BorderLayout());
        JPanel painelEntrada = new JPanel(new GridLayout(4, 1));

        campoTarefa = new JTextField();
        JButton botaoAdicionarTarefa = new JButton("Adicionar Tarefa");
        botaoAdicionarTarefa.addActionListener(e -> adicionarTarefa());

        campoProjeto = new JTextField();
        JButton botaoAdicionarProjeto = new JButton("Adicionar Projeto");
        botaoAdicionarProjeto.addActionListener(e -> adicionarProjeto());

        painelEntrada.add(new JLabel("Título:"));
        painelEntrada.add(campoTarefa);
        painelEntrada.add(botaoAdicionarTarefa);
        painelEntrada.add(botaoAdicionarProjeto);

        areaTarefas = new  JTextArea(10, 30);
        areaTarefas.setEditable(false);
        JScrollPane scrollTarefas = new JScrollPane(areaTarefas);

        areaProjeto = new JTextArea(5, 30);
        areaProjeto.setEditable(false);
        JScrollPane scrollProjeto = new JScrollPane(areaProjeto);

        JButton botaoSugestao = new JButton("Mostrar Sugestão Inteligente");
        botaoSugestao.addActionListener(e -> mostrarSugestao());

        JPanel painelCentro = new JPanel(new GridLayout(2 ,1));
        painelCentro.add(scrollTarefas);
        painelCentro.add(scrollProjeto);

        add(painelEntrada, BorderLayout.NORTH);
        add(painelCentro, BorderLayout.CENTER);
        add(botaoSugestao, BorderLayout.SOUTH);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600, 700);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void adicionarTarefa(){
        String titulo = campoTarefa.getText().trim();
        if(!titulo.isEmpty()){
            Comando comando = new ComandoAdicionarTarefa(titulo, controlador);
            comando.executar();
            campoTarefa.setText("");
            atualizarListaTarefas();
        }
    }
    
    private void adicionarProjeto(){
        String titulo = campoTarefa.getText().trim();
        if (!titulo.isEmpty()){
            Tarefa t = new Tarefa(titulo);
            projeto.adicionarTarefa(t);
            atualizarListaProjeto();
            campoTarefa.setText("");
        }
    }

    private void atualizarListaTarefas(){
        areaTarefas.setText("Tarefas: \n");
        for(Tarefa t : GerenciadorDeTarefas.getInstancia().getTarefas()){
            areaTarefas.append("- " + t.getTitulo() + "\n");
        }
    }

    private void atualizarListaProjeto(){
        areaProjeto.setText("Projeto: \n");
        for(Tarefa t : projeto.getTarefas()){
            areaProjeto.append("- " + t.getTitulo() + "\n");
        }
    }

    private void mostrarSugestao(){
        JOptionPane.showMessageDialog(this, "Sugestão Inteligente: " + ia.sugerirTarefa(), "Assistente IA", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args) {
        new InterfaceGrafica();
    }
}