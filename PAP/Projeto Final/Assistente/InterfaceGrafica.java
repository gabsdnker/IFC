//Padrão Arquitetural MVC(View)
import Command.Comando;
import Command.ComandoAdicionarTarefa;
import Controle.ControladorDeTarefas;
import Controle.GerenciadorDeTarefas;
import Fabrica.FabricaProjeto;
import Fabrica.FabricaTarefa;
import Modelo.Projeto;
import Modelo.Tarefa;
import Observer.ObservadorTarefa;
import Observer.ObservadorTarefaImpl;
import Servico.EstrategiaAleatoria;
import Servico.EstrategiaHorario;
import Servico.SugeridorInteligente;
import javax.swing.*;
import java.awt.*;

public class InterfaceGrafica extends JFrame{
    // Campos de texto para entrada de tarefas e projetos
    private JTextField campoTarefa;
    private JTextField campoProjeto;
    private ControladorDeTarefas controlador;
    private SugeridorInteligente ia;
    private Projeto projeto;

    // Listas para exibir tarefas e projetos
    private JList<String> listaTarefas;
    private DefaultListModel<String> modeloTarefas;

    private JList<String> listaProjetos;
    private DefaultListModel<String> modeloProjeto;

    private JComboBox<String> seletorEstrategia;

    public InterfaceGrafica(){
        super("Asistente de Estudos com Agenda Inteligente");

        // Inicializa o controlador de tarefas, IA e projeto
        controlador = new ControladorDeTarefas();
        ia = new SugeridorInteligente(new EstrategiaHorario());
        projeto = FabricaProjeto.criarProjeto("Meu Projeto");

        //Observador para atualizar  lista de tarefas
        modeloTarefas = new DefaultListModel<>();
        listaTarefas = new JList<>(modeloTarefas);
        ObservadorTarefa observador = new ObservadorTarefaImpl(modeloTarefas);

        GerenciadorDeTarefas.getInstancia().adicionarObservador(observador);

        //Observador para atualizar lista de projetos
        modeloProjeto = new DefaultListModel<>();
        listaProjetos = new JList<>(modeloProjeto);

        configurarInterface();
    }

    private void configurarInterface(){
        // Configura o layout do JFrame
        setLayout(new BorderLayout());

        // Campos de entrada
        campoTarefa = new JTextField();
        campoProjeto = new JTextField();

        //Botões para adicionar tarefas e projetos 
        JButton botaoAdicionarTarefa = new JButton("Adicionar Tarefa");
        botaoAdicionarTarefa.addActionListener(e -> adicionarTarefa());

        JButton botaoAdicionarProjeto = new JButton("Adicionar Projeto");
        botaoAdicionarProjeto.addActionListener(e -> adicionarProjeto());

        JPanel painelEntrada = new JPanel(new GridLayout(1, 2)); // Divide em duas colunas

        // Painel da esquerda: tarefas
        JPanel painelTarefa = new JPanel(new BorderLayout(5, 5));
        painelTarefa.add(new JLabel("Tarefa:"), BorderLayout.NORTH);
        painelTarefa.add(campoTarefa, BorderLayout.CENTER);
        painelTarefa.add(botaoAdicionarTarefa, BorderLayout.SOUTH);

        // Painel da direita: projetos
        JPanel painelProjeto = new JPanel(new BorderLayout(5, 5));
        painelProjeto.add(new JLabel("Projeto:"), BorderLayout.NORTH);
        painelProjeto.add(campoProjeto, BorderLayout.CENTER);
        painelProjeto.add(botaoAdicionarProjeto, BorderLayout.SOUTH);

        // Adiciona os dois subpainéis ao painel de entrada
        painelEntrada.add(painelTarefa);
        painelEntrada.add(painelProjeto);

        //Botões para excluir tarefas e projetos
        JButton botaoExcluirTarefa = new JButton("Excluir Tarefa");
        botaoExcluirTarefa.addActionListener(e -> excluirTarefa());

        JButton botaoExcluirProjeto = new JButton("Excluir Projeto");
        botaoExcluirProjeto.addActionListener(e -> excluirProjeto());

        //Adicionando os painéis de entrada e listas ao JFrame
        JScrollPane scrollTarefas = new JScrollPane(listaTarefas);
        JScrollPane scrollProjetos = new JScrollPane(listaProjetos);

        // Painel de tarefas com botão de exclusão
        JPanel painelTarefas = new JPanel(new BorderLayout());
        painelTarefas.add(new JLabel("Lista de Tarefas"), BorderLayout.NORTH);
        painelTarefas.add(scrollTarefas, BorderLayout.CENTER);
        painelTarefas.add(botaoExcluirTarefa, BorderLayout.SOUTH);

        // Painel de projetos com botão de exclusão
        JPanel painelProjetos = new JPanel(new BorderLayout());
        painelProjetos.add(new JLabel("Lista de Projetos"), BorderLayout.NORTH);
        painelProjetos.add(scrollProjetos, BorderLayout.CENTER);
        painelProjetos.add(botaoExcluirProjeto, BorderLayout.SOUTH);

        // Painel central com os dois painéis acima
        JPanel painelCentro = new JPanel(new GridLayout(2, 1));
        painelCentro.add(painelTarefas);
        painelCentro.add(painelProjetos);

        // ComboBox para selecionar a estratégia de sugestão
        String[] estrategias = { "Horário", "Aleatória" };
        seletorEstrategia = new JComboBox<>(estrategias);
        seletorEstrategia.addActionListener(e -> atualizarEstrategia());

        // Botão de sugestão
        JButton botaoSugestao = new JButton("Mostrar Sugestão Inteligente");
        botaoSugestao.addActionListener(e -> mostrarSugestao());

        // Painel sul com seletor + botão sugestão
        JPanel painelSul = new JPanel(new BorderLayout(5, 5));
        painelSul.add(new JLabel("Selecione a Estratégia:"), BorderLayout.NORTH);
        // Adiciona o seletor de estratégia e o botão de sugestão ao painel sul
        painelSul.add(seletorEstrategia, BorderLayout.CENTER);
        painelSul.add(botaoSugestao, BorderLayout.SOUTH);

        JPanel painelEstrategia = new JPanel(new GridLayout(1, 1));
        painelEstrategia.add(painelSul);

        // Adiciona os componentes ao JFrame
        add(painelEntrada, BorderLayout.NORTH);
        add(painelCentro, BorderLayout.CENTER);
        add(painelEstrategia, BorderLayout.SOUTH);

        // Configurações do JFrame
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Ajusta o tamanho da janela
        setSize(600, 700);
        // Centraliza a janela na tela
        setLocationRelativeTo(null);
        // Torna a janela visível
        setVisible(true);
    }

