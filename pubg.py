from funciones_xml import lista, contar #busc_filt, busc_info, libre
from lxml import etree

arbol=etree.parse('pubg.xml')


#Ejercicio 1
print("Mostramos la categorias de las distintar armas.")
print("pistolas, escopetas, ametralladoras, arcos, francotirador, francotirador_auto, subfusiles, rifle_asalto.")
categoria=input("Nombre de la categoria: ")

print(lista(arbol, categoria))
print(" ")

#Ejercicio 2
busqueda=input("Dame una letra en máyusculas para buscar las cuidades que hay que empiecen por esa letra: ")
print(contar(arbol, busqueda))
print(" ")

#Ejercicio 3
