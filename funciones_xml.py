#Ejercicio listar munición del arma
def lista(texto, arma):
	armas=texto.xpath("//nombre/text()")
	for elem in armas:
		if elem==arma:
			cargador=texto.xpath("//cargador/text()")
			return cargador

#def contar

#def busc_filt

#def busc_info

#def libre