#determinar o tempo de subida
H=int(input())
vg=int(input())
vm=int(input())
total=0
i=0

while(total<H):
	total=total+vg
	if(total<H):
		total=total-vm
	i=i+1
print(i)
	
