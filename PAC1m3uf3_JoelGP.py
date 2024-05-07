# print("hola")

# diccionari = {}

# print(diccionari)

# paraula = "xarxa"
# entrada = {
#   "PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}

# diccionari.update({paraula:entrada})

# print(diccionari)

# auxiliar = diccionari[paraula]

# entrada = {
#   "TÈXTIL" : "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà."}
  
# auxiliar.update(entrada)


# diccionari.update({paraula:auxiliar})

# print(diccionari)




# Creació

persona =	{
  "nom": "Eustaqui",
  "llocNaixement": "Andorra",
  "anyNaixement": 1990
}

# persona = dict(nom = "Anselm", llocNaixement = "Portugal", anyNaixement = 1991)


# Accés
"""
persona["nom"] genera un error si la clave no existe. Esta línea de código accede al valor asociado a la clave "nom" en el diccionario persona y lo imprime
persona.get("nom") devuelve None si la clave no existe. Esta línea utiliza el método .get() de los diccionarios para obtener el valor asociado a la clave "nom"
"""
print(persona["nom"])
print(persona.get("nom"))
"""
persona.keys()  imprime las claves del diccionario persona. El método .keys() devuelve una vista de todas 
las claves en el diccionario. Es útil cuando necesitas iterar sobre las claves del diccionario o realizar 
operaciones específicas con ellas.

persona.values() Esta línea imprime los valores del diccionario persona. El método .values() devuelve una 
vista de todos los valores en el diccionario. Es útil cuando necesitas trabajar solo con los valores y no necesitas las claves.

persona.items() Aquí se imprimen los pares clave-valor del diccionario persona. El método .items() devuelve una vista de tuplas que contienen 
tanto las claves como los valores del diccionario. Cada tupla en la lista representa un par clave-valor del diccionario.

"""
print(persona.keys())
print(persona.values())
print(persona.items())

# Afegir
    # mitjançant index
    # mitjançant mètode (update()) The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
"""
El método update() actualizará el diccionario con los elementos de un argumento dado. Si el elemento no existe, se añadirá el elemento.
"""
persona.update({"Ubicacio": "Barcelona"})
"""
Se añade una entrada al diccionario utilizando una nueva clave de índice y asignando un valor a esta clave:
"""
persona["pes"] = 80

# Eliminar
    # mitjançant mètode (pop())
"""
persona.pop("llocNaixement") elimina la clave "llocNaixement" junto con su valor asociado del diccionario persona.
"""
persona.pop("llocNaixement")
print(persona)
    # mitjançant mètode (popitem()) 
"""
popitem() en este caso elimina  el útlimo término del diccionario
"""

persona.popitem()
print(persona)
    # mitjançant paraula clau (del)

"""
con el del eliminamos algo especificament, en este caso anyNaixement
"""
del persona["anyNaixement"]
print(persona)

    # mitjançant mètode (clear()) elimina toda la lista 
"""
clear()) elimina toda la lista 
"""
persona.clear()
print(persona)  
