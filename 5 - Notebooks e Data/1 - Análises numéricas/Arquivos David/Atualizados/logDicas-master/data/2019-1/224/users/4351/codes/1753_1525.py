vi=int(input("volume inicial: "))
vb=int(input("volume de agua que e bombeado para dentro da masmorra por minuto: "))
vr=int(input("volume de aguya que a elfa retira da masmorra por minuto: "))
min=0
while vi>1000:
	vi= (vi+vb)-vr
	min= min+1
print(min)