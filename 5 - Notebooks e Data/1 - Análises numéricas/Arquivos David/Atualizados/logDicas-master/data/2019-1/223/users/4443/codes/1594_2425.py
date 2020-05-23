# Leitura da quilometragem total
km = float(input("Qual quilometragem total? "))

# Leitura do combustivel gasto
gas = float(input("Qual o total de combustivel gasto? "))

# Calculo do consumo medio
cm = km/gas

# saida
print(round(cm, 3), "km/l")
