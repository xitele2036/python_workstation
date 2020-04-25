#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

class Animal(object):

    def run(self):
        print("Animal is running....")

class Cat(Animal):

    def mao(self):
        print("猫")

class Dog(Animal):

    def quan(self):
        print("犬")

dog = Dog()
dog.quan()
dog.run()
i = isinstance(dog,Dog)
d = dir(dog)
print(d)