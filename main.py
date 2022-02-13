import operator
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches
from operator import itemgetter

ingreso = False
nombre = ""
password = ""
while (ingreso == False):
    print("Bienvenido al visualizador de datos de  de Lifestore\n")
    print("Ya es usuario? si/no ")
    respuesta = input()

    if respuesta.lower() == "no":
        print("Proceso de alta para nuevo usuario")
        nombre = input("Ingrese su nombre:")
        password = input("Ingrese su contraseña:")
        print("Proceso de alta de usuario " + nombre +
              " ha sido finalizado. Por favor inicie sesion")
        continue

    elif respuesta.lower() == "si":
        nombre1 = input("Ingrese su nombre:")
        password1 = input("Ingrese su contraseña:")
        if (nombre1 == "Katherin" and password1 == "Life22"):
            ingreso = True
        elif (nombre1 == nombre and password1 == password):
            ingreso = True
        else:
            print("Contrseña incorrecta, intente de nuevo")

    else:
        print("Opción invalida.")

print("Bienvenido al sistema de analisis de datos de Lifestore ", nombre1)

on_line = True
while (on_line):
    print("¿Que informacion necesita?")
    print("1.- Generar Lista de los 5 mas vendidos")
    print("2.- Generar Lista de los 10 mas Buscados")
    print("3.- Generar Lista de los 5 menos vendidos por categoria")
    print("4.- Generar Lista de los 10 menos buscados por categoria")
    print("5.- Generar Lista de los 5 con mejores reseñas")
    print("6.- Generar Lista de los 5 con peores reseñas y devolución")
    print("7.- Generar Reporte de ventas")
    print("8.- Salir")

    opcion = input()
    if opcion.isnumeric():
        opcion = int(opcion)

    if opcion == 1:
        """lista de los 5 mas vendidos"""
        lista_top5 = []
        lista_productos_ventas = []
        for i in lifestore_products:
            cantidad_ventas = 0
            for j in lifestore_sales:
                if j[1] == i[0]:
                    cantidad_ventas += 1
            addition = i[1]
            lista_top5.append([
                addition, cantidad_ventas, "Vendidos: " + str(cantidad_ventas)
            ])
            temp = i[:]
            temp.append(cantidad_ventas)
            temp.append("Vendidos: " + str(cantidad_ventas))
            lista_productos_ventas.append(temp)
        sorted_list_50 = sorted(lista_top5,
                                key=operator.itemgetter(1),
                                reverse=True)
        print("Los 5 mas vendidos:")
        for m in sorted_list_50[0:5]:
            print(m)

    elif opcion == 2:
        """lista de los 10 mas buscados"""
        lista10 = []
        lista_productos_busquedas = []
        for i in lifestore_products:
            cantidad_busquedas = 0
            for j in lifestore_searches:
                if j[1] == i[0]:
                    cantidad_busquedas += 1
            lista10.append([i[1], cantidad_busquedas])
            temp1 = i[:]
            temp1.append(cantidad_busquedas)
            temp1.append("Busquedas: " + str(cantidad_busquedas))
            lista_productos_busquedas.append(temp1)

        sorted_list_10 = sorted(lista10,
                                key=operator.itemgetter(1),
                                reverse=True)
        print("Los 10 mas buscados")
        for m in sorted_list_10[0:10]:
            print(m)

    elif opcion == 3:
        """Los 5 menos vendidos por categoria"""
        categorias = []
        lista_top5 = []
        lista_productos_ventas = []
        for i in lifestore_products:
            cantidad_ventas = 0
            for j in lifestore_sales:
                if j[1] == i[0]:
                    cantidad_ventas += 1
            addition = i[1]
            lista_top5.append([
                addition, cantidad_ventas, "Vendidos: " + str(cantidad_ventas)
            ])
            temp = i[:]
            temp.append(cantidad_ventas)
            temp.append("Vendidos: " + str(cantidad_ventas))
            lista_productos_ventas.append(temp)
        sorted_list_50 = sorted(lista_top5,
                                key=operator.itemgetter(1),
                                reverse=True)

        for i in lifestore_products:
            cat = i[3]
            if cat in categorias:
                continue
            else:
                categorias.append(cat)

        for i in categorias:
            print("\nLos 5 menos vendidos, Categoria ", i)
            lista_por_categoria = [
                item for item in lista_productos_ventas if item[3] == i
            ]
            lista_por_categoria = sorted(lista_por_categoria,
                                         key=operator.itemgetter(5),
                                         reverse=False)
            if (len(lista_por_categoria) <= 5):
                print("Categoria solo cuenta con " +
                      str(len(lista_por_categoria)) + " elementos")
                for m in lista_por_categoria:
                    print(m)
            else:
                for m in lista_por_categoria[0:5]:
                    print(m)

    elif opcion == 4:
        """Los 10 menos buscados por categoria"""
        categorias = []
        lista10 = []
        lista_productos_busquedas = []
        for i in lifestore_products:
            cantidad_busquedas = 0
            for j in lifestore_searches:
                if j[1] == i[0]:
                    cantidad_busquedas += 1
            lista10.append([i[1], cantidad_busquedas])
            temp1 = i[:]
            temp1.append(cantidad_busquedas)
            temp1.append("Busquedas: " + str(cantidad_busquedas))
            lista_productos_busquedas.append(temp1)
        for i in lifestore_products:
            cat = i[3]
            if cat in categorias:
                continue
            else:
                categorias.append(cat)
        for i in categorias:
            print("\nLos 10 menos Buscados, Categoria ", i)
            lista_por_categoria = [
                item for item in lista_productos_busquedas if item[3] == i
            ]
            lista_por_categoria = sorted(lista_por_categoria,
                                         key=operator.itemgetter(5),
                                         reverse=False)
            if (len(lista_por_categoria) <= 10):
                print("Categoria solo cuenta con " +
                      str(len(lista_por_categoria)) + " elementos")
                for m in lista_por_categoria:
                    print(m)
            else:
                for m in lista_por_categoria[0:10]:
                    print(m)

    elif opcion == 5:
        ###listado de 5 con mejores reseñas

        lista_top5_reviews = []
        for i in lifestore_products:
            cantidad_ventas = 0
            reviews = 0.0
            for j in lifestore_sales:
                if j[1] == i[0]:
                    cantidad_ventas += 1
                    reviews += j[2]
            if (cantidad_ventas == 0):
                continue
            # print("Reviews: " + str(reviews) +" Cantidad de ventas: "+ str(cantidad_ventas))
            total = reviews / cantidad_ventas
            addition = i[1]
            lista_top5_reviews.append([addition, "Reviews: " + str(total)])
        sorted_list_5 = sorted(lista_top5_reviews,
                               key=operator.itemgetter(1),
                               reverse=True)
        print("Los 5 mejores reviews:")
        for m in sorted_list_5[0:5]:
            print(m)

    elif opcion == 6:
        """listado de 5 con peores reseñas y devolucion"""
        lista_worst5_reviews = []
        lista_devoluciones = [item for item in lifestore_sales if item[4] == 1]
        for i in lifestore_products:
            cantidad_ventas = 0
            reviews = 0
            for j in lista_devoluciones:
                if j[1] == i[0]:
                    cantidad_ventas += 1
                    reviews += j[2]
            if (cantidad_ventas == 0):
                continue
            reviews = reviews / cantidad_ventas
            # print("Reviews: " + str(reviews) +" Cantidad de ventas: "+ str(cantidad_ventas))
            addition = i[1]
            lista_worst5_reviews.append([addition, "Reviews: " + str(reviews)])
        sorted_list_5 = sorted(lista_worst5_reviews,
                               key=operator.itemgetter(1),
                               reverse=False)
        print("Los 5 peores reviews:")
        for m in sorted_list_5[0:5]:
            print(m)

    elif opcion == 7:
        """Reporte de Ganancias"""
        ganancia_meses = [[1, "Enero", 0], [2, "Febrero", 0], [3, "Marzo", 0],
                          [4, "Abril", 0], [5, "Mayo", 0], [6, "Junio", 0],
                          [7, "Julio", 0], [8, "Agosto", 0],
                          [9, "Septiembre", 0], [10, "Octubre", 0],
                          [11, "Noviembre", 0], [12, "Diciembre", 0]]

        cantidad_ventas = 0
        for i in lifestore_sales:
            mes = 0
            for j in lifestore_products:
                if i[1] == j[0]:
                    cantidad_ventas += j[2]
                    mes = int(i[3][3:5])
                    for k in range(len(ganancia_meses)):
                        if ganancia_meses[k][0] == mes:
                            ganancia_meses[k][2] += j[2]
                            continue
                    continue

        print("Total de ventas anual: " + str(cantidad_ventas) + "$ USD.")
        print("Promedio de ventas mensuales: " + str(cantidad_ventas // 12) +
              "USD")
        sorted_list_meses = sorted(ganancia_meses,
                                   key=operator.itemgetter(2),
                                   reverse=True)
        print("Meses con mas ventas en USD: ")
        for m in sorted_list_meses:
            print(m)

    elif opcion == 8:
        print("Gracias por utilizar el sistema, hasta luego")
        on_line = False
        continue

    else:
        print("Opción no valida, intente de nuevo")

    continuar = input("¿Desea continuar? si/no ")

    if (continuar.lower() == "y"):
        continue
    if (continuar.lower() == "n"):
        print("Gracias por utilizar el sistema, hasta luego ¡excelente día!／")
        on_line = False
