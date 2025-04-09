// Interface para comportamento de voo
interface FlyBehavior {
    void fly();
}

// Implementações de voo
class FlyWithWings implements FlyBehavior {
    public void fly() {
        System.out.println("Voando com asas!");
    }
}

class FlyNoWay implements FlyBehavior {
    public void fly() {
        System.out.println("Não posso voar.");
    }
}

// Interface para comportamento de grasnido
interface QuackBehavior {
    void quack();
}

// Implementações de grasnido
class Quack implements QuackBehavior {
    public void quack() {
        System.out.println("Quack! Quack!");
    }
}

class Squeak implements QuackBehavior {
    public void quack() {
        System.out.println("Som de brinquedo de borracha!");
    }
}

class MuteQuack implements QuackBehavior {
    public void quack() {
        System.out.println("...");
    }
}

// Classe abstrata Duck
abstract class Duck {
    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    public void performFly() {
        flyBehavior.fly();
    }

    public void performQuack() {
        quackBehavior.quack();
    }

    public void setFlyBehavior(FlyBehavior fb) {
        flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb) {
        quackBehavior = qb;
    }

    public void swim() {
        System.out.println("Todos os patos nadam, até os de brinquedo!");
    }

    public abstract void display();
}

// Diferentes tipos de patos
class MallardDuck extends Duck {
    public MallardDuck() {
        flyBehavior = new FlyWithWings();
        quackBehavior = new Quack();
    }
    public void display() {
        System.out.println("Eu sou um pato Mallard!");
    }
}

class RedheadDuck extends Duck {
    public RedheadDuck() {
        flyBehavior = new FlyWithWings();
        quackBehavior = new Quack();
    }
    public void display() {
        System.out.println("Eu sou um pato de cabeça vermelha!");
    }
}

class RubberDuck extends Duck {
    public RubberDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Squeak();
    }
    public void display() {
        System.out.println("Eu sou um pato de borracha!");
    }
}

class DecoyDuck extends Duck {
    public DecoyDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new MuteQuack();
    }
    public void display() {
        System.out.println("Eu sou um pato de madeira!");
    }
}

// Classe principal para testar o simulador
public class DuckSimulator {
    public static void main(String[] args) {
        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.performQuack();
        mallard.performFly();
        
        System.out.println("\nMudando o comportamento de voo do pato Mallard...");
        mallard.setFlyBehavior(new FlyNoWay());
        mallard.performFly();
    }
}
