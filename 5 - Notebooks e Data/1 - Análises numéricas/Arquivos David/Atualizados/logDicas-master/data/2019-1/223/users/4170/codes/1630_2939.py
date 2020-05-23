espetinhos = int(input("Quantos espetinhos? "))
lucro = ((espetinhos *12) * 83)/100
empregado = 100 + (lucro * 20)/100
lucro_liquido = lucro - empregado
print(round(lucro_liquido,2))