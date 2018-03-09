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
	cadena1=", ".join(acc_miras)
	cadena2=", ".join(acc_compensador)
	cadena3=", ".join(acc_bocacha)
	cadena4=cadena1+", "+cadena2+", "+cadena3
	return print("Los accesorios de la arma {} son {}".format(accesorios, cadena4))

def busc_info(texto, arma, categoria):
	nombre=texto.xpath('//armas/{}/nombre[text()="{}"]/@danio'.format(categoria, arma))
	nombre2=("El daño del arma es {}".format(nombre[0]))
	return nombre2