distancia=float(input("Qual a distancia percorrida em km?"))
combustivel=float(input("Total de combustivel gasto em litros?"))
consumo=(distancia/combustivel)
texto="km/l"
print(round(consumo, 3),texto)