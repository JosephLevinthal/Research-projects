qper1 = int(input("Quantidade inicial de pergaminhos: "))
qvar1 = int(input("Quantidade oinicial de varinhas: "))
pvar = float(input("Percentual de crescimento de varinhas: "))/100
pper = float(input("Percentual de crescimento de pergaminhos: "))/100

cont = qper1 + (qper1 * pper) + qvar1 + (qvar1 * pvar)
espaco = 80000
anos = 0

while (espaco >= cont):
	anos += 1
	cont += qper1 + (qper1 * pper) + qvar1 + (qvar1 * pvar)
	espaco = espaco - cont
	
	
print(anos)