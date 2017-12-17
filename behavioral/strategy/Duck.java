
public abstract class Duck {
    QuackBehavior quackBehavior;
    FlyBehavior flyBehavior;
    public Duck() {}
    public abstract void display();
    public void performQuack() {
        quackBehavior.quack();
    }
    public void performFly() {
        flyBehavior.fly();
    }
    public void setFlyBehavior(FlyBehavior fly) {
        this.flyBehavior = fly;
    }
    public void setQuackBehavior(QuackBehavior quack) {
        this.quackBehavior = quack;
    }
    public void swim() {
        System.out.println("All ducks float");
    };

}


class MallardDuck extends Duck{
    public MallardDuck () {
        quackBehavior = new Quack();
        flyBehavior = new FlyWithWings();
    }

    public void display() {
        System.out.println("MallardDuck"); // 真的鸭子，绿头鸭
    };
}

class RedheadDuck {
    public void display() {};
}

class ModelDuck extends Duck {
    public ModelDuck() {
        flyBehavior = new FlyNoWay();
        quackBehavior = new Quack();
    }
    public void display() {
        System.out.println("ModelDuck");
    };
}
