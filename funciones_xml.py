#Ejercicio listar munición del arma
def lista(texto, categoria):
	arma=texto.xpath("//armas/{}/nombre/text()".format(categoria))
	cargador=texto.xpath("//armas/{}/cargador/text()".format(categoria))
	lista1=[]
	for elem1,elem2 in zip(arma, cargador):
		lista1.append(elem1)
		lista1.append(elem2)
	return lista1

def contar(texto, busqueda):
	busca=texto.xpath("//ciudad/text()")
	lista2=[]
	contador1=0
	for elem in busca:
		lista2.append(elem[0])

	for elem in lista2:
		if elem==busqueda:
			contador1=contador1 + 1
	return contador1

def busc_filt(texto, accesorios):
	acc_miras=texto.xpath('//miras/nombre/arma[text()="{}"]/../@nombre'.format(accesorios))
	acc_compensador=texto.xpath('//compensador/nombre/arma[text()="{}"]/../@nombre'.format(accesorios))
	acc_bocacha=texto.xpath('//bocacha/nombre/arma[text()="{}"]/../@nombre'.format(accesorios))
	lista3=[]
	lista3.append(acc_miras)
	lista3.append(acc_bocacha)
	lista3.append(acc_compensador)
	return print("Los accesorios de la arma {} son {}".format(accesorios, lista3))

#def busc_info

#def libre