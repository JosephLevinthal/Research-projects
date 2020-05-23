espetinhos = float(input("quantos espetinhos foram vendidos? "))
valor = 12 * 0.83
venda = (espetinhos * valor) 
empregado = 100 + (venda *0.2) 
total = venda - empregado
print(round(total, 2))