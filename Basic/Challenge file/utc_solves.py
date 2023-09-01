import random
from pwn import *

#Connexion au serveur
r = remote('54.37.70.250', 1873)
recept=r.recv()
recept=recept.decode()
print(recept)
print('envoi de du choix "e" ...')
r.sendline('e'.encode())

# Récupération du time
t = int(time.time())

#Récupération du message chiffré
recept=r.recv()
recept=recept.decode()
recept=recept[:-1]
recept=recept.split('-')
random.seed(t)
print(recept)

# Process de déchiffrement
decrypted_treasure = []
for c in recept:
    rd = random.randint(0, 255)
    b = (int(c) - int(rd)) % 256
    decrypted_treasure.append(b)
print(decrypted_treasure)
original_treasure = bytes(decrypted_treasure).decode()
print(original_treasure)
