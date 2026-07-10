def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1.1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. 6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese opcion :"))
            if opcion >= 1 and opcion <=6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

def buscar_codigo (codigo, productos):
    codigo = codigo.strip().upper()
    if codigo in productos:
        return True
    else:
        return False
    
def unidades_categoria(categoria, productos, stock):
    total_unidades = 0
    categoria = categoria.strip().lower()
    for codigo in productos:
        categoria_producto = productos[codigo][1].lower()
        if categoria_producto == categoria:
            unidades = stock[codigo][1]
            total_unidades = total_unidades + unidades
    print("El total de unidades disponibles es: ", total_unidades)

def busqueda_precio (p_min, p_max, productos, stock):
    encontrados = []
    
    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]

        if precio >= p_min and precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            encontrados.apprend(nombre + "-" + codigo)
    
    encontrados.sort()

    if len(encontrados) > 0:
        print("Los productos encontrados son: ", encontrados)
    else:
        print("No hay productos en este rango de precio")

def actualizar_precio(codigo, nuevo_precio, productos, stock):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, productos):
        stock [codigo][0] = nuevo_precio
        return True
    else:
        return False
    
def validar_codigo(codigo):
    if codigo.strip() != "":
        return True
    else:
        return False

def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
def validar_categoria(categoria):
    if categoria.strip() != "":
        return True
    else:
        return False
def validar_marca(marca):
    if marca.strip() != "":
        return True
    else:
        return False

def validar_peso(peso_kg):
    if peso_kg > 0:
        return True
    else:
        return False

def validar_importado(es_importado):
    if es_importado == "s" or es_importado == "n":
        return True
    else:
        return False
    
def validar_cachorro(es_para_cachorro):
    if es_para_cachorro == "s" or es_para_cachorro =="n":
        return True
    else:
        return False
    
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
    
def validar_unidades(unidades):
    if unidades >= 0:
        return True
    else:
        return False
    
def agregar_producto (
        codigo,
        nombre,
        categoria,
        marca,
        peso_kg,
        es_importado,
        es_para_cachorro,
        precio,
        unidades,
        productos,
        stock
):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo,productos):
        return False
    
    productos[codigo] = [
        nombre.strip(),
        categoria.strip(),
        marca.strip(),
        peso_kg.strip(),
        es_importado,
        es_para_cachorro
    ]

    stock[codigo] = [precio, unidades]
    return True

def eliminar_producto(codigo, productos , stock):
    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, productos):
        del productos[codigo]
        del stock[codigo]
        return True
    else:
        return False
    
