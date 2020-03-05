class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return 'student name: %s, score: %s' % (self.name, self.score)

    __repr__ = __str__

    def printscore(self):
        print(self.score)

    def __call__(self, *args, **kwargs):
        print('my name is %s.' % self.name)


bart = Student("bart", 23)
print(bart.name)
print(bart.score)
bart.printscore()
print('=====================')


class Animal(object):
    def __init__(self):
        pass

    def __len__(self):
        return 10

    def run(self):
        print("animal is running.")


class Dog(Animal):
    def run(self):
        print("dog is running")


class Cat(Animal):
    def run(self):
        print('cat is running.')


class Time(object):
    def run(self):
        print('timer is started')


def tract(animal):
    animal.run()


a = Animal()
b = Dog()
c = Cat()
t = Time()
tract(a)
tract(b)
tract(c)
tract(t)

print(len(a))
print(len(b))


class StudentWithProp(object):
    @property
    def birth(self):
        return self._birth

    @property
    def age(self):
        return 2015 - self._birth

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     self._name = value
    #
    # @birth.setter
    # def birth(self, value):
    #     self._birth = value


print('===========================')
s2 = Student('weiss', 20)
print(s2)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users.id.list)
print(Chain().users.repos)
print(s2())
print(callable(s2))
print(callable('123'))

print('=================')
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name,member in Weekday.__members__.items():
    print(name,'==>',member)
print(Weekday(1))
