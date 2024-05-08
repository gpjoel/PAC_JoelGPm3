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


from os import system, name
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen



def clear(): system('cls') if name == 'nt' else system('clear')
# Creació
def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("CLICK", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("X JGP!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])
    screen.wait_for_input(5)  # Esperar 5 segundos
    screen.clear()
    

Screen.wrapper(demo)
persona =	{
  "nom": "Eustaqui",
  "llocNaixement": "Andorra",
  "anyNaixement": 1990
}

# persona = dict(nom = "Anselm", llocNaixement = "Portugal", anyNaixement = 1991)


# Accés
def mostrar_acces_persona(persona):
    """
    persona["nom"] genera un error si la clave no existe. Esta línea de código accede al valor asociado a la clave "nom" en el diccionario persona y lo imprime
    persona.get("nom") devuelve None si la clave no existe. Esta línea utiliza el método .get() de los diccionarios para obtener el valor asociado a la clave "nom"
    """
    print("acceso a diccionario")
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
    input("Prem ENTER per continuar...")

def realitzar_agregats(persona):
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
    input("Prem ENTER per continuar...")
    
def realitzar_eliminacions(persona):
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
    input("Prem ENTER per continuar...")

def mostrar_menu():
    """
    Muestra un menú de opciones para operar con el diccionario.
    """
    clear()
    print("-"*39)
    print("PAC#1 – EL LLIBRE DE LES ACCEPCIONS JGP")
    print("-"*39)
    print("\nMenú d'opcions:")
    print("1. Mostrar accés a elements")
    print("2. Agregar")
    print("3. Realitzar eliminacions")
    print("4. Sortir")

def elegir_opcio(opcion, persona):
    """
    Executa l'opció seleccionada por l'usuario.
    """
    if opcion == 1:
        mostrar_acces_persona(persona)
    elif opcion == 2:
        realitzar_agregats(persona)
    elif opcion == 3:
        realitzar_eliminacions(persona)
    elif opcion == 4:
        print("Sortint del programa...")
        exit()
    else:
        print("Opció no vàlida")


while True:
    clear()
    mostrar_menu()
    opcion = int(input("Posa la opció que vols executar: "))
    elegir_opcio(opcion, persona)
