
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite um valor para x:"))
a = float(input("digite um valor para a:"))
b = float(input("digite un valor para b:"))

if(b <= a):
	print("Entradas",a,"e",b,"invalidas")
elif(x < a or x > b):
	print(x,"nao pertence ao intervalo",a,",",b)
elif( x >= a and x <= b):
	print(x,"pertence ao intervalo",a,",",b)