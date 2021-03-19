import random
import numpy as np
import time

#############################################################
### Intro 
#############################################################

# Objects
# Classes 

# mylist = [1,2,3]
# 
# def func():
#     res = []
#     for idx, x in enumerate(mylist):
#         x = x+1
#         mylist[idx] = x
#     print(mylist)
# 
# def add(x=2,y=2,bias=1):
#     return x+y+bias
# 
# # 
# func()
# print(mylist)
# 
# res = add()
# print(res)
# 
# If statements 
# x = ["geel","groen","rood"]
# 
# d = {"appel":10,"kers":100,"banaan":2500}
# 
# for key, value in d.items():
#     print(key, value)



# For loop 
# While loop 



#############################################################
### Intro 
#############################################################

"""
Explore programming!

(1) 1 rabbit pair produces one ofspring every timestep
(2) rabbits start repoducing after 1 one month


(a) Rabbit
    - logging 
    - global parameter / function 
    - enforces constraints on the subclasses

(b) Create subclass RabbitMale RabbitFemale 
    - implements repoduction 
    - local properties 

"""

F = [1,1]
for _ in range(10):
    F.append(sum(F[-2:]))

print(F)

class RabbitMale:
    def __init__(self):
        self.love = random.randint(1,10)
        self.age = 1


class RabbitFemale:
    def __init__(self):
        self.love = random.randint(1,10)
        self.age = 1

    def __add__(self,other):
        if self.love == other.love:
#             print('we made baby rabbits!!')
            Babies = (RabbitMale(), RabbitFemale())
        else:
            Babies = None
        return Babies

BunBun = RabbitMale()
Coco = RabbitFemale()

Babies = None
while not Babies:
    Babies = Coco + BunBun
    print("Coco and BunBun are having fun!")
    Coco.love=random.randint(1,10)
    time.sleep(.1)

print("Two new Baby rabbits were born!")
print(Babies)

# 
# 
# 
