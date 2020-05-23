# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
vb= float(input("escolha o valor: "))
if(vb>=200.00):
	r=vb-vb*0.05
else:
	r=vb
print(round(r, 2))