import pandas as pd

def menu():
    while True:
        print("informacion departamentos(1)")
        print("realizar consulta(2)")
        try:
            opcion = int(input("Elige una opción: "))
            if opcion in [1, 2]:
                return opcion
            else:
                print("Opción inválida. Debe ser 1 o 2.")
        except ValueError:
            print("Error: se debe de ingresar un numero.")



def informacion_departamentos():
    print("si busca algun departamento en particular estos son los nombres aceptados por la api.")
    print("si desea tambien puede poner el numero correspondiente al departamento")
    print(""" 
     1. ANTIOQUIA
     2. ARAUCA
     3. ATLANTICO
     4. BARRANQUILLA
     5. BOGOTA
     6. BOLIVAR
     7. BOYACA
     8. CALDAS
     9. CAQUETA
    10. CARTAGENA
    11. CASANARE
    12. CAUCA
    13. CESAR
    14. CORDOBA
    15. CUNDINAMARCA
    16. GUAJIRA
    17. HUILA
    18. MAGDALENA
    19. META
    20. NARIÑO
    21. NORTE SANTANDER  
    22. QUINDIO
    23. RISARALDA
    24. SANTANDER
    25. STA MARTA D.E.  
    26. SUCRE
    27. TOLIMA
    28. VALLE
    """)

def pedir_datos_usuario():
    departamento = input("Ingrese el nombre del departamento : ").upper()
    while True:
        try:
            limite = int(input("Ingrese el número de registros a consultar: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return departamento, limite


def mostrar_resultados(df):
    if df.empty:
        print("\nNo se encontraron resultados para esa consulta.")
        return


    columnas_req = {
        'ciudad_municipio_nom': 'Ciudad de ubicación',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'fuente_tipo_contagio': 'Tipo',
        'estado': 'Estado',
        'pais_viajo_1_nom': 'País de procedencia'
    }

    columnas_existentes = {k: v for k, v in columnas_req.items() if k in df.columns}


    for col in columnas_req.keys():
        if col not in df.columns:
            df[col] = "N/A"



    df_filtrado = df[list(columnas_req.keys())].rename(columns=columnas_req)

    print("\n" + "=" * 80)
    print(f"{'LISTA':^80}")


    print(df_filtrado.to_string(index=False))
    print("=" * 80)


