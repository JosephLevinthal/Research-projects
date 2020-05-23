a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))

if (a<b and a<c and c>b):
	mensagem = b
else:
	if (c<b and c<a and b>a):
		mensagem = a
	else:
		if (b<c and b<a and a>c):
			mensagem = c
		else:
			if(a>b and a>c and b>c):
				mensagem = b
			else:
				if(a>b and a<c):
					mensagem = a
print(mensagem)