
import funciones as fn


cilindros = []

while True:
    print("Bienvenido a Gaxplosive")
    print(" ---------o----------")
    print("1. Registrar pedido : ")
    print("2. Listar los todos los pedidos : ")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opccion = int(input("Ingrese una de las opciones : "))

    if opccion == 1:
        fn.registrar_pedido(cilindros)
    elif opccion == 2:
        fn.listar_pedido(cilindros)
    elif opccion == 3:
        fn.imprimir_hoja_ruta(cilindros)
    elif opccion == 4:
        print("Gracias por preferir gaxplosive")
    
