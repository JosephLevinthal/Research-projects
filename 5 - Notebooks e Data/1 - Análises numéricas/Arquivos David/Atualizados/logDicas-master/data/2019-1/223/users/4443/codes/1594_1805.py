# Leitura das coordenados dos pontos A e B:
xA = float(input("Digite um valor para absissa de A: "))
yA = float(input("Digite um valor para ordenada de A: "))
xB = float(input("Digite um valor para absissa de B: "))
yB = float(input("Digite um valor para ordenada de B: "))

# Calculo das coordenadas do ponto M:
xM = round((xB + xA)/2, 1)
yM = round((yB + yA)/2, 1)

print(xM, yM)



