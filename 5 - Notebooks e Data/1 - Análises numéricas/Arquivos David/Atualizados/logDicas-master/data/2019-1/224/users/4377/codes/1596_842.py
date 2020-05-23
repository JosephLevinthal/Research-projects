nu=int(input("numerode4digitos"))
a1=nu//1000
a2=(nu%1000)//100
a3=((nu%1000)%100)//10
a4=(((nu%1000)%100)%10)
soma=a1+a2+a3+a4
print(soma)