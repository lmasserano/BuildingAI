
import math
import random
import numpy as np
from io import StringIO
import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False
    right = 1

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if right:
            for i in range (1,min(6,99-x)):
                if h[x + i] > h[x]:
                    x = x + 1         # right is higher, go there
                    summit = False    # and keep going
        if summit:
            for i in range (1,min(6,x)):    
                if h[x - i] > h[x]:
                    x = x - 1         # left is higher, go there
                    summit = False    # and keep going
                    right = 0
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
