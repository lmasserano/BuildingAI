import math
import random
import numpy as np
from io import StringIO
import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    count = 0
    count1 = 0
    for i in seq:
        if i:
            count1 = count1 + 1
        else:
            count1 = 0
        if count1 == 5:
            count = count + 1
            count1 = count1 - 1
    return count

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