def main():
    productos= {
        "M001": ["Alimento Premium", "comida", "DogPlus", "10", "True", False],
        "M002": ["Arena Aglomerante", "Higiene", "CatClean", "8", "False", "False"],
        "M003": ["Snack Dental", "snack", "BiteJoy", "1", "True", "True"],
        "M004": ["Shampoo suave", "higiene", "Petcare", "0.5", "False", "True"],
        "M005": ["Correa Nylon", "accesorio", "WalkPro", "0.3", "True", "False"],
        "M006":["Cama mediana", "accesorio", "CozyPet", "2", "False", "False"],
    }

    stock = {
        "M001": [32990, 12],
        "M002": [9990, 0],
        "M003": [5490, 25],
        "M004": [7990, 5],
        "M005": [11990, 7],
        "M006": [24990, 3,]
    }
    while True:
        mostrar_menu()
        opcion= leer_opcion()
        if opcion ==1:
            categoria= input("Ingrese categoria a consultar :")
            unidades_categoria(
                categoria,
                productos,
                stock
            )
        elif opcion ==2:
            while True:
                try:
                    precio_minimo =int(input("Ingrese precio minimo :"))
                    precio_maximo= int(input("Ingrese precio maximo: "))
                    if (
                        precio_minimo >= 0
                        and precio_maximo >= 0
                        and precio_minimo <= precio_maximo
                    ):
                        break
                    else:
                        print("El precio minimo debe ser mayor o igual a cero"
                              "y menor o igual que el precio maximo"
                        )
                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_precio(
                precio_minimo,
                precio_maximo,
                productos,
                stock
             )
       
        elif opcion ==3:
                continuar ="s"
                while continuar == "s":
                    
                    codigo = input("Ingrese el codigo del producto: ").strip().upper()
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio"))
                        if nuevo_precio <= 0:
                          print("El nuevo precio debe ser un entero positivo")
                        else:
                             resultado = actualizar_precio(
                                 codigo,
                                nuevo_precio,
                                productos,
                                stock,
                              )
                             if resultado:
                                print("Precio actualizado")
                             else:
                                print("El codigo no existe")
                    
                    except ValueError:
                        print("El nuevo preico debe ser un numero entero positivo")

                    while True:
                        continuar = input("Desea actualizar otro precio? s/n").strip().lower()
                        if continuar == "s" or continuar =="n":
                            break
                        else:
                            print("Debe ingresar s o n")
        elif opcion ==4:
                codigo = input("Ingrese codigo del producto").strip().upper()
                nombre = input("Ingrese el nombre :")
                categoria= input("Ingrese cateogoria: ")
                marca= input("Ingrese marca :")
                peso_valido = True
                precio_valido = True
                unidades_validas = True
        
                try:
                    peso_kg = float(input("Ingrese peso en kg :"))
                except ValueError:
                    peso_kg = 0
                    peso_valido= False
                es_importado_texto = input("Es importado? s/n").strip().lower()
                es_cachorro_texto = input("Es para cachorro? s/n").strip().lower()
                try:
                    precio= int(input("Ingrese el precio: "))
                except ValueError:
                    precio = 0
                    precio_valido = False
                try:
                    unidades = int(input("Ingrese unidades"))
                except ValueError:
                    unidades = -1
                    unidades_validas= False
                todos_validos= True
                if not validar_codigo(codigo):
                    print("Error el codigo no puede estar vacio")
                    todos_validos = False
                elif buscar_codigo(codigo, productos):
                    print("Error el codigo no existe")
                    todos_validos= False
                if not validar_nombre (nombre):
                    print("Error el nombre no puede quedar vacio")
                    todos_validos = False
                if not validar_categoria (categoria):
                    print("Error la categoria no puede estar vacia")
                    todos_validos = False
                if not validar_marca(marca):
                    print("Error la marca no puede estar vacia")
                    todos_validos= False
                if not peso_valido or not validar_peso(peso_kg):
                    print("Error el peso debe ser un numero mayor que 0")
                    todos_validos = False
                if not validar_importado (es_importado_texto):
                    print("Error  debe ingresar s o n")
                    todos_validos = False
                if not validar_cachorro(es_cachorro_texto):
                    print("Error debe ingresar S o n")
                    todos_validos = False
                if not precio_valido or not validar_precio(precio):
                    print("Error el precio debe ser un entero mayor que 0")
                    todos_validos= False
                if not unidades_validas or not validar_precio(precio):
                    print("Error")
                    todos_validos= False
                if not unidades_validas or not validar_unidades(unidades):
                    print("error")
                    todos_validos = False
                if todos_validos:
                    if es_importado_texto =="s":
                        es_importado = True
                    else:
                        es_importado = False
                    if es_cachorro_texto == "s":
                        es_para_cachorro = True
                    else:
                        es_para_cachorro = False
                    
                    resultado = agregar_producto(
                        codigo,
                        nombre,
                        categoria,
                        marca,
                        peso_kg,
                        es_importado,
                        es_para_cachorro,
                        precio,
                        unidades,
                        productos,
                        stock
                    )
                    if resultado:
                        print("producto agregado")
                    else:
                        print("El producto no fue agregado")
                elif opcion == 5:
                    codigo = input("Ingrese codigo del producto que desea eliminar").strip().lower()
                    resultado = eliminar_producto(
                        codigo,
                        productos,
                        stock
                    )
                if resultado:
                    print("Producto eliminado")
                else:
                    print("El codigo no existe")
        elif opcion == 6:
            print("Programa finalizado")
            break
main()
                
                
                

                
                    
        


        



        





                        


                    


                  
    

    


    


