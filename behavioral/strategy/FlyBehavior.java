public interface FlyBehavior {
    public void fly();
}
class FlyWithWings implements FlyBehavior {
    public void fly() { System.out.println("Flying...");  }
}
class FlyNoWay implements FlyBehavior {
    public void fly() { System.out.println("I can't fly");  }
}

class FlyRocketPowered implements FlyBehavior {
    public void fly() {
        System.out.println("I am flying with rocket power!");
    }
}
