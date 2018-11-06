#funzione del calcolo del volume di una sfera

import math


def sfera(r): 
    Volume= (r**3*math.pi*4./3.)
    return Volume

r = input('Quanto vale il raggio?  ')
r = int(r)
print (sfera(r))






