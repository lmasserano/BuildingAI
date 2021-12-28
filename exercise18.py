import math
import random
import numpy as np
from io import StringIO
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i,j] =  np.inf
            else:
                dist[i,j] = np.sqrt(sum([(a-b)**2 for a, b in zip(data[i],data[j])]))
    print(np.unravel_index(np.argmin(dist), dist.shape))

def main(text):
    # Write your function here
    bag = text.split()
    line = text.split("\n")
    bag_unique = []
    for i in bag:
        if i not in bag_unique:
            bag_unique.append(i)
    N = len(bag_unique)
    n = len(line)
    data_text = np.zeros((n, N), dtype = int)
    for i in line:
        word = i.split()
        for j in word:
            data_text[line.index(i),bag_unique.index(j)] += 1
    find_nearest_pair(data_text)

main(text)
