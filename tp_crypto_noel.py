# -*- coding: utf-8 -*-

"""
QUESTION SUR ALGORITHME POUR 
LA GENERATION DES CLES DE FEISTEL
"""

# Convertir un nombre en binaire sur 8 bits

def bin8(n):
    return format(n, "08b")

# Appliquer la fonction de permutation H à un nombre sur 8 bits

def permute(n, H):
    b = bin8(n)                                # on convertir le nombre en binaire
    
    p = ""                                     # On initialise le résultat
    
    for i in H:                                # pour chaque indice dans H
        p += b[i]                              # ajouter le bit correspondant au résultat
    return int(p, 2)                           # convertir le résultat en décimal

# Ici on divise un nombre sur 8 bits en deux blocs de 4 bitS

def split(n):
    b = bin8(n)                                # convertir le nombre en binaire
    k1 = b[:4]                                 # prendre les 4 premiers bits
    k2 = b[4:]                                 # prendre les 4 derniers bits
    return int(k1, 2), int(k2, 2)              # convertir les blocs en décimal

# On Calcule le OU exclusif de deux nombres sur 4 bits

def xor4(a, b):
    return a ^ b                               # utiliser l'opérateur xor de python

# On Calcule le ET logique de deux nombres sur 4 bits

def and4(a, b):
    return a & b                              

# On Applique le décalage à gauche d'ordre 2 à un nombre sur 4 bits

def shift_left(n):
    b = format(n, "04b")                       # convertir le nombre en binaire
    s = b[2:] + b[:2]                          # décaler les bits de 2 positions vers la gauche
    return int(s, 2)                           # convertir le résultat en décimal

# On  Applique le décalage à droite d'ordre 1 à un nombre sur 4 bits

def shift_right(n):
    b = format(n, "04b")                       # convertir le nombre en binaire
    s = b[-1] + b[:-1]                         # décaler les bits de 1 position vers la droite
    return int(s, 2)                           # convertir le résultat en décimal

# Générer deux sous-clés de 4 bits à partir d'une clé de 8 bits

def generate_keys(K, H):
    
    Kp = permute(K, H)                         # appliquer la permutation H à la clé K
    k1p, k2p = split(Kp)                       # diviser la clé permutée en deux blocs
    k1 = xor4(k1p, k2p)                        # calculer k1 par le ou exclusif de k1p et k2p
    k2 = and4(k1p, k2p)                        # calculer k2 par le et logique de k1p et k2p
    k1 = shift_left(k1)                        # appliquer le décalage à gauche à k1
    k2 = shift_right(k2)                       # appliquer le décalage à droite à k2
    
    return k1, k2 



"""
QUESTION SUR ALGORITHME
DE CHIFFREMENT DE FEISTEL
"""

# Ici on Iimporter le module random pour générer des clés aléatoires

import random

# A ce niveau on définie une fonction qui effectue l'opération xor entre deux chaînes binaires

def xor(a, b):

    result = ""

    for i in range(len(a)):
    
        if a[i] == b[i]:
            result += "0"
  
        else:
            result += "1"
 
    return result

# Définir une fonction qui effectue la permutation d'une chaîne binaire selon un ordre donné

def permute(a, order):
   
    result = ""
   
    for i in order:
        
        # Ajouter le bit correspondant de la chaîne au résultat
        
        result += a[i]

    return result

# Définir le bloc N de 8 bits

N = "10100110"

# On définir la permutation π

pi = [3, 5, 9, 6, 0, 7, 2, 1]

# On pplique la permutation π au bloc N

N = permute(N, pi)

# Diviser N en deux blocs de 4 bits
G0 = N[:4]
D0 = N[4:]

# Générer des clés aléatoires k1 et k2 de 4 bits

k1 = "".join([str(random.randint(0, 1)) for _ in range(4)])
k2 = "".join([str(random.randint(0, 1)) for _ in range(4)])

# Définir la permutation P

P = [1, 9, 0, 2]

