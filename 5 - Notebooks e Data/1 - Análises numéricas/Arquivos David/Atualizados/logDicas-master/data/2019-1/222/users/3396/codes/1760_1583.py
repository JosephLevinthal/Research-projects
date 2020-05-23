from numpy import*
n=input("digita um string: ")

n1=len(n)

s1=n[0:3]   #posicao de tres em tres
l=3 

while l<n1:
    s1= s1 + "." + n[l:l+3]
    l=3+l
print(s1)

