public class DemoProxy {
    public static void main(String[] args) {
        ConexaoBanco conexao1 = new ConexaoProxy("Usuário1");
        ConexaoBanco conexao2 = new ConexaoProxy("Usuário2");
        ConexaoBanco conexao3 = new ConexaoProxy("Usuário3");
        ConexaoBanco conexao4 = new ConexaoProxy("Usuário4");

        conexao1.conectar();
        conexao2.conectar();
        conexao3.conectar();

        // Esta deve ser recusada
        conexao4.conectar();

        // Libera uma conexão
        conexao2.desconectar();

        // Tenta conectar novamente
        conexao4.conectar();
    }
}
