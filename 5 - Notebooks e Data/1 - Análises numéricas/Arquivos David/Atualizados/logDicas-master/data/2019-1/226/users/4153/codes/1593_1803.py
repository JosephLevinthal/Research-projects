num_conta=int(input("Insira o numero da conta: "))
D1=num_conta//1000
D2=(num_conta//100)-(10*D1)
D3=(num_conta//10)-((num_conta//100)*10)
D4=num_conta%10

A=((D1*5)+(D2*4)+(D3*3)+(D4*2))%11

print(A)