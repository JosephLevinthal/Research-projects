qac = int(input(" qual e a quantidade de acai? "))
qts= int(input("qual e a quantidade de salgados? "))
vl = float(input(" qual e o valor em dinheiro? "))
qac= qac*24
qts= qts*3
total = qac+qts
if(vl>=total):
	mensagem = "Sim"
else:
	mensagem = "Nao"
print(round(total,2))
print(mensagem)