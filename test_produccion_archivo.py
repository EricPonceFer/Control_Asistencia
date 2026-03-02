import os
import pandas as pd
from src.proyecto.models.procesamiento_produccion import ProduccionService


def main():

    # Instanciar servicio
    service = ProduccionService()

    try:
        print("🔄 Ejecutando proceso de producción...")
        
        df_resultado = service.ejecutar_proceso_dataframe()

        print("\n✅ Resultado generado correctamente\n")
        print("Primeras filas del resultado:\n")
        print(df_resultado.head())

        print("\n📊 Información general:")
        print(df_resultado.info())

        # Si quieres guardar resultado
        ruta_guardada = service.ejecutar_proceso_completo()
        print(f"\n💾 Archivo guardado en: {ruta_guardada}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()