from funciones_xml import lista #buscar, busc_filt, busc_info, libre
from lxml import etree

arbol=etree.parse('pubg.xml')

#Ejercicio 1
print("Teniendo en cuenta que el juego tiene las siguientes armas, dime una para saber el tamaño del cargador.")
for elem in arbol:
	print(arbol.xpath("//arma/text()"))
arma=input("Nombre del arma: ")