import math
import random
from io import StringIO
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # write the recursive function here
    # remember to print out the route as the recursion ends
    a = len(ports)
    if a > 1:
        for i in ports:
            route.append(i)
            ports_a=ports.copy()
            ports_a.remove(i)
            permutations(route, ports_a)
            route.remove(i)
    else:
        route = route + ports
        print(' '.join([portnames[i] for i in route]))

# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
