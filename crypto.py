import random
import math

"""Return True if n is prime
"""
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % ii for ii in range(3, int(math.sqrt(n)) + 1, 2))

"""This use the Diffie Hellman Protocol to share a secret key
"""
class DH(object):
    
    def __init__(self, G = 0, g = 0):
        if G == 0 or g == 0:
            self.GenerateGroup()
        else:
            self.G, self.g = G, g
        
    """Generates a cyclic group G and a generator g of this group
    """
    def GenerateGroup(self):
        mod = 0
        
        while not is_prime(mod - 1):
            mod = random.randint(1, 10000)
            
        while True:
            g = random.randint(2, mod - 1)
            test = g**2
            order = 2
            while test != 1:
                test *= g
                order += 1
            if order == mod - 1: break

        self.G, self.g = (mod, order), g

test = DH()
print(test.G, test.g)

