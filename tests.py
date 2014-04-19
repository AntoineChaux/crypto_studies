from crypto import DiffieHellman, ElGamal, RSA

"""Testing Diffie Hellman
"""
# 1. BOB
bob = DiffieHellman()
# G and g are generated automatically
print("G is a group mod %i and of order %i, and the generator g is %i" % (bob.G[0], bob.G[1], bob.g))
# We generate a secret and a public key
bob.generate_secret()
bob.generate_public()

# 2. ALICE
# We already know G and g
alice = DiffieHellman(bob.G, bob.g)
# We generate the secret key and the public key
alice.generate_secret()
alice.generate_public()

# 3. WE CREATE THE SHARED KEY
bob.generate_sharedkey(alice.publickey)
alice.generate_sharedkey(bob.publickey)
# Bob and Alice now have the same _sharedkey and the same public (G, g)


"""Testing ElGamal Encryption
"""
# 1. BOB
bob = ElGamal()
bob.generate_secret()
bob.generate_public()

# 2. ALICE
alice = ElGamal(bob.G, bob.g)
alice.generate_secret()
alice.generate_public()

# 3. WE CREATE THE SHARED KEY
bob.generate_sharedkey(alice.publickey)
alice.generate_sharedkey(bob.publickey)

# 4. WE TRY TO ENCRYPT ONE MESSAGE
encrypted = bob.encrypt(56)
print("we are encrypting the number '56' -> %i" % encrypted)

# 5. WE SEND IT TO ALICE
message = alice.decrypt(encrypted)
print("we are decrypting the code '%i' -> %i" % (encrypted, message))
