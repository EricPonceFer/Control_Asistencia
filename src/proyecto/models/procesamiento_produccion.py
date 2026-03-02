import pandas as pd
import os
from datetime import timedelta
from src.proyecto.config import RUTA_ARCHIVO_PRODUCCION_DEFECTO, RUTA_SALIDA_PRODUCCION_DEFECTO


class ProduccionService:

    def __init__(self, ruta_archivo: str | None = None, ruta_salida: str | None = None,fecha_desde: str | None = None, fecha_hasta: str | None = None):
        """
        Inicializa el servicio con rutas opcionales.
        Si no se proporcionan, usa las rutas por defecto.
        """
        self.ruta_archivo = ruta_archivo or RUTA_ARCHIVO_PRODUCCION_DEFECTO
        self.ruta_salida = ruta_salida or RUTA_SALIDA_PRODUCCION_DEFECTO
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
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
        columnas_requeridas = {"Codigo", "Orden y maquina", "Fecha y hora"}

        if not columnas_requeridas.issubset(df.columns):
            raise ValueError(
                "El archivo no contiene las columnas requeridas: "
                "'Codigo', 'Orden y maquina' y 'Fecha y hora'"
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

        if self.fecha_desde:
            fecha_desde_dt = pd.to_datetime(self.fecha_desde)
            df = df[df["Fecha y hora"] >= fecha_desde_dt]

        if self.fecha_hasta:
            fecha_hasta_dt = pd.to_datetime(self.fecha_hasta) + pd.Timedelta(days=1)
            df = df[df["Fecha y hora"] < fecha_hasta_dt]
        # ==============================
        # CREAR COLUMNAS AUXILIARES
        # ==============================
        df["año"] = df["Fecha y hora"].dt.year
        df["mes"] = df["Fecha y hora"].dt.month
        df["dia"] = df["Fecha y hora"].dt.day
        df["semana"] = df["Fecha y hora"].dt.isocalendar().week

        return df


    # ==============================
    # PROCESAR PRODUCCIÓN
    # ==============================
    def procesar_produccion(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df = df.sort_values(by=["Orden y maquina", "Fecha y hora"])
            resultado = []

            # Separar Orden y Máquina
            df["Orden"] = df["Orden y maquina"].str[:8]
            df["Maquina"] = df["Orden y maquina"].str[-2:]

            for (orden, maquina), grupo in df.groupby(["Orden", "Maquina"]):

                grupo = grupo.sort_values("Fecha y hora").reset_index(drop=True)

                hora_inicio = grupo.loc[0, "Fecha y hora"]
                hora_fin = grupo.loc[len(grupo) - 1, "Fecha y hora"]

                ultimo_operador = grupo.loc[len(grupo) - 1, "Codigo"]

                # Calcular duración total
                diferencia_horas = (hora_fin - hora_inicio).total_seconds() / 3600

                horas_td = timedelta(hours=diferencia_horas)
                horas_formateadas = (
                    f"{int(horas_td.total_seconds() // 3600):02d}:"
                    f"{int((horas_td.total_seconds() % 3600) // 60):02d}"
                )

                # Determinar turno
                hora_inicio_h = hora_inicio.hour
                hora_fin_h = hora_fin.hour

                if 6 <= hora_inicio_h < 18 and 6 <= hora_fin_h < 18:
                    turno = "Día"
                elif (hora_inicio_h >= 18 or hora_inicio_h < 6) and \
                    (hora_fin_h >= 18 or hora_fin_h < 6):
                    turno = "Noche"
                else:
                    turno = "Mixto"

                resultado.append({
                    "Orden": orden,
                    "Máquina": maquina,
                    "Último Operador": ultimo_operador,
                    "Año": hora_inicio.year,
                    "Mes": hora_inicio.month,
                    "Semana": hora_inicio.isocalendar().week,
                    "Día": hora_inicio.day,
                    "Hora_inicio": hora_inicio.time(),
                    "Hora_fin": hora_fin.time(),
                    "Horas_totales": horas_formateadas,
                    "Turno": turno
                })

            return pd.DataFrame(resultado)

        except Exception as e:
            raise RuntimeError(f"Error procesando producción: {e}")


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
    def guardar_produccion(self, df: pd.DataFrame) -> str:
        try:
            nombre_archivo = "Reporte_produccion.xlsx"

            # Construir ruta final
            ruta_final = os.path.join(self.ruta_salida, nombre_archivo)

            if os.path.exists(ruta_final):
                df_existente = pd.read_excel(ruta_final)
                df_final = pd.concat([df_existente, df], ignore_index=True)
            else:
                df_final = df

            df_final.to_excel(ruta_final, index=False)

            return ruta_final

        except Exception as e:
            raise RuntimeError(f"Error guardando archivo: {e}")
    
    def ejecutar_proceso_dataframe(self) -> pd.DataFrame:
        """
        Ejecuta el proceso completo pero retorna el DataFrame resultante
        en lugar de guardarlo. Útil para pruebas unitarias.
        """
        try:
            df = self.cargar_archivo_excel()
            self.validar_columnas(df)
            df = self.preparar_fechas(df)
            df_procesado = self.procesar_produccion(df)
            df_ordenado = self.ordenar_por_fecha(df_procesado)
            return df_ordenado

        except Exception as e:
            raise RuntimeError(f"Error en el proceso completo: {e}")
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
            df_ordenado = self.ejecutar_proceso_dataframe()
            ruta_guardada = self.guardar_produccion(df_ordenado)
            return ruta_guardada

        except Exception as e:
            raise RuntimeError(f"Error en el proceso completo: {e}")