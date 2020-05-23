valor = float(input())
qt = int(input())
valortiket = float(input())
qpasses = int(input())
valorpasses = float(input())

t = valor - ((valortiket*qt) + (valorpasses*qpasses))
if(t>=0):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")