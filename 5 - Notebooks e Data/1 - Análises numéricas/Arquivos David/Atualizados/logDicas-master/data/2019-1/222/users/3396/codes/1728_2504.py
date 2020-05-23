virus = int(input("Digite: "))
leuco = int(input("Digite: "))
pvirus = int(input("Digite: "))
pleuco = int(input("Digite: "))

s_leuco = leuco
s_virus = virus
dias = 0

while s_leuco <= (s_virus * 2):
	s_leuco =  s_leuco + (s_leuco * (pleuco / 100))
	s_virus = s_virus + (s_virus * (pvirus / 100))
	dias = dias + 1
print(dias)

