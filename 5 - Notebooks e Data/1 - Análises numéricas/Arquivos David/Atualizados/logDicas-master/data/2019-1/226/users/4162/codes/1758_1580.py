from numpy import*
n=array(eval(input("insira as notas: ")))
na=array(eval(input("insira os nomes: ")))

i=0
f=0
a=0
r=0
s=0
while i!=size(n):
	if n[i]==-1:
		f=f+1
	elif n[i]>=6:
		a=a+1
	elif n[i]<6 and n[1]!=-1:
		r=r+1
	if n[i]!=-1:
		s=s+n[i]
	if n[i]==max(n):
		m=i
	i=i+1
print(f)
print(a)
print(r)
print(round(s/(size(n)-f),2))
print(na[m])