    // Métodos para adicionar, excluir e atualizar tarefas e projetos
    private void adicionarTarefa(){
        String titulo = campoTarefa.getText().trim();
        // Verifica se o campo de texto não está vazio
        if(!titulo.isEmpty()){
            Comando comando = new ComandoAdicionarTarefa(titulo, controlador);
            // Adiciona a tarefa ao gerenciador de tarefas
            comando.executar();
            campoTarefa.setText("");
        } else {
            JOptionPane.showMessageDialog(this, "Digite um título para a tarefa.");
        }
    }

    private void atualizarEstrategia() {
        String escolha = (String) seletorEstrategia.getSelectedItem();
        if (escolha.equals("Horário")) {
            ia.setEstrategia(new EstrategiaHorario());
        } else if (escolha.equals("Aleatória")) {
            ia.setEstrategia(new EstrategiaAleatoria());
        }
    }

    private void adicionarProjeto(){
        String titulo2 = campoProjeto.getText().trim();
        // Verifica se o campo de texto não está vazio
        if(!titulo2.isEmpty()){
            Tarefa t2 = FabricaTarefa.criarTarefa(titulo2);
            // Adiciona a tarefa ao projeto
            projeto.adicionarTarefa(t2);
            atualizarProjeto();
            campoProjeto.setText("");
        } else {
            JOptionPane.showMessageDialog(this, "Digite um título para o projeto.");
        }
    }

    private void excluirTarefa(){
        String selecionada = listaTarefas.getSelectedValue();
        // Verifica se uma tarefa foi selecionada
        // Se sim, remove a tarefa do gerenciador de tarefas
        if(selecionada != null){
            GerenciadorDeTarefas.getInstancia().getTarefas().removeIf(t2 -> t2.getTitulo().equalsIgnoreCase(selecionada));
            GerenciadorDeTarefas.getInstancia().notificarObservador();
        } else {
            JOptionPane.showMessageDialog(this, "Selecione uma tarefa para excluir.");
        }
    }

    private void excluirProjeto(){
        String selecionada = listaProjetos.getSelectedValue();
        // Verifica se um projeto foi selecionado
        // Se sim, remove o projeto do gerenciador de tarefas
        if(selecionada != null){
            projeto.getTarefas().removeIf(t2 -> t2.getTitulo().equalsIgnoreCase(selecionada));
            projeto.notificarObservador();
            atualizarProjeto();
        } else {
            JOptionPane.showMessageDialog(this, "Selecione um projeto para excluir.");
        }
    }

    private void atualizarProjeto(){
        // Atualiza a lista de tarefas do projeto
        modeloProjeto.clear();
        for(Tarefa t2 : projeto.getTarefas()){
            modeloProjeto.addElement(t2.getTitulo());
        }
    }

    private void mostrarSugestao(){
        // Mostra uma sugestão de tarefa inteligente
        // Verifica se há tarefas no gerenciador de tarefas
        JOptionPane.showMessageDialog(this, "Sugestão: " + ia.sugerirTarefa(), "Assistente IA", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String[] args){
        new InterfaceGrafica();
    }

}