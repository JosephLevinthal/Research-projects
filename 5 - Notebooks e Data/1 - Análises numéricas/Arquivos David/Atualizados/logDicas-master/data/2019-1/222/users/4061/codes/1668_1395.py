vendas = float(input("digite vendas"))
#comissao1 = (1000*0.05)
#comissao2 = (1000*0.1)

if(vendas<=1000):
   mensagem = (vendas*0.05)
				
else:
	mensagem = (vendas*0.05)+(vendas-1000)*0.1
				 
print(round(mensagem, 2))
