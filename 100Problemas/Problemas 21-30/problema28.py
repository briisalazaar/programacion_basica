class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado exitosamente.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        """Método para retirar dinero de la cuenta."""
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        elif cantidad > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado exitosamente.")

    def consultar_saldo(self):
        """Método para consultar el saldo de la cuenta."""
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")

# Función principal para manejar el menú de la cuenta bancaria
def menu():
    # Crear una cuenta bancaria con un saldo inicial de 0
    nombre = input("Ingrese el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(nombre)

    while True:
        print("\n--- Menú de la Cuenta Bancaria ---")
        print("1. Realizar un depósito")
        print("2. Realizar un retiro")
        print("3. Consultar saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            # Realizar un depósito
            cantidad = float(input("¿Cuánto desea depositar? "))
            cuenta.depositar(cantidad)
        
        elif opcion == '2':
            # Realizar un retiro
            cantidad = float(input("¿Cuánto desea retirar? "))
            cuenta.retirar(cantidad)
        
        elif opcion == '3':
            # Consultar saldo
            cuenta.consultar_saldo()
        
        elif opcion == '4':
            print("¡Gracias por usar nuestro servicio! Hasta luego.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
