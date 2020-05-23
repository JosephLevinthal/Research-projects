acai = float(input("quantidade de acai: "))
salgado = int(input("quantidade de salgado: "))
valor = float(input("valor: "))

total = 24*(acai/1000) + 3*salgado

if  (total <= valor):
      print(round(total, 1))
      print("Sim")
		
else:
      print(round(total, 1))
      print("Nao")
     