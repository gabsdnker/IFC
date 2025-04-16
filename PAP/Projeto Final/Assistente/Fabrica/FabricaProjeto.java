package Fabrica;

import Modelo.Projeto;

public class FabricaProjeto {
    public static Projeto criarProjeto(String nome) {
        return new Projeto(nome);
    }
}
