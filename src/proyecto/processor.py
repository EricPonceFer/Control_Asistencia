
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.proyecto.UI.diseño import Ui_MainWindow
from PySide6.QtGui import QIcon, QColor, QBrush, QFont
from PySide6.QtCore import QSize, QDate, QAbstractTableModel, Qt
from PySide6.QtWidgets import QFileDialog
import os
from proyecto.models.procesamiento_asistencia import AsistenciaService
from pathlib import Path

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        base_path = Path(__file__).resolve().parent / "UI" / "resource"
        icon_path = base_path / "carpeta.png"
        self.servicio = AsistenciaService()
        self.ui.btn_archivo.setIcon(QIcon(str(icon_path)))
        self.ui.btn_archivo.setIconSize(QSize(20, 20))
        self.ui.btn_archivo.setText("")
        self.ui.btn_guardar.setIcon(QIcon(str(icon_path)))
        self.ui.btn_guardar.setIconSize(QSize(20, 20))
        self.ui.btn_guardar.setText("")

        self.ui.btn_archivo.clicked.connect(self.seleccionar_archivo)
        self.ui.btn_previsualizar.clicked.connect(self.previsualizar_datos)
        self.ui.btn_guardar.clicked.connect(self.seleccionar_carpeta)
        self.ui.btn_deshacer.clicked.connect(self.restablecer_campos)
        self.ui.btn_crear.clicked.connect(self.crear_asistencia)

    def ejecutar_proceso(self):
        servicio = AsistenciaService()
        ruta = servicio.ejecutar_proceso_completo()
        print("Archivo guardado en:", ruta)

    def seleccionar_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            "",
            "Todos los archivos (*);;Archivos Excel (*.xlsx *.xls);;Archivos CSV (*.csv)"
        )
        if archivo:
            self.ui.ln_Ubicacion.setText(archivo)

    def seleccionar_carpeta(self):
        carpeta = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar carpeta de destino",
            os.path.expanduser("~"),  # abre en carpeta de usuario
            QFileDialog.ShowDirsOnly
        )

        if carpeta:
            self.ui.ln_Guardado.setText(carpeta)

    def previsualizar_datos(self):
        try:
            self.servicio.ruta_archivo = self.ui.ln_Ubicacion.text()
            self.servicio.fecha_desde = self.ui.dt_desde.date().toString("yyyy-MM-dd")
            self.servicio.fecha_hasta = self.ui.dt_hasta.date().toString("yyyy-MM-dd")

            df_ordenado = self.servicio.ejecutar_proceso_dataframe()

            modelo = PandasModel(df_ordenado)
            self.ui.tb_visualizar.setModel(modelo)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def restablecer_campos(self):
        self.ui.ln_Guardado.clear()
        self.ui.ln_Ubicacion.clear()
        self.ui.dt_hasta.setDate(QDate.currentDate())
        self.ui.dt_desde.setDate(QDate(2025, 1, 1))
        self.ui.tb_visualizar.setModel(None)
    
    def crear_asistencia(self):
        try:
            # 🔹 Obtener datos de la UI
            ruta_archivo = self.ui.ln_Ubicacion.text()
            ruta_salida = self.ui.ln_Guardado.text()

            fecha_desde = self.ui.dt_desde.date().toString("yyyy-MM-dd")
            fecha_hasta = self.ui.dt_hasta.date().toString("yyyy-MM-dd")

            # 🔹 Validaciones básicas
            if not ruta_archivo:
                QMessageBox.warning(self, "Error", "Debe seleccionar un archivo.")
                return

            if not ruta_salida:
                QMessageBox.warning(self, "Error", "Debe seleccionar carpeta de guardado.")
                return

            # 🔹 Crear servicio
            self.servicio.ruta_archivo = ruta_archivo
            self.servicio.ruta_salida = ruta_salida
            self.servicio.fecha_desde = fecha_desde
            self.servicio.fecha_hasta = fecha_hasta

            # 🔹 Ejecutar proceso
            ruta_guardada = self.servicio.ejecutar_proceso_completo()

            QMessageBox.information(
                self,
                "Éxito",
                f"Archivo generado correctamente en:\n{ruta_guardada}"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Ocurrió un error:\n{str(e)}"
            )


class PandasModel(QAbstractTableModel):
    def __init__(self, df):
        super().__init__()
        self._df = df

    # -------------------------
    # Dimensiones
    # -------------------------
    def rowCount(self, parent=None):
        return len(self._df)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    # -------------------------
    # Datos
    # -------------------------
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        valor = self._df.iloc[index.row(), index.column()]

        # Mostrar texto
        if role == Qt.DisplayRole:
            return str(valor)

        # Centrar texto
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        # 🎨 Color de fondo según observación
        if role == Qt.BackgroundRole:
            if "Observación" in self._df.columns:
                observacion = self._df.iloc[index.row()]["Observación"]

                if observacion == "Turno válido":
                    return QBrush(QColor(200, 255, 200))  # verde claro

                if observacion == "No cumplió 8 horas":
                    return QBrush(QColor(255, 230, 150))  # amarillo claro

                if observacion == "Posible falta de salida":
                    return QBrush(QColor(255, 180, 180))  # rojo claro

        # 🔤 Negrita en encabezado importante
        if role == Qt.FontRole:
            font = QFont()
            if self._df.columns[index.column()] == "Código":
                font.setBold(True)
            return font

        return None

    # -------------------------
    # Encabezados
    # -------------------------
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._df.columns[section])
            if orientation == Qt.Vertical:
                return str(section + 1)

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        if role == Qt.BackgroundRole:
            return QBrush(QColor(50, 90, 150))  # azul encabezado

        if role == Qt.ForegroundRole:
            return QBrush(Qt.white)

        if role == Qt.FontRole:
            font = QFont()
            font.setBold(True)
            return font

        return None