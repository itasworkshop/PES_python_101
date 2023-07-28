"""Inheritance in python"""

class Computer:

    def __init__(self,price,company):
       print("hello from init")
       self.price = price
       self.company = company

    def myInfo(self):
        print("This computer is ",self.price,self.company)

    def playMusic(self):
        print("Music is getting played...")

class Laptop(Computer):

    def __init__(self,price,company,touchpad):
        super().__init__(price,company)
        self.touchpad = touchpad

    def laptopInfo(self):
        print("This is laptop info",self.price,self.company,self.touchpad)


laptop1 = Laptop(45000,"HP","mini")
laptop1.laptopInfo()
laptop1.playMusic()


