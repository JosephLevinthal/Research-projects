j = float(input("taxa de juros: "))
ap = float(input("valor do apatamento: "))
q = 1500
t = 36
vf= (q * ((1+j)**t))
if(vf>=ap):
	print(round(vf, 2))
	print("Sim")
else:
	print(round(vf, 2))
	print("Nao")