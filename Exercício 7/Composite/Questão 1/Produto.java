import java.util.ArrayList;
import java.util.List;
public class Produto implements ItemCatalago{  
    private String nome;
    private double preco;

    public Produto(String nome, double preco){  
        this.nome = nome;
        this.preco = preco;
    }

    @Override
    public void exibirDetalhes(String prefixo){
        System.out.println(prefixo + "- " + nome + " (R$ " + preco + ")");
    }
}