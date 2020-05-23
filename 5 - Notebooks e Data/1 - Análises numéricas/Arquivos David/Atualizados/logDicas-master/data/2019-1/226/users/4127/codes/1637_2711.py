disp= int(input("Qual o valor que voce tem disponivel?"))
ru= int(input("quantos tickets de ru voce quer comprar?"))
vru= float(input("qual o valor dos tickets do ru?"))
passe= int(input("qual a quantidade de passes do onibus?"))
vpasse= float(input("qual o valor dos passes?"))

total= disp-((ru*vru)+(passe*vpasse))

if (total>0):
	msg="suficiente".upper()
if (total<0):
	msg="insuficiente".upper()
print(msg)