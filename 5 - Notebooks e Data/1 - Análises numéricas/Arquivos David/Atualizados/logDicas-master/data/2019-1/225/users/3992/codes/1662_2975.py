var1 = int(input("quantidade do suco: "))
var2 = int(input("quantidade de salgado:"))
var3 = float(input("valor disponivel: "))
var4 = var1*3
var5 = var2*3.5
var6 = var4 + var5
if(var4 + var5 <= var3): 
	mensagem = "Sim"
else: 
	mensagem = "Nao"
print(round(var6,2))
print(mensagem)