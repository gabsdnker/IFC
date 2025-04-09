public class ConexaoReal implements ConexaoBanco {
    private String nome;

    public ConexaoReal(String nome) {
        this.nome = nome;
    }

    @Override
    public void conectar() {
        System.out.println(nome + " conectado ao banco de dados.");
    }

    @Override
    public void desconectar() {
        System.out.println(nome + " desconectado do banco de dados.");
    }
}
