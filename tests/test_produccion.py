import pandas as pd
import tempfile
import os
from src.proyecto.models.procesamiento_produccion import ProduccionService


def test_procesar_produccion_basico():
    # Crear datos de prueba
    data = {
        "Codigo": ["OP1", "OP1", "OP2"],
        "Orden y maquina": ["12345678AA", "12345678AA", "12345678AA"],
        "Fecha y hora": [
            "2024-01-10 07:00:00",
            "2024-01-10 15:00:00",
            "2024-01-10 16:00:00",
        ]
    }

    df_test = pd.DataFrame(data)

    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        df_test.to_excel(tmp.name, index=False)
        ruta_temp = tmp.name

    try:
        # Instanciar servicio
        service = ProduccionService(ruta_archivo=ruta_temp)

        df_resultado = service.ejecutar_proceso_dataframe()

        # 🔎 Validaciones
        assert not df_resultado.empty
        assert "Orden" in df_resultado.columns
        assert "Máquina" in df_resultado.columns
        assert "Último Operador" in df_resultado.columns

        # Validar valores esperados
        fila = df_resultado.iloc[0]

        assert fila["Orden"] == "12345678"
        assert fila["Máquina"] == "AA"
        assert fila["Último Operador"] == "OP2"
        assert fila["Turno"] == "Día"

    finally:
        os.remove(ruta_temp)

def test_turno_noche():
    data = {
        "Codigo": ["OP1", "OP1"],
        "Orden y maquina": ["87654321BB", "87654321BB"],
        "Fecha y hora": [
            "2024-01-10 19:00:00",
            "2024-01-11 02:00:00",
        ]
    }

    df_test = pd.DataFrame(data)

    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
        df_test.to_excel(tmp.name, index=False)
        ruta_temp = tmp.name

    try:
        service = ProduccionService(ruta_archivo=ruta_temp)
        df_resultado = service.ejecutar_proceso_dataframe()

        assert df_resultado.iloc[0]["Turno"] == "Noche"

    finally:
        os.remove(ruta_temp)