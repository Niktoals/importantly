#                                           ООП

#   №! Наследование
'''class Human:
    def __init__(self, name):
        self.name=name

    def say_hello(self):
        print("Hello I'm {}".format(self.name))

#human_1=Human(name='Nikita')
#human_1.say_hello()

class Human_2(Human):
    def __init__(self, name, age):
        super().__init__(name)
        self.age=age
    def say_hello(self):
        print("Hello I'm {} and I'm {}".format(self.name, self.age))

#human_2=Human_2(name='Andrey', age=16)
#human_2.say_hello()


class A:
    def __init__(self):
        self.a=10
        self.f=50

class B:
    def __init__(self):
        self.b=5

class C(A, B):
    def __init__(self, a, b, f):
        A.__init__(self)
        B.__init__(self)
        self.a=a
        self.b=b
        self.f=f

    def ret(self):
        print(self.b+self.f+self.a)

    @staticmethod 
    def predict():
        print('a+b+f=65')

#c=C(a=20, b=30, f=10)
#C.predict()
#c.ret()'''