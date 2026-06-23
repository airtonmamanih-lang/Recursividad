import mysql.connector
def sugerirLibros(listaIndices,posActual,libros,cursor,conexion):
    if posActual>=len(listaIndices):
        print("\nNo se encontraron mas sugerencias.")
        return
    indiceLibrosActual=listaIndices[posActual]
    tituloRec=libros[indiceLibrosActual][1]
    autorRec=libros[indiceLibrosActual][2]
    cateRec=libros[indiceLibrosActual][3]
    dispo=libros[indiceLibrosActual][4]
    if dispo>0:
        rpta=input(f"El libro {tituloRec} del autor {autorRec} pertenece a la misma categoria {cateRec} del libro que se busco inicialmente, desea solicitarlo? (s/n): ")
        if rpta=='s':
            queryActu="UPDATE modulo1 SET UnidadesDisponibles=UnidadesDisponibles-1 WHERE Titulo=%s and Autor=%s;"
            cursor.execute(queryActu,(tituloRec,autorRec))
            conexion.commit()
            libros[indiceLibrosActual][4]=libros[indiceLibrosActual][4]-1
            print("Reserva efectuada.")
            return 
        else:
            sugerirLibros(listaIndices,posActual+1,libros,cursor,conexion)
    else:
        sugerirLibros(listaIndices,posActual+1,libros,cursor,conexion)
libros=[]
try:
    conexion=mysql.connector.connect(
        host=" ",
        user=" ",
        password=" ",
        database=" "
    )
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
        cursor=conexion.cursor()
        query="SELECT NumeroLibro, Titulo, Autor, Categoria, UnidadesDisponibles FROM modulo1;"
        cursor.execute(query)
        datosC=cursor.fetchall()
        libros=[list(fila) for fila in datosC]

    if len(libros)>0:
        print("\nIniciando procesamiento de algoritmo de biblioteca...\n")

    while True:
        tit=input("Ingrese el nombre del libro solicitado (ingrese 'salir' para terminar.):")
        if tit.lower()=='salir':
            print("Saliendo del sistema.")
            break
        aut=input("Ingrese el autor del libro solicitado:")
        valor=False
        for i in range(len(libros)):
            if tit==libros[i][1] and aut==libros[i][2]:
                valor=True
                if libros[i][4]>0:
                    print("Libro disponible, prestamo permitido.")
                    query_actu = """
                    UPDATE modulo1
                    SET UnidadesDisponibles=UnidadesDisponibles-1
                    WHERE Titulo = %s AND Autor = %s
                    """
                    tituloLibro=tit
                    autorLibro=aut
                    cursor.execute(query_actu,(tituloLibro,autorLibro))
                    conexion.commit()
                    print("Prestamo efectuado.")
                    libros[i][4]=libros[i][4]-1
                else:
                    print("Unidades no disponibles del libro",libros[i][1],", del autor",libros[i][2])
                    categoria=libros[i][3]
                    indicesRecomen=[]
                    for j in range(len(libros)):
                        if categoria==libros[j][3] and j!=i:
                            indicesRecomen.append(j)
                    if len(indicesRecomen)>0:
                        print("A continuacion, se muestra un libro de la misma categoria al inicialmente solicitado:")
                        sugerirLibros(indicesRecomen,0,libros,cursor,conexion)
        if valor==False:
            print("Titulo o autor del libro incorrecto, por favor ingrese nuevamente.")
except mysql.connector.Error as error:
    print(f"Error de MySQL: {error}")
finally:
    #Cerrando la conexion
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("\nDatos extraídos satisfactoriamente. Conexión a MySQL cerrada.")