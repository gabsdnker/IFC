import java.util.ArrayList;
import java.util.List;

public class ConexaoProxy implements ConexaoBanco {
    private static final int LIMITE_CONEXOES = 3;
    private static int conexoesAtivas = 0;
    private static List<ConexaoReal> conexoes = new ArrayList<>();
    private ConexaoReal conexaoReal;

    private String nome;

    public ConexaoProxy(String nome) {
        this.nome = nome;
    }

    @Override
    public void conectar() {
        if (conexoesAtivas < LIMITE_CONEXOES) {
            conexaoReal = new ConexaoReal(nome);
            conexaoReal.conectar();
            conexoes.add(conexaoReal);
            conexoesAtivas++;
        } else {
            System.out.println(nome + " não pôde conectar: limite de conexões atingido.");
        }
    }

    @Override
    public void desconectar() {
        if (conexaoReal != null) {
            conexaoReal.desconectar();
            conexoes.remove(conexaoReal);
            conexoesAtivas--;
        }
    }
}
