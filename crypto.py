import random
import math
import sys
from fractions import gcd

"""Return True if n is prime
"""
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % ii for ii in range(3, int(math.sqrt(n)) + 1, 2))

"""This use the Diffie Hellman Protocol to share a secret key
G is (n, o) such that g generates a group of order o in Z/nZ
"""
class DH(object):
    
    def __init__(self, G = (0,0), g = 0):
        if G == (0,0) or g == 0:
            self.GenerateGroup()
        else:
            self.G, self.g = G, g
        
    """Generates a cyclic group G and a generator g of this group
    """
    def GenerateGroup(self):
        # we generate a new group
        mod = 4
        while not is_prime(mod):
            mod = random.randint(5, 1000000)
            
        while True:
            # we generate a random element 'g' prime to mod
            g = random.randint(2, mod)
            #if gcd(g, mod) != 1: continue
            #this line is useless since we use a prime for modulo

            test = g**2 % mod
            order = 2

            # we get the order of g
            while test != 1:
                test = (test * g) % mod
                order += 1

            if test == 1: break

        self.G, self.g = (mod, order), g

    def GenerateSecret(self):
        self.__privatekey = random.randint(2,10000)

    def GeneratePublic(self):
        self.publickey = (self.g ** self.__privatekey) % self.G[0]

    def GenerateSharedkey(self, publickey):
        self.__sharedkey = (publickey ** self.__privatekey) % self.G[0]


"""Testing Diffie Hellman
"""
# 1. BOB
bob = DH()
# G and g are generated automatically
print("G is a group mod %i and of order %i, and the generator g is %i" % (bob.G[0], bob.G[1], bob.g))
# we generate a secret and a public key
bob.GenerateSecret()
bob.GeneratePublic()

# 2. ALICE
# We already know G and g
alice = DH(bob.G, bob.g)
# We generate the secret key and the public key
alice.GenerateSecret()
alice.GeneratePublic()

# 3. WE CREATE THE SHARED KEY
bob.GenerateSharedkey(alice.publickey)
alice.GenerateSharedkey(bob.publickey)

# 4. Bob and Alice now have the same __sharedkey and the same public (G, g)


