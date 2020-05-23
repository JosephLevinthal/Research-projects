tempo = int(input())
qf = 1.042.000
q0 = 1.500
i = round((qf/q0**(1/t)) - 1 ,5)
if i <= 0.01:
	mensagem = "Real"
else: 
	mensagem = "Ireeal"
print(i)
print(mensagem)