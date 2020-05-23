preco = float(input("Preco do ingresso: "))
quan = int(input("Quantidade de ingressos: "))

promo = preco - (preco * (20/100))
a = promo * quan
print(round(a, 2))