import random
import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# DIFFIE HELLMAN

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
        # I don't know how to do that... So I'm just gonna pick p+1 groups as I know that groups of order p are primes. So Z/12Z should work for example
        G = random.randint(1, 10000)
        if is_prime(G - 1):
            print(G)
            while True:
                g = random.randint(2, G - 1)
                print(g)
                test = g**2
                ii = 2
                while test != 1:
                    test *= g
                    ii += 1
                if ii == G: break
        self.G, self.g = G, g

test = DH()
print(test.G, test.g)

# RSA

# ELGAMAL
