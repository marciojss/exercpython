def ctof(temperc):
	temperf = 9*temperc/5+32
	return temperf
def ftoc(temperf):
	temperc = (temperf-32)*5/9
	return temperc
value = input("qual a temperatura?")
tipo = raw_input ("qual a escala?")
if tipo == 'f'| tipo == 'F':
	print ftoc(value)
elif tipo == 'c'| tipo == 'C':
	print ctof(value)
else:
	print 'tipo invalido'
