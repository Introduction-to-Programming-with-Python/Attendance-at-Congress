#   Funcion 1.
def cargar_datos(nombre_archivo:str)->list:
    
    """
    
    Parameters
    ----------
    nombre_archivo : str
        Archivo que contiene la información de la asistencia a sesiones en la
        Cámara de Representantes.

    Returns
    -------
    list
        Lista de diccionarios que contiene información de los congresistas, y
        dentro de estos, su respectivo diccionario de asistencias.

    """
    
    #   Inicializacion de variables necesarias.
    
    data = []
    data_asistencia = []
    info_basica = {}
    info_asistencia = {}
    
    #   Lecuta de archivo.
    
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    linea = archivo.readline().replace("\n", "").split(",")
    
    linea = archivo.readline()
    
    #   Inicialmente se creo el diccionario con toda la informacion de cada
    #   cada congresista pero con su respectivo diccionario de asistencias 
    #   vacio.
    
    while len(linea) > 0:
    
        datos_linea = linea.replace("\n", "").split(",")
    
        nombre = datos_linea[0]
        info_basica["nombre"] = nombre
    
        partido = datos_linea[1]
        info_basica["partido"] = partido
    
        circunscripcion = datos_linea[2]
        info_basica["circunscripcion"] = circunscripcion
    
        info_basica["plenaria"] = {}

        info_basica["congreso_pleno"] = {}
    
        fecha = datos_linea[3]
        estado_asistencia = datos_linea[5]
    
        info_asistencia[fecha] = estado_asistencia
        data_asistencia.append(info_asistencia)
        info_asistencia = {}
        
        if info_basica not in data:
            data.append(info_basica)
    
    
        info_basica = {}
        linea = archivo.readline()
    
    archivo.close()
    
    #   Se vuelve a abrir el archivo para leerse completamente de nuevo.
    
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    
    linea = archivo.readline()
    linea = archivo.readline()
    datos_linea = linea.replace("\n", "").split(",")
    
    #   Inicializacion de variables.
    
    dic_congresista_nombre = datos_linea[0]
    fecha = datos_linea[3]
    asistencia = datos_linea[5]
    tipo = datos_linea[4]
    avance = 0
    dic_congresista = {}
    
    #   Con este ciclo se completa la lista de diccionarios cargando a los
    #   congresistas sus respectivas asistencias.
    
    while len(linea) > 0:
    
    
            if dic_congresista_nombre == datos_linea[0]:
            
                dic_congresista = data[avance]
                dic_congresista_nombre = dic_congresista["nombre"]
                dic_congresista_plenaria = dic_congresista["plenaria"]
                dic_congresista_congreso_pleno = dic_congresista["congreso_pleno"]

                fecha = datos_linea[3]
                tipo = datos_linea[4]
                asistencia = datos_linea[5]

                if tipo == "congreso_pleno":
    
                    dic_congresista_congreso_pleno[fecha] = asistencia
    
                    linea = archivo.readline()
                    datos_linea = linea.replace("\n", "").split(",")

                else:
                    dic_congresista_plenaria[fecha] = asistencia

                    linea = archivo.readline()
                    datos_linea = linea.replace("\n", "").split(",")
    
            else:
            
                avance += 1
    
                dic_congresista = data[avance]
                dic_congresista_nombre = dic_congresista["nombre"]
                dic_congresista_plenaria = dic_congresista["plenaria"]
                dic_congresista_congreso_pleno = dic_congresista["congreso_pleno"]
    
                if tipo == "congreso_pleno":
    
                    dic_congresista_congreso_pleno[fecha] = asistencia
    
                    linea = archivo.readline()
                    datos_linea = linea.replace("\n", "").split(",")

                else:
                    dic_congresista_plenaria[fecha] = asistencia

                    linea = archivo.readline()
                    datos_linea = linea.replace("\n", "").split(",")
    
    archivo.close()

    return data

def inasistencias_congreso_pleno(datos_congresistas:list)->dict:

    diccionario = {}

    for i in datos_congresistas:
        dic_congresista = i
        dic_congresista_nombre = dic_congresista["nombre"]
        diccionario[dic_congresista_nombre] = 0

    for i in datos_congresistas:
        dic_congresista = i
        nombre = dic_congresista["nombre"]
        dic_congreso_pleno = dic_congresista["congreso_pleno"]

        for l in dic_congreso_pleno.values():
            if l != "ASISTIÓ":
                diccionario[nombre] += 1

    return diccionario

def congresistas_que_faltaron_más_de_una_sesión(datos_congresistas:list)->list:

    diccionario = inasistencias_congreso_pleno(cargar_datos("./data.csv"))
    lista = []
    contador = 0

    while contador in range(0, len(diccionario)):
        for i in diccionario:
            nombre = i
            inasistencias = diccionario[nombre]
            if inasistencias > 1:
                lista.append(nombre)
            contador += 1

    return lista

def congresistas_con_mas_fallas(datos_congresistas:list)->str:

    diccionario = inasistencias_congreso_pleno(cargar_datos("./data.csv"))
    maximo = 0
    lista = []
    cadena = "{}, {}, {}"

    for i in diccionario:
        nombre = i
        inasistencias = diccionario[nombre]
        if inasistencias > maximo:
            maximo = inasistencias

    while len(lista) <= 3:
        for i in diccionario:
            nombre = i
            inasistencias = diccionario[nombre]
            if inasistencias == maximo:
                lista.append(nombre)

    n1 = lista[0]
    n2 = lista[1]
    n3 = lista[2]

    cadena = cadena.format(n1,n2,n3)

    return cadena