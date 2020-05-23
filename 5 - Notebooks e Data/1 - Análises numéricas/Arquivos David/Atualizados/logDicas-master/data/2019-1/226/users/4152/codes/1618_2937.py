n = int(input("Escreva o numero de mols de um gas: "))

V = float(input("Escreva o volume do gas: "))

T = float(input("Escreva a temperatura do gas: "))

Tt = T + 273.1

R = 0.082057

p = (n * R * Tt) / V

print(p)