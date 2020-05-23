A = int(input("habitantes de uma cidade A: "))
B = int(input("habitantes de uma cidade B: "))
A1 = float(input("percentual de crescimeto populacional A: "))
B1 = float(input("percentual de crescimeto populacional B: "))

vca = A + ((A * A1)/100) #variavel acumuladora de A
vcb = B + ((B * B1)/100)  #variavel acumuladora de B
n = 1 #variavel contadora

while(vca < vcb):
	vca = vca +((vca * A1)/100)
	vcb = vcb +((vcb * B1)/100)
	n = n + 1
print(n)