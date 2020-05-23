suco=int(input("entre com a quantidades de sucos: "))
sal= int(input("entre com a quantidade de salgados: "))
valor=float(input("entre com o valor disponivel: "))

valsu= suco*3
valsal=sal*3.50
valtotal=valsu+valsal
print(valtotal)

if(valtotal<=valor):
	
	print("Sim")
	
else:
	print("Nao")
