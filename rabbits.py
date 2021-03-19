import random


class RabbitMale():
    def __init__(self):
        self.gender = 'male'
        self.age = 2
        self.love = random.randint(1,10)


class RabbitFemale():
    def __init__(self):
        self.gender = 'female'
        self.age = 2
        self.love = random.randint(1,10)
    
    def reproduce(self,other):
        if other.gender == 'male' and other.age > 1:
            Babies = None
            while not Babies:
                self.love = random.randint(1,10)
                if other.love == self.love: 
                    Babies = (RabbitMale(),RabbitFemale())
                    return Babies
        else:
            raise ValueError




"""


"""


if __name__ == "__main__":
    Bol2 = RabbitMale()
    Witje2 = RabbitFemale()
    babies = Witje2.reproduce(Bol2)
    print(babies)
