num=int(input("numero de 4 digitos: "))

n1=num//1000	
n2=(num//100)%10
n3=(num//10)%10
n4=num%10

N1=(n1*5)
N2=(n2*4)
N3=(n3*3)
N4=(n4*2)
W=(N1+N2+N3+N4)
print(W%11)

