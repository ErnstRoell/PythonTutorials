import random
import time 
import numpy as np
class RabbitMale:
    def __init__(self):
        self.love = random.randint(1,10)
        self.age = 1

class RabbitFemale:
    def __init__(self):
        self.love = random.randint(1,10)
        self.age = 1

Coco = RabbitMale()
BunBun = RabbitFemale()

Babies = None
while not Babies:
    time.sleep(1)
    BunBun.love=random.randint(1,10)
    if BunBun.love == Coco.love:
        print('We made Baby Rabbits')
        Babies = (RabbitMale(),RabbitFemale())
    else:
        print("BunBun is angry at me :(")


    
