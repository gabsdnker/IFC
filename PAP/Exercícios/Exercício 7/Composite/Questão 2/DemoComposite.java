public class DemoComposite {
    public static void main(String[] args) {
        // Criando objetos Empregado
        Empregado ceo = new Empregado("Ana", "Diretoria", 10000);
        Empregado gerenteTI = new Empregado("Bruno", "TI", 8000);
        Empregado dev1 = new Empregado("Carlos", "TI", 5000);
        Empregado dev2 = new Empregado("Diana", "TI", 5000);
        Empregado gerenteRH = new Empregado("Elisa", "RH", 7500);
        Empregado rh1 = new Empregado("Fábio", "RH", 4000);

        // Montando a hierarquia
        ceo.adicionar(gerenteTI);
        ceo.adicionar(gerenteRH);

        gerenteTI.adicionar(dev1);
        gerenteTI.adicionar(dev2);

        gerenteRH.adicionar(rh1);

        // Exibindo a hierarquia
        exibirHierarquia(ceo, 0);
    }

    public static void exibirHierarquia(Empregado emp, int nivel) {
        String prefixo = "  ".repeat(nivel);
        System.out.println(prefixo + emp.toString());
        for (Empregado subordinado : emp.getSubordinados()) {
            exibirHierarquia(subordinado, nivel + 1);
        }
    }
}
