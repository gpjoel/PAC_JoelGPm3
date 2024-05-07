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
print(persona["nom"])
print(persona.get("nom"))

print(persona.keys())
print(persona.values())
print(persona.items())

# Afegir
    # mitjançant index
    # mitjançant mètode (update())

persona.update({"Ubicacio": "Barcelona"})
persona["pes"] = 80

# Eliminar
    # mitjançant mètode (pop())
persona.pop("llocNaixement")
print(persona)
    # mitjançant mètode (popitem()) en este caso elimina el utlimo del diccionario

persona.popitem()
print(persona)
    # mitjançant paraula clau (del)

del persona["anyNaixement"]
print(persona)

    # mitjançant mètode (clear()) elimina toda la lista 

persona.clear()
print(persona)  
