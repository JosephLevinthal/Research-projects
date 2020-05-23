pres=float(input())
mols=float(input())
temp=float(input())
temp1=temp+273.15

resultado=(0.082*mols*temp1)/pres

print(resultado)