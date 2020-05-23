qi = int(input())
pc = int(input())/100
qv = int(input())

anos = 0 

while(qi>0 and qi<12000):
	qi = (qi + (qi*pc)) - qv
	anos = anos +1
	if(qi<0):
		mensagem = "EXTINCAO"
	else:
		mensagem = "LIMITE"
print(mensagem)
print(anos)
	