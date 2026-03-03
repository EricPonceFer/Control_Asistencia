def generar_formato_semanal(df, ruta_salida):
    try:

        if df.empty:
            raise ValueError("El DataFrame está vacío.")

        columnas_requeridas = [
            "Código", "Año", "Mes", "Semana",
            "Día", "Hora_entrada", "Hora_salida"
        ]

        for col in columnas_requeridas:
            if col not in df.columns:
                raise ValueError(f"Falta la columna: {col}")

        wb = Workbook()
        wb.remove(wb.active)

        dias_semana = ["LUNES", "MARTES", "MIÉRCOLES",
                       "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]

        meses_es = {
            1:"ENERO",2:"FEBRERO",3:"MARZO",4:"ABRIL",
            5:"MAYO",6:"JUNIO",7:"JULIO",8:"AGOSTO",
            9:"SEPTIEMBRE",10:"OCTUBRE",11:"NOVIEMBRE",12:"DICIEMBRE"
        }

        # 🔹 Agrupar por Año y Semana
        for (anio, semana), grupo_semana in df.groupby(["Año", "Semana"]):

            ws = wb.create_sheet(title=f"{anio}-S{semana}")

            mes = int(grupo_semana["Mes"].iloc[0])
            nombre_mes = meses_es.get(mes, "")

            # 🔹 Obtener lunes real de la semana ISO
            lunes_semana = datetime.fromisocalendar(int(anio), int(semana), 1)

            # 🔹 TÍTULO
            ws.merge_cells(start_row=1, start_column=3, end_row=1, end_column=16)
            ws["C1"] = f"SEMANA {semana} - {nombre_mes} {anio}"
            ws["C1"].alignment = Alignment(horizontal="center")
            ws["C1"].font = Font(bold=True, size=14)

            # 🔹 Encabezado OPERADOR
            ws.merge_cells("A3:A5")
            ws["A3"] = "OPERADOR"
            ws["A3"].alignment = Alignment(horizontal="center", vertical="center")
            ws["A3"].font = Font(bold=True)

            col = 2

            for i, dia_nombre in enumerate(dias_semana):

                fecha_real = lunes_semana.replace() + \
                             (timedelta(days=i))

                numero_dia = fecha_real.day

                # Nombre del día
                ws.merge_cells(start_row=3, start_column=col,
                               end_row=3, end_column=col+1)

                ws.cell(row=3, column=col).value = dia_nombre
                ws.cell(row=3, column=col).alignment = Alignment(horizontal="center")
                ws.cell(row=3, column=col).font = Font(bold=True)

                # Número del día
                ws.merge_cells(start_row=4, start_column=col,
                               end_row=4, end_column=col+1)

                ws.cell(row=4, column=col).value = numero_dia
                ws.cell(row=4, column=col).alignment = Alignment(horizontal="center")

                # Entrada / Salida
                ws.cell(row=5, column=col).value = "ENTRADA"
                ws.cell(row=5, column=col+1).value = "SALIDA"

                col += 2

            # 🔹 Insertar datos
            fila_excel = 6

            for codigo, grupo_operador in grupo_semana.groupby("Código"):

                ws.cell(row=fila_excel, column=1).value = codigo
                col = 2

                for i in range(7):

                    fecha_real = lunes_semana + \
                                 timedelta(days=i)

                    dia_num = fecha_real.day

                    registro = grupo_operador[grupo_operador["Día"] == dia_num]

                    if not registro.empty:
                        ws.cell(row=fila_excel, column=col).value = str(registro.iloc[0]["Hora_entrada"])
                        ws.cell(row=fila_excel, column=col+1).value = str(registro.iloc[0]["Hora_salida"])

                    col += 2

                fila_excel += 1

            # Ajustar ancho columnas
            for i in range(1, 17):
                ws.column_dimensions[get_column_letter(i)].width = 14

        wb.save(ruta_salida)

    except PermissionError:
        raise RuntimeError("No se pudo guardar el archivo. Cierra el Excel si está abierto.")

    except Exception as e:
        raise RuntimeError(f"Error generando formato semanal: {e}")

import pandas as pd
from datetime import time

# 🔹 Simular datos de prueba
data = [
    {"Código": "OP001", "Año": 2025, "Mes": 3, "Semana": 10, "Día": 3,
     "Hora_entrada": time(8, 0), "Hora_salida": time(17, 0)},

    {"Código": "OP001", "Año": 2025, "Mes": 3, "Semana": 10, "Día": 4,
     "Hora_entrada": time(8, 5), "Hora_salida": time(16, 55)},

    {"Código": "OP002", "Año": 2025, "Mes": 3, "Semana": 10, "Día": 3,
     "Hora_entrada": time(7, 50), "Hora_salida": time(17, 10)},

    {"Código": "OP001", "Año": 2025, "Mes": 3, "Semana": 11, "Día": 10,
     "Hora_entrada": time(8, 0), "Hora_salida": time(17, 0)},

    {"Código": "OP002", "Año": 2025, "Mes": 3, "Semana": 11, "Día": 11,
     "Hora_entrada": time(9, 0), "Hora_salida": time(18, 0)},
]

df_prueba = pd.DataFrame(data)

# 🔹 Ruta donde se guardará el archivo
ruta_salida = "reporte_semanal_prueba.xlsx"

# 🔹 Llamar función
generar_formato_semanal(df_prueba, ruta_salida)

print("Archivo generado correctamente:", ruta_salida)