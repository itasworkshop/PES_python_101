
class Computer:

    price  = 50000
    company = "HP"

    def myInfo(self):
        print("This computer is ",self.price,self.company)

    def playMusic(self):
        print("Music is getting played...")

"""object creation"""
computer = Computer()
"""calling object methods"""
computer.myInfo()
computer.playMusic()