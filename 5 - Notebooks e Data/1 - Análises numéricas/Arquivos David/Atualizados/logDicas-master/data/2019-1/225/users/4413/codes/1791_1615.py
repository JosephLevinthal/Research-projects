from numpy import*
v1 = array(eval(int(input("aneis do primeiro jogador: "))))
v2 = array(eval(int(input("aneis do segundo jogador: "))))
dtype=int

if(sum(v1) < sum(v2)):
	msg="jogador um"
elif(sum(v2) < sum(v1)):
	msg="jogador dois"
else:
	msg="empate"
		
print(upper(msg))
