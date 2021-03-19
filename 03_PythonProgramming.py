import random 
import time 
import numpy as np 

from rabbits import RabbitMale, RabbitFemale, Population

# Exercise 1 

Bol = RabbitMale()
Witje = RabbitFemale()
babies = Witje.reproduce(Bol)


# Exercise 2 

"""
1) Population of rabbits that reproduces on each iteration 
    - Pop of females 
    - Pop of Males 
2) Each female chooses a mate and then makes minis with him
    - if her age is larger then 1 
3) Increases it's age by one
4) Then we print out the population count
"""

"""
Population
Attribute
- males (list) 
- females (list)

functions 
- if #males == #females
- if age > 1 and gender == males / 
- choose random mate 
- run reproduce 
- append babies 

- count 

"""

pop.reproduce(10)



