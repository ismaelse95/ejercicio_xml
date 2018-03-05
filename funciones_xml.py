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

#def busc_filt

#def busc_info

#def libre