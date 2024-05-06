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

# Eliminar
    # mitjançant mètode (pop())
    # mitjançant mètode (popitem())
    # mitjançant mètode (clear())
    # mitjançant paraula clau (del)