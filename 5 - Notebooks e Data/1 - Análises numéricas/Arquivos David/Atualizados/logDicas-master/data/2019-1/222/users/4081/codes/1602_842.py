# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("quatro digitos: "))
numero1= (num//1000)
numero2= (num//100) % 10
numero3= (num//10)  % 10
numero4= (num%10)
soma=(numero1+numero2+numero3+numero4)
print(soma)			 
			 