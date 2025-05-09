package Fabrica;

import Modelo.Projeto;

public class FabricaProjeto {
    // Método para criar um projeto
    // Este método é responsável por criar um novo projeto com o nome fornecido
    // e inicializa a lista de projetos
    public static Projeto criarProjeto(String nome) {
        return new Projeto(nome);
    }
}
