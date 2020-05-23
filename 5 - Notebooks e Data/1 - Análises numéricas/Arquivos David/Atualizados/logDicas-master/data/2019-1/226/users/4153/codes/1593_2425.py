dist = float(input("Insira a distancia: "))
comb = float(input("Insira a consumo de combustivel: "))

cons_medio = dist/comb 
D = round(cons_medio, 3)
print(D,"km/l")