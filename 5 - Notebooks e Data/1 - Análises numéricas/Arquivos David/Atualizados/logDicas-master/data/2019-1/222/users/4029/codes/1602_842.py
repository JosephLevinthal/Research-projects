# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var= int(input("digite um numero inteiro de 4 digitos: "))
var1= var//1000
var2= (var%1000)//100
var3= ((var%1000)%100)//10
var4= ((var%1000)%100)%10	 
print(var1+var2+var3+var4)