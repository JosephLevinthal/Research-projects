# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("preco sem disconto:"))
vlr = p*0.05
if(p > 200.0):
	vt = p-vlr
else:
	vt = p
	
print(round(vt, 2))