from numpy import*

x = array(eval(input("vetor faltas: ")))
s = zeros(6, dtype=float) #vetor dias da semana

for i in x:
	if i == 2:
		s[0] = s[0] + 1
	elif i == 3:
		s[1] = s[1] + 1
	elif i == 4:
		s[2] = s[2] + 1
	elif i == 5:
		s[3] = s[3] + 1
	elif i == 6:
		s[4] = s[4] + 1
	elif i == 7:
		s[5] = s[5] + 1
t = sum(s)
j = 0
for k in s:
	s[j] = round((s[j] * (100/t)), 1)
	j = j + 1
print(s)