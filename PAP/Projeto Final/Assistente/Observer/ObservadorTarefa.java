package Observer;

//Padrão de Projeto Observer
// Interface ObservadorTarefa
public interface ObservadorTarefa {
    // Método que será chamado para notificar o observador sobre mudanças
    // Este método deve ser implementado pelas classes que desejam ser notificadas
    void atualizar();
}
