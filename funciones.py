
SECTOR = ["centro", "colina", "industrias"]


def registrar_pedido(cilindros):
    nombre = input("ingrese su nombre y apellido :  ")
    direccion = input("ingrese su direccion : ")
    sector = input ("ingrese la comuna donde vive (centro, colina, industrias) :  ")
    while sector not in SECTOR:
        sector = input ("ingrese la comuna donde vive : ")
    tamaño = int(input("selecione el tamaño del cilintro de 5, 15 y 45 kilos. : "))
    cilindro = int(input(" cantidad de cilindros a pedir : "))
 
   
    cilindros.append({
            'nombre':nombre,
            'direccion':direccion,
            'sector':sector,
            'tamaño':tamaño,
            'cilindro':cilindro
    
    })
  
     
def listar_pedido(cilindros):
      for cilindro in cilindros:
        print(cilindro)
        return
      

def imprimir_hoja_ruta(cilindros):
   try:
    registro_pedidos = input("presione Enter para imprimir lista completa, o escriba la comuna para seleccionar por sector ").lower()
    if registro_pedidos == "":
        for registro_pedidos in cilindros:
         print(cilindros)
    elif registro_pedidos in SECTOR:
        for lugar in SECTOR:
            if lugar == SECTOR:
               print(cilindros)
    else : 
        print("sector no valido ")
        return
   except:

    with open('cilindros.txt','r')as archivo:
       archivo.load = 'listapedido.txt'
       print(cilindros)

    with open('cilindros.txt','w')as archivo:
     archivo.write(f"nombre y apellido cliente :{cilindros['nombre']}\n")
     archivo.write(f"direcion ingresada  :{cilindros['direccion']}\n")
     archivo.write(f"sector :{cilindros['sector']}\n")
     archivo.write(f"cantidad de cilindros  :{cilindros['cilindro']}\n")
     archivo.write(f"tamaño del cindro:{cilindros['tamaño']}\n")
     


    



  