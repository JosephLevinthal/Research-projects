valor = float(input())
qtick = int(input())
vtick = float(input())
qpass = int(input())
vpass = float(input())
if qtick*vtick + qpass*vpass < valor:
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")