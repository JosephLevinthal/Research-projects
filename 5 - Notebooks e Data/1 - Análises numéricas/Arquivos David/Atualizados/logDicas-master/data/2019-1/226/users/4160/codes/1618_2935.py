# Universidade Federal do Amazonas
# Aluna: Bruna Santiago dos Santos
# Data: 02/04/2018

# Massa dos caminhões: 
ma = float(input(" Digite a massa do caminhao a em kg: "))
mb = float(input(" Digite a massa do caminhao b em kg: "))

# Velocidade do caminhão B: 
v0 = float(input(" Digite a velocidade do caminhao b: "))

# Velocidade após a colisão: 
vf = (( 2 * ma  + mb ) / (ma + mb))  * v0

print(vf)


