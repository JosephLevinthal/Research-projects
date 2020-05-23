qt = int(input("insira a quantidade inicial de tambaquis: "))
pt = float(input("insira o percentual de crscimento de tambaquis:"))
qv = int(input("insira a quantidade de tambaquis postos a venda:"))
ano = 0
ct = (qt * pt)/100
while(qt > 0 and qt < 12000):
	ct = (qt * pt)/100
	qt = qt + ct - qv
	ano = ano + 1
if(qt <= 0):
	msg = "EXTINCAO"
else:
	msg = "LIMITE"
print(msg)
print(ano)

