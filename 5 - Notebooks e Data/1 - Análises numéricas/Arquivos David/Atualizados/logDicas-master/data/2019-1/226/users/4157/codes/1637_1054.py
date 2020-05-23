x = float(input("coordenada x:"))
y = float(input("coordenada y:"))
reta = (2*x + y)
if(reta == 3):
	per = "ponto pertence a reta"
else:
	per = "ponto nao pertence a reta"
	
print(per.lower())