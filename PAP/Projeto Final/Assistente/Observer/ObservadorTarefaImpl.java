package Observer;

import javax.swing.DefaultListModel;
import Controle.GerenciadorDeTarefas;
import Modelo.Tarefa;

/// ObservadorTarefaImpl é uma implementação do padrão Observer
/// que atualiza um modelo de lista com as tarefas atuais
public class ObservadorTarefaImpl implements ObservadorTarefa {
    private DefaultListModel<String> modelo;

    public ObservadorTarefaImpl(DefaultListModel<String> modelo) {
        this.modelo = modelo;
    }

    @Override
    public void atualizar() {
        // Atualiza o modelo da lista com as tarefas atuais
        modelo.clear();
        for (Tarefa t : GerenciadorDeTarefas.getInstancia().getTarefas()) {
            modelo.addElement(t.getTitulo());
        }
    }
}
