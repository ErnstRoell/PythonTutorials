import random 
import time 
import numpy as np 

from rabbits import RabbitMale, RabbitFemale

'''
1) Twee hazen (object) 
2) Maak een functie om voortplanten
3) In een functie zetten  
'''

Bol = RabbitMale()
Witje = RabbitFemale()

Babies = None
while not Babies:
    Bol.love = random.randint(1,10)
    if Bol.love == Witje.love: 
        print('Wij hebben kleintjes gemaakt!')
        Babies = (RabbitMale(),RabbitFemale())
    else: 
        print('Not yet')


