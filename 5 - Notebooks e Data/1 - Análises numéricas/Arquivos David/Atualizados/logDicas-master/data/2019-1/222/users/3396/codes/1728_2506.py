
q_peixes = int(input("Digite :"))
p_cres = int(input("Digite :"))
ret = int(input("Digite :"))

s_peixe = q_peixes
anos = 0 
s_ret = 0
while s_peixe > 0 and s_peixe < 12000:
		s_peixe = s_peixe + (s_peixe * (p_cres / 100)) - ret
		anos = anos + 1
if s_peixe < s_ret:
	print("EXTINCAO")
	print(anos)
else:
	print("LIMITE")
	print(anos)