vi = int(input('vi: '))
vb = int(input('vb: '))
vr = int(input('vr: '))
c = 0

while (vi>1000):
	vi = vi+vb
	vi = vi-vr
	c = c+1
print(c)