dg = int(input("digite a conta: "))

n1 = int(dg%10)
n2 = int((dg%100)/10)
n3 = int((dg/100)%10)
n4 = int(dg//1000)

N1 = n4*5
N2 = n3*4
N3 = n2*3
N4 = n1*2

N = N1 + N2 + N3 + N4
NF = N%11
print(NF)