#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''# python Interface/Abstractclass 写法 1：NotImplementedError  '''

class QuackBehavior(object):
    def quack(self):  # 不建议用这种方式：不用装饰器，而用raise。子类不实现，就会调用引发 Error。
        raise NotImplementedError()
class Quack(QuackBehavior):
    def quack(self):
        print("quack...")
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<<silence>>")
class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak...")

'''
python Interface/Abstractclass 写法 2： ABCMeta + @abstractmethod   ##############
py2 / py3 语法不同，所以要采取特殊写法
# python 2 的 ABCMeta 写法
class FlyBehavior(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def fly(self): pass
# python 3 的 ABCMeta 写法
class QuackBehavior(object, metaclass=ABCMeta):
    @abstractmethod
    def quack(self): pass
'''

from abc import ABCMeta, abstractmethod
ABC = ABCMeta(u'ABC', (object,), {})  # 跨越 py2 / py3 的写法
class FlyBehavior(ABC):
    @classmethod   # 如果必须运行某些方法，使用 @classmethod
    def version(cls): return "1.0"
    @abstractmethod # 子类如果不实现这个接口，实例化子类时 就会报错
    def fly(self): pass
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying...")
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I am flying with rocket power!")


class Duck(ABC):
    def __init__(self):
        self.quackBehavior = QuackBehavior()
        self.flyBehavior = FlyBehavior()
    @abstractmethod
    def display(self): pass  # 不能直接调用这个方法，而必须由子类覆盖
    def performQuack(self):
        self.quackBehavior.quack()
    def performFly(self):
        self.flyBehavior.fly()
    def setFlyBehavior(self, fly):
    # def setFlyBehavior(self, fly: FlyBehavior):
        # 接口还可以校验
        if not isinstance(fly, FlyBehavior):
            raise Exception('接口类型 错误')
        # FlyBehavior的  @classmethod def version(self): return "1.0"
        # 在这里得到了应用
        if not FlyBehavior.version() == '1.0':
            raise Exception('接口版本 错误')
        self.flyBehavior = fly
    def setQuackBehavior(self, quack):
    # def setQuackBehavior(self, quack: QuackBehavior):
        self.quackBehavior = quack
    def swim(self):
        print("All ducks float")
class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack() # 因为Python中一切都是对象，所以可以写的更简略。
        self.flyBehavior = FlyWithWings()
    def display(self):
        print("MallardDuck")
class ModelDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyNoWay()
    def display(self):
        print("ModelDuck")

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()

    model = ModelDuck()
    model.display()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()
