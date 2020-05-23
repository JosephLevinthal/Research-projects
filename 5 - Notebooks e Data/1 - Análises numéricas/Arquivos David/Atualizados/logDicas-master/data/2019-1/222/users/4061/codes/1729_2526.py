num1 = int(input("digite numero1: ")) #o numero que ira ser digitado primeiro
num2 = int(input("digite numero2: ")) #o segundo numero

soma1 = 0 #essa variável é para armazenar a soma dos divisores (quocientes) do primeiro numero digitado
soma2 = 0 #essa variável é para armazenar a soma dos divisores (quocientes) do segundo numero digitado - 
#ex.: se for 6, o quociente achado sera 1, 2 e 3 - quando o resto for zero
cont1 = num1 #a variavel cont1 vai ter o mesmo valor do numero digitado - para usarmos como um contador
cont2 = num2 #o mesmo para a variavel cont2 - iremos contar ex.: se digitar 6 iremos contar 6,5,4,3,2,1 e 0

while(cont1 > 1):#o contador inicia com (exemplo) 6, entao 6 > 1 ok, mas quando for 1 > 1, falso, para de contar
	if(num1 % cont1 == 0): #nesse if procuramos as divisoes de resto zero, se achar, ok, se não, pula e vai para cont1
		soma1 = soma1 + (num1 // cont1) #aqui somamos os divisores (quocientes encontrados) 
	cont1 = cont1 - 1 #aqui contamos de cima para baixo, ex.: 6,5,4,3,2,1,0
	
while(cont2 > 1): #mesma logica do de cima, para achar a soma do segundo numero
	if(num2 % cont2 == 0):
		soma2 = soma2 + (num2 // cont2)
	cont2 = cont2 - 1

print(soma1)#terminando as somas acima, aqui vamos imprimir o que foi somado
print(soma2)

if(soma1 == num2 and soma2 ==num1): #aqui so vai ser amigos se um numero for igual a soma do outro e vise-versa
	print("AMIGOS")
else:
	print("NAO AMIGOS")
