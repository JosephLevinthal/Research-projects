qi=int(input("quanridade inicial de baloes: "))
qc=int(input("quantidade de baloes construidos a cada semana: "))
qd=int(input("quantidade de baloes destruidos a cada semana: "))

s=0
soma=0
while(qi<200):
	qi=qi+qc
	qi=qi-qd
	s+=1
print(s)