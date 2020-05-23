s= int(input("insira a qnt de sucos:"))
sal= int(input("insira a quantidade de salgados:"))
v= float(input("insira o valor disponivel:"))
vl= (s*3+sal*3.50)
if(vl<=v):
	mensagem="Sim"
else:
	mensagem="Nao"
print(round(vl,2))
print(mensagem)