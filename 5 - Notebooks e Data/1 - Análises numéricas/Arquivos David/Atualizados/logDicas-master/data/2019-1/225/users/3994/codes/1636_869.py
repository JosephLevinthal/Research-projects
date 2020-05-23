# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
psd = float(input(" digite psd: "))
d = 5/100

if (psd>=200):
	pcd = psd -(psd * d)
	print(round(pcd,2))
else:
	print(round(psd,2))