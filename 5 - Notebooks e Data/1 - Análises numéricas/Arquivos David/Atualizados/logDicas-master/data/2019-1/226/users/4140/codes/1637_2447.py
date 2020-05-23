preco=float(input());
pag=float(input());

if(preco>pag):
	calc=preco-pag
	calc1=round(calc,2);
	print("Falta",calc1);
if(preco<=pag):
	calc=pag-preco;
	calc1=round(calc,2);
	print("Troco de",calc1);

	
	