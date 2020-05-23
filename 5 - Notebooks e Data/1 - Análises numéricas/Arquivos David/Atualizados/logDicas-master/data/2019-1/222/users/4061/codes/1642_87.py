a = int(input("digite a: "))
b = int(input("digite b: "))
c = int(input("digite c: "))

if(a<b and a<c):
	mensagem = a
else:
	if(b<a and b<c):
		mensagem = b
	else:
		mensagem = c

print(mensagem)