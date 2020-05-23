from numpy import*
x=int(input("Digite um numero ate 10.000 "))
a=array(['um','dois','tres','quatro','cinco','seis','sete','oito','nove'])
b=array(['dez','onze','doze','deze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa'])
c=array(['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos'])
d=array(['mil','dois mil','tres mil','quatro mil','cinco mil','seis mil','sete mil','oito mil','nove mil'])
t=x//10000
m=(x//1000)%10
n=(x//100)%10
q=(x//10)%10
j=x%10
y=x%100

if(j==1):
	j=a[j-1]
elif(j==2):
	j=a[j-1]
elif(j==3):
	j=a[j-1]
elif(j==4):
	j=a[j-1]
elif(j==5):
	j=a[j-1]
elif(j==6):
	j=a[j-1]
elif(j==7):
	j=a[j-1]
elif(j==8):
	j=a[j-1]
elif(j==9):
	j=a[j-1]
	
if(x==10):
	j=b[x-10]
elif(x==11):
	j=b[x-10]
elif(x==12):
	j=b[x-10]
elif(x==13):
	j=b[x-10]
elif(x==14):
	j=b[x-10]	
elif(x==15):
	j=b[x-10]	
elif(x==16):
	j=b[x-10]	
elif(x==17):
	j=b[x-10]	
elif(x==18):
	j=b[x-10]	
elif(x==19):
	j=b[x-10]	

if(q==2):
	q=b[q+8]
elif(q==3):
	q=b[q+8]
elif(q==4):
	q=b[q+8]
elif(q==5):
	q=b[q+8]
elif(q==6):
	q=b[q+8]
elif(q==7):
	q=b[q+8]
elif(q==8):
	q=b[q+8]
elif(q==9):
	q=b[q+8]
	
if(n==1):
	n=c[n-1]
elif(n==2):
	n=c[n-1]
elif(n==3):
	n=c[n-1]
elif(n==4):
	n=c[n-1]
elif(n==5):
	n=c[n-1]
elif(n==6):
	n=c[n-1]
elif(n==7):
	n=c[n-1]
elif(n==8):
	n=c[n-1]
elif(n==9):
	n=c[n-1]
	
if(m==1):
	m=d[m-1]
elif(m==2):
	m=d[m-1]
elif(m==3):
	m=d[m-1]
elif(m==4):
	m=d[m-1]
elif(m==5):
	m=d[m-1]
elif(m==6):
	m=d[m-1]
elif(m==7):
	m=d[m-1]
elif(m==8):
	m=d[m-1]
elif(m==9):
	m=d[m-1]	

if(y==10):
	c="dez"
elif(y==20):
	c="vinte"
elif(y==30):
	c="trinta"
elif(y==40):
	c="quarenta"
elif(y==50):
	c="cinquenta"
elif(y==60):
	c="sessenta"
elif(y==70):
	c="setenta"
elif(y==80):
	c="oitenta"
elif(y==90):
	c="noventa"
elif(y==11):
	c="onze"
elif(y==12):
	c="doze"
elif(y==13):
	c="treze"
elif(y==14):
	c="quatorze"
elif(y==15):
	c="quinze"
elif(y==16):
	c="dezesseis"
elif(y==17):
	c="dezessete"
elif(y==18):
	c="dezoito"
elif(y==19):
	c="dezenove"	

	
if(x==0):
	print("zero")
elif(x>0 and x<=19):
	print(j)
elif(j==0)and(x>19 and x<99):
	print(q)
	
x=str(x)
if(len(x)==2):
	if(int(x)>20 and j!=0):
		print(q," e ",j)
elif(len(x)==3):
	if(int(x)==111):
		print("cento e onze")
	elif(int(x)==112):
		print("cento e doze")
	elif(int(x)==113):
		print("cento e treze")
	elif(int(x)==114):
		print("cento e quatorze")
	elif(int(x)==115):
		print("cento e quinze")
	elif(int(x)==116):
		print("cento e dezesseis")
	elif(int(x)==117):
		print("cento e dezessete")
	elif(int(x)==118):
		print("cento e dezoito")
	elif(int(x)==119):
		print("cento e dezenove")	
	elif(j==0)and(y==10 or y==20 or y==30 or y==40 or y==50 or y==60 or y==70 or y==80 or y==90):
		print(n," e ",c)
	elif(y>=11 and y<=19):
		print(n," e ",c)
	elif(q!=0 and j!=0):	
		print(n," e ",q," e ",j)
	elif(q==0 and j!=0):
		print(n," e ",j)
	elif(j==0 and q==0 and n=="cento"):
		print("cem")
	elif(j==0 and q==0):
		print(n)
elif(len(x)==4):
	if(j==0 and q==0 and n==0):
		print(m)
	elif(n==0) and (j==0) and (y==10 or y==20 or y==30 or y==40 or y==50 or y==60 or y==70 or y==80 or y==90):	
	   print(m," e ",c)
	elif(n==0)and(y>=11 and y<=19):
		print(m," e ",c)
	elif(j!=0 and q!=0 and n!=0):
		print(m," e ",n," e ",q," e ",j)
	elif(j==0 and q!=0 and n!=0):
		print(m," e ",n," e ",q)
	elif(q==0 and j!=0 and n!=0):
		print(m," e ",n," e ",j)
	elif(q==0 and j==0 and n!=0):
		print(m," e ",n)
	elif(q==0 and n==0):
		print(m," e ",j)
	elif(j==0 and n==0):
		print(m," e ",q)






	
	