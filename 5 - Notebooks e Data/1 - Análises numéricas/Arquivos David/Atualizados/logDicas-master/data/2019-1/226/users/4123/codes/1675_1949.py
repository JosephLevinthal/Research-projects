num = input()
res = input()

if num == res:
	print("Ganhou R$ 100.000,00")
elif num[0]==res[1] and num[1]==res[0]:
	print("Ganhou R$ 50.000,00")
elif num[0]==res[0] or num[1]==res[0] or num[1]==res[1] or num[0]==res[1]:
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")