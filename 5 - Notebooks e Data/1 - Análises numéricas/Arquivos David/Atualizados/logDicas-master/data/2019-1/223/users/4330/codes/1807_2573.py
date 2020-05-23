from numpy import*
peso = array(eval(input("")))
altura = array(eval(input("")))
imc_dos_alunos = zeros(size(peso), dtype=float)

for i in range(size(peso)):
	imc_dos_alunos[i] = peso[i]/(altura[i]**2)
	imc_dos_alunos[i] = round(imc_dos_alunos[i],2)
	
print(imc_dos_alunos)
maior = max(imc_dos_alunos)
print("O MAIOR IMC DA TURMA EH:",maior)

if maior < 17:
	mensagem = "muito abaixo do peso"
elif maior >17 and maior < 18.49 :
	mensagem = "abaixo do peso"
elif maior >= 18.5 and maior < 24.99:
	mensagem = "peso normal"
elif maior > 25 and maior < 29.99:
	mensagem = "acima do peso"
elif maior > 30 and maior < 34.99:
	mensagem = "obesidade"
elif maior >= 35 and maior < 39.99:
	mensagem = "obesidade severa"
elif maior > 40:
	mensagem = "obesidade morbida"
print(mensagem.upper())
	