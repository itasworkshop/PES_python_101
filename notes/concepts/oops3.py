
class Computer:

    def __init__(self,price,company):
       print("hello from init")
       self.price = price
       self.company = company

    def myInfo(self):
        print("This computer is ",self.price,self.company)

    def playMusic(self):
        print("Music is getting played...")


computer1 = Computer(45000,"HP")
computer1.myInfo()
computer1.playMusic()

computer2 = Computer(67000,"DELL")
computer2.myInfo()
computer2.playMusic()

