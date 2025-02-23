class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return "La pila está vacía"
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return "La pila está vacía"
    
    def tamano(self):
        return len(self.items)

def pila_menu():
    pila = Pila()
    while True:
        print("\n--- Menú Pila ---")
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Ver cima")
        print("4. Ver tamaño")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            item = input("Introduce un elemento para apilar: ")
            pila.apilar(item)
            print(f"Elemento '{item}' apilado.")
        elif opcion == "2":
            print(f"Elemento desapilado: {pila.desapilar()}")
        elif opcion == "3":
            print(f"Cima de la pila: {pila.cima()}")
        elif opcion == "4":
            print(f"Tamaño de la pila: {pila.tamano()}")
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

# Ejecutar el menú de la pila
pila_menu()


