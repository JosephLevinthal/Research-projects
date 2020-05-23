vendas = float(input("espetinhos vendidos"))
lucro1 = 0.83*12
lucrototal = (vendas)*(lucro1)
empregado = 100 + (0.2*(lucrototal))
lucroliquido = (lucrototal)-(empregado)

print(round(lucroliquido, 2))