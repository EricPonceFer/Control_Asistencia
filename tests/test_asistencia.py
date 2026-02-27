import pandas as pd
import pytest
from datetime import datetime
from src.proyecto.models import AsistenciaService


def crear_dataframe_prueba():
    """
    Simula marcaciones reales:
    - Empleado 1: turno válido (9 horas)
    - Empleado 2: turno inválido (6 horas)
    - Empleado 3: falta salida (>12h)
    """

    data = {
        "Codigo": [1, 1, 2, 2, 3, 3],
        "Fecha y hora": [
            datetime(2025, 2, 1, 6, 0),
            datetime(2025, 2, 1, 15, 0),  # 9h válido

            datetime(2025, 2, 1, 7, 0),
            datetime(2025, 2, 1, 13, 0),  # 6h inválido

            datetime(2025, 2, 1, 6, 0),
            datetime(2025, 2, 2, 8, 0),   # 26h -> falta salida
        ]
    }

    return pd.DataFrame(data)


def test_procesamiento_asistencia():
    servicio = AsistenciaService(
        ruta_archivo="dummy.xlsx",
        ruta_salida="dummy_salida.xlsx"
    )

    df = crear_dataframe_prueba()

    servicio.validar_columnas(df)
    df = servicio.preparar_fechas(df)
    resultado = servicio.procesar_asistencia(df)

    # Debe haber 3 registros procesados
    assert len(resultado) == 3

    # Turno válido
    assert resultado.loc[0, "Observación"] == "Turno válido"

    # Turno inválido (<8h)
    assert resultado.loc[1, "Observación"] == "No cumplió 8 horas"

    # Falta de salida
    assert resultado.loc[2, "Observación"] == "Posible falta de salida"


def test_validacion_columnas_incorrectas():
    servicio = AsistenciaService()

    df = pd.DataFrame({"col1": [1, 2]})

    with pytest.raises(ValueError):
        servicio.validar_columnas(df)