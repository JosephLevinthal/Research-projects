var=float(input(" Quantos espetos bob vendeu? "))
lucro=0.83 * (var*12)
empregado=100+(0.2*lucro)
ll=lucro-empregado
print(round(ll,2))