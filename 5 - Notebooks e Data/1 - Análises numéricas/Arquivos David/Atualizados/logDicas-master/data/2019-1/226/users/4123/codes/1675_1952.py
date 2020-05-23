s = float(input())

if s <=1659.38:
	s = s - s*0.08
elif s>1659.38 and s<=2765.66:
	s = s - s*0.09
elif s>2765.66 and s<=5531.31:
	s = s - s*0.11
else:
	s = s - 608.44

if  s>1903.98 and s<=2826.65:
	s = s - s*0.075
elif s>2826.65 and s<=3751.05:
	s = s - s*0.15
elif s>3751.05 and s<=4664.68:
	s = s - s*0.225
elif s>4664.68:
	s = s - s*0.275

print("Salario liquido = R$",round(s,2))
	