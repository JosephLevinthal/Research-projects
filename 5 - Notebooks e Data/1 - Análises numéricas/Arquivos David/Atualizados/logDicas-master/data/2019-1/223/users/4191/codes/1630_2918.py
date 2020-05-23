#p é o preço integral, q é a quantidade de ingressos
p= float(input("Preco integral do ingresso: "))
q=float(input("quantidade: "))
v=p-(p*20/100)
t=q*v
print(round(t, 2))