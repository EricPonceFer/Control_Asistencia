import pandas as pd
import os
from datetime import timedelta
from src.proyecto.config import RUTA_ARCHIVO_DEFECTO, RUTA_SALIDA_DEFECTO


class AsistenciaService:

    def __init__(self, ruta_archivo: str | None = None, ruta_salida: str | None = None):
        """
        Inicializa el servicio con rutas opcionales.
        Si no se proporcionan, usa las rutas por defecto.
        """
        self.ruta_archivo = ruta_archivo or RUTA_ARCHIVO_DEFECTO
        self.ruta_salida = ruta_salida or RUTA_SALIDA_DEFECTO


    # ==============================
    # CARGAR ARCHIVO
    # ==============================
    def cargar_archivo_excel(self) -> pd.DataFrame:
        if not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(
                f"El archivo no existe en la ruta: {self.ruta_archivo}"
            )

        try:
            df = pd.read_excel(self.ruta_archivo)
            return df
        except Exception as e:
            raise RuntimeError(f"Error al cargar el archivo: {e}")


    # ==============================
    # VALIDAR COLUMNAS
    # ==============================
    def validar_columnas(self, df: pd.DataFrame) -> None:
        columnas_requeridas = {"Codigo", "Fecha y hora"}

        if not columnas_requeridas.issubset(df.columns):
            raise ValueError(
                "El archivo no contiene las columnas requeridas: "
                "'Codigo' y 'Fecha y hora'"
            )


    # ==============================
    # PREPARAR FECHAS
    # ==============================
    def preparar_fechas(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df["Fecha y hora"] = pd.to_datetime(df["Fecha y hora"])
        except Exception:
            raise ValueError(
                "La columna 'Fecha y hora' no tiene un formato válido."
            )

        df["año"] = df["Fecha y hora"].dt.year
        df["mes"] = df["Fecha y hora"].dt.month
        df["dia"] = df["Fecha y hora"].dt.day
        df["semana"] = df["Fecha y hora"].dt.isocalendar().week

        return df


    # ==============================
    # PROCESAR ASISTENCIA
    # ==============================
    def procesar_asistencia(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df = df.sort_values(by=["Codigo", "Fecha y hora"])
            resultado = []

            for codigo, grupo in df.groupby("Codigo"):

                grupo = grupo.sort_values("Fecha y hora").reset_index(drop=True)
                i = 0

                while i < len(grupo) - 1:

                    hora_entrada = grupo.loc[i, "Fecha y hora"]
                    hora_salida = grupo.loc[i + 1, "Fecha y hora"]

                    diferencia_horas = (
                        hora_salida - hora_entrada
                    ).total_seconds() / 3600

                    # 🔴 Caso: posible falta de salida
                    if diferencia_horas > 12:
                        resultado.append({
                            "Código": codigo,
                            "Año": hora_entrada.year,
                            "Mes": hora_entrada.month,
                            "Semana": hora_entrada.isocalendar().week,
                            "Día": hora_entrada.day,
                            "Hora_entrada": hora_entrada.time(),
                            "Hora_salida": None,
                            "Horas_trabajadas": "00:00",
                            "Observación": "Posible falta de salida"
                        })
                        i += 1
                        continue

                    # 🔵 Caso válido
                    horas_td = timedelta(hours=diferencia_horas)

                    horas_formateadas = (
                        f"{int(horas_td.total_seconds() // 3600):02d}:"
                        f"{int((horas_td.total_seconds() % 3600) // 60):02d}"
                    )

                    observacion = (
                        "Turno válido"
                        if diferencia_horas >= 8
                        else "No cumplió 8 horas"
                    )

                    resultado.append({
                        "Código": codigo,
                        "Año": hora_entrada.year,
                        "Mes": hora_entrada.month,
                        "Semana": hora_entrada.isocalendar().week,
                        "Día": hora_entrada.day,
                        "Hora_entrada": hora_entrada.time(),
                        "Hora_salida": hora_salida.time(),
                        "Horas_trabajadas": horas_formateadas,
                        "Observación": observacion
                    })

                    i += 2

            return pd.DataFrame(resultado)

        except Exception as e:
            raise RuntimeError(f"Error procesando asistencia: {e}")


    # ==============================
    # ORDENAR
    # ==============================
    def ordenar_por_fecha(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            return df.sort_values(
                by=["Año", "Mes", "Día"]
            ).reset_index(drop=True)
        except Exception as e:
            raise RuntimeError(f"Error ordenando datos: {e}")


    # ==============================
    # GUARDAR
    # ==============================
    def guardar_asistencia(self, df: pd.DataFrame) -> str:
        try:
            if os.path.exists(self.ruta_salida):
                df_existente = pd.read_excel(self.ruta_salida)
                df_final = pd.concat([df_existente, df], ignore_index=True)
            else:
                df_final = df

            df_final.to_excel(self.ruta_salida, index=False)

            return self.ruta_salida

        except Exception as e:
            raise RuntimeError(f"Error guardando archivo: {e}")
        
    # ==============================
    # PROCESO COMPLETO
    # ==============================
    def ejecutar_proceso_completo(self) -> str:
        """
        Ejecuta todo el flujo:
        - Cargar archivo
        - Validar columnas
        - Preparar fechas
        - Procesar asistencia
        - Ordenar resultados
        - Guardar archivo
        
        Retorna la ruta donde se guardó el archivo.
        """
        try:
            df = self.cargar_archivo_excel()

            self.validar_columnas(df)

            df = self.preparar_fechas(df)

            df_procesado = self.procesar_asistencia(df)

            df_ordenado = self.ordenar_por_fecha(df_procesado)

            ruta_guardada = self.guardar_asistencia(df_ordenado)

            return ruta_guardada

        except Exception as e:
            raise RuntimeError(f"Error en el proceso completo: {e}")