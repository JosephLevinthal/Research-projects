# Leitura das coordenados dos pontos A e B:
xA = float(input("Digite um valor para absissa de A: "))
yA = float(input("Digite um valor para ordenada de A: "))
xB = float(input("Digite um valor para absissa de B: "))
yB = float(input("Digite um valor para ordenada de B: "))

# Calculo da distancia de A para B:
dAB = round(((xB - xA)**2 + (yB - yA)**2)**0.5, 3)
print(dAB) 
