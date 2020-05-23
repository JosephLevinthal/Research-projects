distancia = float(input("digite a distancia em km: "))
combustivel_gasto = float(input("digite o combustivel em Litros: ")) 
consumo_medio = distancia / combustivel_gasto
var = "km/l"
print(round(consumo_medio, 3),var)
