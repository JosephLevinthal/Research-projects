autonomia = 12.0

tempo = float(input("tempo gasto (em h): "))
velocidade = float(input("velocidade media (em km/h): "))

distancia = tempo*velocidade 

litros = distancia / autonomia

print(distancia)
print(litros)