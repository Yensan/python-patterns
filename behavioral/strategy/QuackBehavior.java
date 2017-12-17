public interface QuackBehavior {
    public void quack();
}
class Quack implements QuackBehavior {
    public void quack() { System.out.println("quack...");  }
}
class MuteQuack implements QuackBehavior {
    public void quack() { System.out.println("<<silence>>");  }
}
class Squeak implements QuackBehavior {
    public void quack() { System.out.println("Squeak...");  }
}
