var1=int(input());

var2=(var1//1000)*5;

var3=((var1//100)%10)*4

var4=(((var1//10)%100)%10)*3;

var5=(((var1%1000)%10)%10)*2;

soma=var2+var3+var4+var5;
resultado=soma%11;

print(resultado);