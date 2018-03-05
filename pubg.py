from funciones_xml import lista #buscar, busc_filt, busc_info, libre
from lxml import etree

arbol=etree.parse('pubg.xml')


#Ejercicio 1
print("Teniendo en cuenta que el juego tiene las siguientes armas, dime una para saber el tamaño del cargador.")
print("Pistolas: ")
print(arbol.xpath("//armas/pistolas/nombre/text()"))
print("Escopetas: ")
print(arbol.xpath("//armas/escopetas/nombre/text()"))
print("Ametralladoras: ")
print(arbol.xpath("//armas/ametralladoras/nombre/text()"))
print("Arcos: ")
print(arbol.xpath("//armas/arcos/nombre/text()"))
print("Francotirador: ")
print(arbol.xpath("//armas/francotirador/nombre/text()"))
print("Francotirador automatico: ")
print(arbol.xpath("//armas/francotirador_auto/nombre/text()"))
print("Subfusiles: ")
print(arbol.xpath("//armas/subfusiles/nombre/text()"))
print("Rifle de asalto: ")
print(arbol.xpath("//armas/rifle_asalto/nombre/text()"))
arma=input("Nombre del arma: ")
