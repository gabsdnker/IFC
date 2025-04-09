import java.util.EnumSet;

enum Size {
    SMALL(0), MEDIUM(1), LARGE(2);
    
    private final int value;

    Size(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

abstract class Beverage {
    protected Size size;
    protected String description;
    protected int dosesOfCoffee;

    public Beverage() {
        this.size = Size.SMALL;
        this.description = "Unknown Beverage";
        this.dosesOfCoffee = 1;
    }

    public void setSize(Size size) {
        this.size = size;
    }

    public Size getSize() {
        return size;
    }

    public void setDosesOfCoffee(int doses) {
        this.dosesOfCoffee = doses;
    }

    public int getDosesOfCoffee() {
        return dosesOfCoffee;
    }

    public String getDescription() {
        return description;
    }

    public abstract double cost();
}

class Espresso extends Beverage {
    public Espresso() {
        description = "Espresso";
    }

    @Override
    public double cost() {
        return 1.99;
    }
}

class HouseBlend extends Beverage {
    public HouseBlend() {
        description = "House Blend Coffee";
    }

    @Override
    public double cost() {
        return 0.89;
    }
}

abstract class CondimentDecorator extends Beverage {
    public abstract String getDescription();
}

class Milk extends CondimentDecorator {
    private Beverage beverage;

    public Milk(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public double cost() {
        double cost = beverage.cost();
        switch (beverage.getSize()) {
            case SMALL:
                cost += 0.10;
                break;
            case MEDIUM:
                cost += 0.15;
                break;
            case LARGE:
                cost += 0.20;
                break;
        }
        return cost;
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Milk";
    }
}

class Soy extends CondimentDecorator {
    private Beverage beverage;

    public Soy(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public double cost() {
        double cost = beverage.cost();
        switch (beverage.getSize()) {
            case SMALL:
                cost += 0.10;
                break;
            case MEDIUM:
                cost += 0.15;
                break;
            case LARGE:
                cost += 0.20;
                break;
        }
        return cost;
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Soy";
    }
}

class Mocha extends CondimentDecorator {
    private Beverage beverage;
    private int doses;

    public Mocha(Beverage beverage, int doses) {
        this.beverage = beverage;
        this.doses = doses;
    }

    @Override
    public double cost() {
        return 0.20 * doses + beverage.cost();
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + String.format(", Mocha (%d doses)", doses);
    }
}

class Whip extends CondimentDecorator {
    private Beverage beverage;

    public Whip(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public double cost() {
        double cost = beverage.cost();
        switch (beverage.getSize()) {
            case SMALL:
                cost += 0.10;
                break;
            case MEDIUM:
                cost += 0.15;
                break;
            case LARGE:
                cost += 0.20;
                break;
        }
        return cost;
    }

    @Override
    public String getDescription() {
        return beverage.getDescription() + ", Whip";
    }
}

public class CoffeeShop2 {
    public static void main(String[] args) {
        Beverage beverage = new Espresso();
        beverage.setSize(Size.SMALL);
        beverage.setDosesOfCoffee(2);
        System.out.println(beverage.getDescription() + " $ " + beverage.cost());

        Beverage beverage2 = new HouseBlend();
        beverage2.setSize(Size.MEDIUM);
        beverage2.setDosesOfCoffee(3);
        beverage2 = new Milk(beverage2);
        beverage2 = new Mocha(beverage2, 2);
        beverage2 = new Whip(beverage2);
        System.out.println(beverage2.getDescription() + " $ " + beverage2.cost());
    }
}

