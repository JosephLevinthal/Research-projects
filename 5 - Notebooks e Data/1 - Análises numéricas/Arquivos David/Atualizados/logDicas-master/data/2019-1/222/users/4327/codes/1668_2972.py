s0=int(input("s0: "))
v=int(input("velocidade: "))
t=int(input("tempo em segundos: "))

s=s0+(v*t)

if(s>=1000):
	print(s)
	print("Sim")
else:
	print(s)
	print("Nao")