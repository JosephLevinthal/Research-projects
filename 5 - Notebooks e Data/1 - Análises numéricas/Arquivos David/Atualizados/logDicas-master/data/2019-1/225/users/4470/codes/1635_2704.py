nota = float(input())
msg = input("bonificacao? S/N ")

if (msg == "S"):
	x = nota+(10/100)*nota
	
else:
	x = nota
	
print(x)