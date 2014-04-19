import random
import math
import sys
from fractions import gcd

"""Return True if n is prime
"""
def is_prime(n):
    if n < 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % ii for ii in range(3, int(math.sqrt(n)) + 1, 2))

"""This use the Diffie Hellman Protocol to share a secret key
G is (n, o) such that g generates a group of order o in Z/nZ
"""
class DiffieHellman(object):

    publickey = 0
    _privatekey = 0
    _sharedkey = 0
    
    def __init__(self, G = (0,0), g = 0):
        if G == (0,0) or g == 0:
            self.generate_group()
        else:
            self.G, self.g = G, g
        
    """Generates a cyclic group G and a generator g of this group
    """
    def generate_group(self):
        # we generate a new group
        mod = 0
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
        return self.G, self.g

    def generate_secret(self):
        self._privatekey = random.randint(2,10000)

    def generate_public(self):
        if self._privatekey == 0:
            return False
        self.publickey = (self.g ** self._privatekey) % self.G[0]
        return True

    def generate_sharedkey(self, publickey):
        if self._privatekey == 0:
            return False
        self._sharedkey = (publickey ** self._privatekey) % self.G[0]
        return True


"""ElGamal Encryption
"""
class ElGamal(DiffieHellman):

    _sharedkey_inverse = 0

    def encrypt(self, message):
        if self._sharedkey == 0:
            return False
        encrypted = (message * self._sharedkey) % self.G[0]
        return encrypted

    def decrypt(self, encrypted):
        if self._sharedkey_inverse == 0:
            self.generate_sharedkey_inverse()
        message = encrypted * self._sharedkey_inverse % self.G[0]
        return message

    def generate_sharedkey_inverse(self):
        inverse = 2
        test = self._sharedkey * inverse % self.G[0]
        while test != 1:
            inverse += 1
            test = self._sharedkey * inverse % self.G[0]
        self._sharedkey_inverse = inverse


"""RSA Encryption
"""
class RSA(object):
        
    def generate_publickey(self):
        p, q = 0
        
        while not is_prime(p):
            p = random.randint(2, 100000)
        while not is_prime(q):
            q = random.randint(2, 100000)
                        
    
