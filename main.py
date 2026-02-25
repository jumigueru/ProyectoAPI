from api import conectar_api, obtener_datos_de_la_api, diccionario_buscar

from ui import pedir_datos_usuario, mostrar_resultados, menu , informacion_departamentos




def ejecucion_principal():

    opcion = menu()
    if opcion == 1:
        informacion_departamentos()
    else:

        depto, limite = pedir_datos_usuario()

        if depto.isdigit():
            if 1 <= int(depto) <= 28:
                depto = diccionario_buscar(depto)


        cliente = conectar_api()
        df_datos = obtener_datos_de_la_api(cliente, limite, depto)

        mostrar_resultados(df_datos)


if __name__ == "__main__":
    ejecucion_principal()






