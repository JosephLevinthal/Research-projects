tempo = float(input("Tempo de viagem: "))
velocidade = float(input("Velocidade media: "))

distancia = velocidade * tempo
quantidade = distancia / 12

print (round(distancia, 1))
print (round(quantidade, 1))
