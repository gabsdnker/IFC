public class MenuRestaurante{
    public static void main(String[] args){
        // Bebidas
        Produto cocacola = new Produto("Coca-cola 2L", 14.00);  // Corrigido para "Produto"
        Produto pepsi = new Produto("Pepsi 2L", 12.00);  // Corrigido para "Produto"
        Produto sucoNatural = new Produto("Suco Natural", 10.00);  // Corrigido para "Produto"

        // Pratos principais
        Produto lasanha = new Produto("Lasanha", 25.00);  // Corrigido para "Produto"
        Produto bifeComFritas = new Produto("Bife com fritas", 28.00);  // Corrigido para "Produto"
        Produto parmegiana = new Produto("Parmegiana", 30.00);  // Corrigido para "Produto"

        // Sobremesas 
        Produto pudim = new Produto("Pudim", 10.00);  // Corrigido para "Produto"
        Produto sorvete = new Produto("Sorvete", 8.50);  // Corrigido para "Produto"
        Produto acai = new Produto("Açaí", 12.00);  // Corrigido para "Produto"

        // Categorias
        Categoria bebidas = new Categoria("Bebidas");  // Corrigido para "Categoria"
        bebidas.adicionarItem(cocacola);
        bebidas.adicionarItem(pepsi);
        bebidas.adicionarItem(sucoNatural);

        Categoria pratosPrincipais = new Categoria("Pratos Principais");  // Corrigido para "Categoria"
        pratosPrincipais.adicionarItem(lasanha);
        pratosPrincipais.adicionarItem(bifeComFritas);
        pratosPrincipais.adicionarItem(parmegiana);

        Categoria sobremesas = new Categoria("Sobremesas");  // Corrigido para "Categoria"
        sobremesas.adicionarItem(pudim);
        sobremesas.adicionarItem(sorvete);
        sobremesas.adicionarItem(acai);

        Categoria menu = new Categoria("Menu Restaurante");  // Corrigido para "Categoria"
        menu.adicionarItem(bebidas);
        menu.adicionarItem(pratosPrincipais);
        menu.adicionarItem(sobremesas);

        menu.exibirDetalhes("");
    }
}
