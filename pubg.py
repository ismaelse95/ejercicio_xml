from funciones_xml import lista, contar, busc_filt #, busc_info, libre
from lxml import etree

arbol=etree.parse('pubg.xml')


#Ejercicio 1
print("Mostramos la categorias de las distintar armas.")
print("pistolas, escopetas, ametralladoras, arcos, francotirador, francotirador_auto, subfusiles, rifle_asalto.")
categoria=input("Nombre de la categoria: ")

print(lista(arbol, categoria))
print("-------------------------------------------------------------")

#Ejercicio 2
busqueda=input("Dame una letra en máyusculas para buscar las cuidades que hay que empiecen por esa letra: ")
print(contar(arbol, busqueda))
print("-------------------------------------------------------------")

#Ejercicio 3
print("Dame el nombre de una de las siguientes armas.")
print("P1911, Tommy Gun, Vector, M16A4, M249, M416, SCAR-L, AKM, kar98k, M24, R1895, SKS, Groza, MK14, AWM, Micro UZI, P92, UMP9, VSS, Glock")
accesorios=input("Nombre: ")
print(" ")
print(busc_filt(arbol, accesorios))
print("-------------------------------------------------------------")

#Ejercicio 4
