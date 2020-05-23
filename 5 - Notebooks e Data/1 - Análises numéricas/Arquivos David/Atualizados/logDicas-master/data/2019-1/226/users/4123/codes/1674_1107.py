# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
num = int(input())
d = int(input())
if num not in range(0,7):
	print("A entrada ",num," eh invalida")
else:
	dia = (d+num)%7
	dias = ["domingo","segunda","terca","quarta","quinta","sexta","sabado"]
	print("Hoje eh",dias[num],"e o dia futuro eh",dias[dia])
