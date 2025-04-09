import java.util.ArrayList;
import java.util.List;

interface StockObserver {
    void update(String product, int quantity);
}

interface StockSubject {
    void addObserver(StockObserver observer);
    void removeObserver(StockObserver observer);
    void notifyObservers();
}

class Product implements StockSubject {
    private List<StockObserver> observers = new ArrayList<>();
    private String name;
    private int quantity;

    public Product(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }

    public void addObserver(StockObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(StockObserver observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (StockObserver observer : observers) {
            observer.update(name, quantity);
        }
    }

    public void sellItem() {
        if (quantity > 0) {
            quantity--;
            System.out.println("\n[Loja] Produto vendido: " + name + " | Estoque restante: " + quantity);
            if (quantity <= 3) { // Quando o estoque chega a 3 ou menos, avisa os interessados
                notifyObservers();
            }
        } else {
            System.out.println("\n[Loja] Produto esgotado: " + name);
        }
    }
}

// Observador - Cliente
class Customer implements StockObserver {
    private String name;

    public Customer(String name) {
        this.name = name;
    }

    @Override
    public void update(String product, int quantity) {
        System.out.println("[Cliente " + name + "] Alerta! O estoque de " + product + " está baixo (" + quantity + " restantes). Compre logo!");
    }
}

// Observador - Gerente
class Manager implements StockObserver {
    @Override
    public void update(String product, int quantity) {
        System.out.println("[Gerente] Atenção! O estoque de " + product + " está baixo. Avaliar necessidade de reposição.");
    }
}

// Observador - Sistema de Reposição
class RestockSystem implements StockObserver {
    @Override
    public void update(String product, int quantity) {
        System.out.println("[Sistema de Reposição] Ordem de compra gerada para o produto: " + product);
    }
}

public class StockObserverExample {
    public static void main(String[] args) {
        Product laptop = new Product("Laptop Gamer", 5);
        
        Customer cliente1 = new Customer("Ricardo");
        Customer cliente2 = new Customer("Ana");
        Manager gerente = new Manager();
        RestockSystem sistemaReposicao = new RestockSystem();

        laptop.addObserver(cliente1);
        laptop.addObserver(cliente2);
        laptop.addObserver(gerente);
        laptop.addObserver(sistemaReposicao);

        // Simulando vendas
        laptop.sellItem();
        laptop.sellItem();
        laptop.sellItem();
        laptop.sellItem();
    }
}
