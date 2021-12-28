import math
import random
import numpy as np
from io import StringIO
import random

def main():

    favourite1 = "dogs"
    favourite2 = "cats"
    favourite3 = "bats" 
    prob1 = 0.8
    prob2 = 0.9
    a = random.random()
    if a < prob1:
        print("I love " + favourite1)
    elif a < prob2:
        print("I love " + favourite2)
    else:
        print("I love " + favourite3)

main()
