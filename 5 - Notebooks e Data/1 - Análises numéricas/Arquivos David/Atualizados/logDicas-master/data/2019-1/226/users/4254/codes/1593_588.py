# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("Qual o valor do saque? "))

notas100 = int(valor // 100)
notas50 = int((valor % 100)//50)
notas10 = int(((valor % 100)%50)//10)
			  
print(int(notas100))
print(int(notas50))
print(int(notas10))	  
