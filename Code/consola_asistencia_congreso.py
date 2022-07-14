import asistencia_congreso as asis

def ejecutar_cargar_datos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de asistencia de los congresistas
        Retorno: list
            La lista de asistencia por parte de congresistas de la camara de representantes
            a sesiones en el congreso.
    """
    asistencia = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la asistencia: ")
    asistencia = asis.cargar_datos(archivo)
    if len(asistencia)==0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información de la asistencia.")
    else:
        print("Se cargaron las asistencias de los siguientes congresistas a partir del archivo.")
        for elemento in asistencia:
            print(elemento)
    return asistencia

def ejecutar_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias injustificadas.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) faltó (inasistencias) veces a sesiones de forma injustificada"
    """
    print(asis.congresistas_con_mas_fallas(asistencias))
    return None

def ejecutar_mas_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de asistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre_congresista) asistió (asistencias) veces a sesiones del congreso"
    """
    print("Functionality not available")
    return None

def ejecutar_porcentaje_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar el porcentaje de asistencias por cada congresista.
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo porcentaje de asistencia.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (Porcentaje congresista 1)
        (Nombre congresista 2) : (Porcentaje congresista 2)
    """
    print("Functionality not available")
    return None

def ejecutar_mayor_porcentaje_asistencia(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor porcentaje de asistencia
        Se debe mostrar al usuario un mensaje con el siguiente formato:
        El congresista con mayor porcentaje de asistencias es (nombre) con un porcentaje de asistencias de (porcentaje)
    """
    print("Functionality not available")
    return None

def ejecutar_circunscripcion_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la circunscripcion con mayor número de inaasistencias al congreso.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        La circunscripción (nombre circunscripcion) acumuló (número de fallas) fallas
    """
    print("Functionality not available")
    return None

def ejecutar_mas_inasistencias_excusa(asistencias:list)->None:
    """Ejecuta la opción de consultar el congresista con mayor número de inasistencias al congreso con excusa médica.
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre congresista) falló (numero de inasistencias) veces con excusa médica
    """
    print("Functionality not available")
    return None

def ejecutar_mas_X_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar los congresistas que fallan mas de un numero determinado de veces
        Se debe mostrar al usuario el nombre de cada congresista con su respectivo número de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre congresista 1) : (inasistencias congresista 1)
        (Nombre congresista 2) : (inasistencias congresista 2)
        Si el diccionario está vacío debe retornar el siguiente mensaje:
        Ningún congresista supera el limite establecido
    """
    numero_fallas = input("Inserte el numero de fallas desde el cual desea partir: ")
    numero_maximo_fallas = asis.maximo_de_fallas_de_cualquier_tipo(asistencias)
    siga = False

    print("Functionality not available")

def ejecutar_asistencias_partido(asistencias:list)->None:
    """Ejecuta la opción de consultar los porcentajes de asistencias de los partidos politicos
        Se debe mostrar al usuario el nombre de cada partido con su respectivo porcentaje de inasistencias.
        A continuación se muestra un ejemplo de la salida esperada:
        (Nombre partido 1) : (porcentaje partido 1)
        (Nombre partido 2) : (porcentaje partido 2)
    """
    print("Functionality not available")

def ejecutar_fecha_mas_inasistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar la fecha con mayor número de inasistencias
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En la fecha (fecha) hubo (número de inasistencias) fallas
    """
    print("Functionality not available")

def  ejecutar_racha_asistencias(asistencias:list)->None:
    """Ejecuta la opción de consultar congresista con mayor racha de asistencias consecutivas
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        El congresista (nombre congresista) tuvo una racha de (asistencias consecutivas) sesiones consecutivas
    """
    print("Functionality not available")
    return None

def ejecutar_mes_mayor_sesiones(asistencias:list)->None:
    """Ejecuta la opción de consultar el mes y año con mayor numero de sesiones
        El mensaje que se retorna al usuario debe tener el siguiente formato:
        En el mes (mes/año) hubo (número de sesiones) sesiones
    """
    print("Functionality not available")
    return None

def ejecutar_asistio_fecha(asistencias:list):

    """Ejecuta la opción de consultar la asistencia de un congresista en una fecha determinada
        Si el congresista asistió a la sesion de la fecha, se debe mostrar el siguiente mensaje:
            El congresista (nombre congresista) asistió a la sesión de la fecha (dia)/(mes)/(anio)
        Si el congresista no asistio o no habia sesion ese dia, se muestra el siguiente mensaje:
            El congresista no asistio a la sesion o no hubo sesion ese dia
    """
    print("Functionality not available")

    return None

def ejecutar_asistencia_circunscripcion_fecha(asistencias:list)->None:
    
    """Ejecuta la opción de consultar la asistencia por circunscripcion en un mes y año determinado
        Se debe mostrar al usuario cada circunscripcion y su respectiva asistencia como se muestra a continuación:
        "(nombre circunscripcion) : (asistencia)"
    """

    print("Functionality not available")

    return None


def mostrar_menu():
    print("\nOpciones")
    print("1. Cargar el archivo con la asistencia al congreso")
    print("2. Consultar congresista con más inasistencias injustificadas")
    print("3. Consultar congresista con más asistencias")
    print("4. Calcular porcentaje de asistencia de los congresistas")
    print("5. Consultar congresista con mayor porcentaje de asistencia")
    print("6. Consultar la circunscripcion con mas inasistencias")
    print("7. Consultar el congresista con más inasistencias con excusa médica")
    print("8. Consultar congresistas que fallan más de un número determinado de veces")
    print("9. Consultar porcentaje de asistencias por partido político")
    print("10. Consultar fecha con más fallas")
    print("11. Consultar congresista con mayor racha de asistencias")
    print("12. Consutlar mes y año con mayor número de sesiones realizadas")
    print("13. Consultar asistencias de congresista por fecha")
    print("14. Consultar asistencia por circunscripcion por mes y año")
    print("15. Salir de la aplicacion")

def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar  = True
    asistencia = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            asistencia = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 3:
            ejecutar_mas_asistencias(asistencia)
        elif opcion_seleccionada == 4:
            ejecutar_porcentaje_asistencias(asistencia)
        elif opcion_seleccionada == 5:
            ejecutar_mayor_porcentaje_asistencia(asistencia)
        elif opcion_seleccionada == 6:
            ejecutar_circunscripcion_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 7:
            ejecutar_mas_inasistencias_excusa(asistencia)
        elif opcion_seleccionada == 8:
            ejecutar_mas_X_inasistencias(asistencia)
        elif opcion_seleccionada == 9:
            ejecutar_asistencias_partido(asistencia)
        elif opcion_seleccionada == 10:
            ejecutar_fecha_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 11:
            ejecutar_racha_asistencias(asistencia)
        elif opcion_seleccionada == 12:
            ejecutar_mes_mayor_sesiones(asistencia)
        elif opcion_seleccionada == 13:
            ejecutar_asistio_fecha(asistencia)
        elif opcion_seleccionada == 14:
            ejecutar_asistencia_circunscripcion_fecha(asistencia)
        elif opcion_seleccionada == 15:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()