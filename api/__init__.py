import pandas as pd
from sodapy import Socrata

import pandas as pd
from sodapy import Socrata

def diccionario_buscar(indice):
    diccionario_regiones = {
        1: "ANTIOQUIA",
        2: "ARAUCA",
        3: "ATLANTICO",
        4: "BARRANQUILLA",
        5: "BOGOTA",
        6: "BOLIVAR",
        7: "BOYACA",
        8: "CALDAS",
        9: "CAQUETA",
        10: "CARTAGENA",
        11: "CASANARE",
        12: "CAUCA",
        13: "CESAR",
        14: "CORDOBA",
        15: "CUNDINAMARCA",
        16: "GUAJIRA",
        17: "HUILA",
        18: "MAGDALENA",
        19: "META",
        20: "NARIÑO",
        21: "NORTE SANTANDER",
        22: "QUINDIO",
        23: "RISARALDA",
        24: "SANTANDER",
        25: "STA MARTA D.E.",
        26: "SUCRE",
        27: "TOLIMA",
        28: "VALLE"
    }
    return diccionario_regiones[int(indice)]




def conectar_api():
    return Socrata("www.datos.gov.co", None)

def obtener_datos_de_la_api(client, limite, departamento):

    departamento_upper = departamento.upper()
    filtro = f"departamento_nom='{departamento_upper}'"
    results = client.get("gt2j-8ykr", limit=limite, where=filtro)
    return pd.DataFrame.from_records(results)

def procesar_a_dataframe_de_pandas(lista_datos):

    df = pd.DataFrame.from_records(lista_datos)
    return df