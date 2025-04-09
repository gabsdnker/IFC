import java.util.ArrayList;
import java.util.List;

public class Categoria implements ItemCatalago{  
    private String nome;
    private List<ItemCatalago> itens = new ArrayList<>();

    public Categoria(String nome){  
        this.nome = nome;
    }

    public void adicionarItem(ItemCatalago item){
        itens.add(item);
    }

    public void removerItem(ItemCatalago item){
        itens.remove(item);
    }

    @Override
    public void exibirDetalhes(String prefixo){
        System.out.println(prefixo + " + " + nome);
        for(ItemCatalago item : itens){
            item.exibirDetalhes(prefixo + " ");
        }
    }
}