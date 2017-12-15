#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.

*TL;DR80
Enables selecting an algorithm at runtime.
"""

# Strategy Pattern 的核心：将 变化 与 不变 的代码分离。
# Python 一切都是对象，不需要 JAVA 的繁重设计。不变的部分放在继承树；变化的部分做成一堆函数，动态加载，随时切换。
# 方法：每次调用，自动传入实例self。所以，将一个函数 变为 方法，需要接收self。这里使用装饰器语法

from typing import Callable
from types import MethodType

# 用法 1： self.quackBehavior = MethodType(quackf, self)
def regist_func_to_class(func):  # 如果被注册为类的属性，调用时，必然会传入self
    def wraper(self, *args):     # 使用装饰器语法，屏蔽self，仅仅调用函数
        result = func(*args)
        return result
    return wraper

# 如果这些函数不需要重用，那么@decorator就可以了
@regist_func_to_class
def quack(): print("quack...")
@regist_func_to_class
def muteQuack(): print("<<silence>>")
# 如果这些函数需要被别的模块使用，那么就 func = decorator(func)
def squeak(): print("Squeak...")
squeak = regist_func_to_class(squeak)  # 装饰步骤放在类中，就不会影响 其他模块导入这个函数


# 用法 2： self.flyBehavior = flyf 就不需要复杂的处理，直接当做函数使用
def flyWithWings():
    print("Flying...")
def flyNoWay():
    print("I can't fly")
def flyRocketPowered():
    print("I am flying with rocket power!")


from abc import ABCMeta, abstractmethod
ABC = ABCMeta(u'ABC', (object,), {})
class Duck(ABC):
    def __init__(self, flyf: Callable[[], None], quackf: Callable[[], None]):
        if isinstance(flyf, Callable) and isinstance(quackf, Callable):
            self.quackBehavior = MethodType(quackf, self)
            self.flyBehavior = flyf
    @abstractmethod
    def display(self): pass
    def performQuack(self):
        self.quackBehavior()
    def performFly(self):
        self.flyBehavior()
    def setFlyBehavior(self, flyf: Callable):
        if flyf is not None:
            self.flyBehavior = flyf
    def setQuackBehavior(self, quackf: Callable):
        if quackf is not None:
            self.quackBehavior = MethodType(quackf, self)
    def swim(self):
        print("All ducks float")
class MallardDuck(Duck):
    def __init__(self, flyf: Callable=flyWithWings, quackf: Callable=quack):
        super(MallardDuck, self).__init__(flyf, quackf)
    def display(self):
        print("MallardDuck")
class ModelDuck(Duck):
    def __init__(self, flyf: Callable=flyNoWay, quackf: Callable=quack):
        super(ModelDuck, self).__init__(flyf, quackf)
    def display(self):
        print("ModelDuck")

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()
    if isinstance(mallard, Callable):
        pass
    model = ModelDuck()
    model.display()
    model.performFly()
    model.setFlyBehavior(flyRocketPowered)
    model.performFly()