# Premier round

# Calculer D1 = P(G0) ⊕ k1
D1 = xor(permute(G0, P), k1)

# Calculer G1 = D0 ⊕ (G0 ∨ k1)
G1 = xor(D0, xor(G0, k1))

# Deuxième round

# Calculer D2 = P(G1) ⊕ k2
D2 = xor(permute(G1, P), k2)

# Calculer G2 = D1 ⊕ (G1 ∨ k2)
G2 = xor(D1, xor(G1, k2))

# Concaténer G2 et D2 pour obtenir C
C = G2 + D2

# Appliquer l'inverse de la permutation π à C

C = permute(C, [4, 7, 6, 0, 3, 1, 5, 2])

# Enfin on Affiche le texte chiffré C

print("Le texte chiffré C est:", C)



"""
QUESTION SUR ALGORITHME
DE DECHIFFREMENT DE FEISTEL

"""


PI = "46027315" 

P = "2013" 

K1 = "1010" 

K2 = "1100" 

# Définir une fonction pour convertir un nombre en binaire

def to_bin(n, bits):
    
  return bin(n)[2:].zfill(bits)

# Définir une fonction pour convertir un binaire en nombre

def to_num(b):
    
  return int(b, 2)

# Définir une fonction pour appliquer une permutation à un binaire

def permute(b, p):
    
  return "".join([b[int(i)-1] for i in p])

# Définir une fonction pour effectuer un XOR entre deux binaires

def xor(b1, b2):
    
  return "".join(["0" if b1[i] == b2[i] else "1" for i in range(len(b1))])

# Définir une fonction pour effectuer un OR entre deux binaires

def or_(b1, b2):
    
  return "".join(["1" if b1[i] == "1" or b2[i] == "1" else "0" for i in range(len(b1))])

# Définir une fonction pour inverser une permutation

def inverse(p):
    
  return "".join([str(p.index(str(i))+1) for i in range(1, len(p)+1)])

# Définir la fonction de déchiffrement de Feistel

def feistel_decrypt(C):
    
  # Appliquer la permutation initiale
  
  C = permute(C, PI)
  
  # Diviser C en deux blocs de 4 bits
  
  G2, D2 = C[:4], C[4:]
  
  # Premier tour
  
  G1 = permute(xor(D2, K2), inverse(P))      # G1 = P^-1 * (D2 ⊕ K2)
  
  D1 = xor(G2, or_(G1, K2))                  # D1 = G2 ⊕ (G1 ∨ K2)
  
  # Deuxième tour
  
  G0 = permute(xor(D1, K1), inverse(P))      # G0 = P^-1 * (D1 ⊕ K1)
  D0 = xor(G1, or_(G0, K1))                  # D0 = G1 ⊕ (G0 ∨ K1)
  
  # Concaténer G0 et D0
  N = G0 + D0
  
  # Appliquer l'inverse de la permutation initiale
  
  N = permute(N, inverse(PI))
  
  
  return N




"""
#QUESTION 2
LGORITHME DE CARRE ET MULTIPLICATION
"""

# Fonction qui calcule x^b (mod n) en utilisant l'algorithme des carrés et des multiplications

def square_and_multiply(x, b, n):
     
  b = bin(b)[2:]                  # Convertir l'exposant b en binaire
 
  result = 1                      # Initialiser le résultat à 1
  
  # Parcourir les bits de b de droite à gauche
  
  for bit in b[::-1]:
      
    # Si le bit est 0, on élève le résultat au carré modulo n
    
    if bit == "0":
      result = (result * result) % n
      
    # Si le bit est 1, on élève le résultat au carré modulo n, puis on le multiplie par x modulo n
    
    else:
      result = (result * result * x) % n
  # Retourner le résultat final
  return result

# Demander à l'utilisateur de saisir les valeurs de x, b et n
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))

# Afficher le résultat de x^b (mod n)

print(f"{x}^{b} (mod {n}) = {square_and_multiply(x, b, n)}")