import hashlib
import struct

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).digest()
    return sha_signature

alphabet = "abcdefghijklmnopqrstuvwxyz"
chiffres = "0123456789"
speciaux = r"~!@#$%^&*()-_=+[]{};:,.<>/?"

alphanum = chiffres + alphabet + alphabet.upper()


#print majuscules

site = raw_input("nom du site: ")
pmdp = raw_input("mot de passe primaire: ")
tout = site.lower() + pmdp

cc = encrypt_string(tout)

amdp = []

num = struct.unpack('B',cc[0])[0]; # unsigned char
indice = num % len(alphabet)
amdp.append(alphabet[indice].upper())
num = struct.unpack('B',cc[1])[0]; # unsigned char
indice = num % len(chiffres)
amdp.append(chiffres[indice])
num = struct.unpack('B',cc[2])[0]; # unsigned char
indice = num % len(speciaux)
amdp.append(speciaux[indice])
num = struct.unpack('B',cc[3])[0]; # unsigned char
indice = num % len(alphabet)
amdp.append(alphabet[indice])

for i in range(8):
	num = struct.unpack('B',cc[i+4])[0]; # unsigned char
	indice = num % len(alphanum)
	amdp.append(alphanum[indice])

mdp = ""
for c in amdp:
	mdp = mdp + c
	
print mdp

	


