import java.util.ArrayList;
import java.util.List;

class Empregado {
    private String nome;
    private String departamento;
    private int salario;
    private List<Empregado> subordinados;

    public Empregado(String nome, String departamento, int salario) {
        this.nome = nome;
        this.departamento = departamento;
        this.salario = salario;
        this.subordinados = new ArrayList<>();
    }

    public void adicionar(Empregado empregado) {
        subordinados.add(empregado);
    }

    public void remover(Empregado empregado) {
        subordinados.remove(empregado);
    }

    public List<Empregado> getSubordinados() {
        return subordinados;
    }

    @Override
    public String toString() {
        return "Empregado: " + nome + ", Departamento: " + departamento + ", Salário: R$" + salario;
    }
}