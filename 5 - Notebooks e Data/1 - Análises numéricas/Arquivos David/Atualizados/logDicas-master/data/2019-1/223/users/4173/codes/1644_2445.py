a = input("C,F")
b = float(input())
r = 5/9*(b-32)
d = 1.8*b+32

if (a == "F"):
	mensagem = r
if (a == "C"):
	mensagem = d
print(round(mensagem,2))
	
	
