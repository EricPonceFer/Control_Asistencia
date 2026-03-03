# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Diseño_Aplicacion.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
from PySide6.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(867, 531)
        MainWindow.setFixedSize(867, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuBar = QFrame(self.centralwidget)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setMinimumSize(QSize(150, 0))
        self.MenuBar.setMaximumSize(QSize(180, 16777215))
        self.MenuBar.setStyleSheet(u"\n"
"background-color: rgb(255, 92, 92);")
        self.MenuBar.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.MenuBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.MenuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.MenuBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 111, 91))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    letter-spacing: 1px;\n"
"    padding: 8px 5px;\n"
"}")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.btn_asistencia = QPushButton(self.MenuBar)
        self.btn_asistencia.setObjectName(u"btn_asistencia")
        self.btn_asistencia.setGeometry(QRect(20, 250, 101, 31))
        self.btn_asistencia.setStyleSheet(u"QPushButton {\n"
"    background-color: #2563EB;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    border-radius: 6px;\n"
"    padding: 8px 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1D4ED8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E40AF;\n"
"}\n"
"")
        self.btn_produccion = QPushButton(self.MenuBar)
        self.btn_produccion.setObjectName(u"btn_produccion")
        self.btn_produccion.setGeometry(QRect(20, 300, 101, 31))
        self.btn_produccion.setAutoFillBackground(False)
        self.btn_produccion.setStyleSheet(u"QPushButton {\n"
"    background-color: #3F3F46;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"    padding: 8px 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #52525B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #27272A;\n"
"}")

        self.horizontalLayout.addWidget(self.MenuBar)

        self.EspacioCarga = QFrame(self.centralwidget)
        self.EspacioCarga.setObjectName(u"EspacioCarga")
        self.EspacioCarga.setMinimumSize(QSize(150, 0))
        self.EspacioCarga.setMaximumSize(QSize(16777215, 16777215))
        self.EspacioCarga.setStyleSheet(u"QFrame{background-color: rgb(165, 255, 240);}\n"
"\n"
"QLabel{color:rgb(0, 0, 0);\n"
"	\n"
"	font: 700 14pt \"Verdana\";\n"
"}")
        self.EspacioCarga.setFrameShape(QFrame.Shape.StyledPanel)
        self.EspacioCarga.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.EspacioCarga)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.EspacioCarga)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.TituloAsistencia = QLabel(self.frame)
        self.TituloAsistencia.setObjectName(u"TituloAsistencia")
        self.TituloAsistencia.setGeometry(QRect(130, 20, 431, 41))
        self.TituloAsistencia.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TituloAsistencia.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.EspacioCarga)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-bottom: 2px solid #5DADE2;\n"
"    padding: 6px 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #2E86C1;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom: 2px solid #3498DB;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_Ubicacion = QFrame(self.frame_4)
        self.fr_Ubicacion.setObjectName(u"fr_Ubicacion")
        self.fr_Ubicacion.setStyleSheet(u"#fr_Ubicacion {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #85C1E9;\n"
"    border-radius: 12px;\n"
"}\n"
"")
        self.fr_Ubicacion.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_Ubicacion.setFrameShadow(QFrame.Shadow.Raised)
        self.RutaArchivo = QLabel(self.fr_Ubicacion)
        self.RutaArchivo.setObjectName(u"RutaArchivo")
        self.RutaArchivo.setGeometry(QRect(20, 10, 141, 21))
        self.RutaArchivo.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        self.ln_Ubicacion = QLineEdit(self.fr_Ubicacion)
        self.ln_Ubicacion.setObjectName(u"ln_Ubicacion")
        self.ln_Ubicacion.setEnabled(False)
        self.ln_Ubicacion.setGeometry(QRect(20, 30, 371, 31))
        self.btn_archivo = QPushButton(self.fr_Ubicacion)
        self.btn_archivo.setObjectName(u"btn_archivo")
        self.btn_archivo.setGeometry(QRect(400, 30, 31, 26))

        self.verticalLayout_2.addWidget(self.fr_Ubicacion)

        self.fr_Guardado = QFrame(self.frame_4)
        self.fr_Guardado.setObjectName(u"fr_Guardado")
        self.fr_Guardado.setStyleSheet(u"#fr_Guardado\n"
" {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #85C1E9;\n"
"    border-radius: 12px;\n"
"}\n"
"")
        self.fr_Guardado.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_Guardado.setFrameShadow(QFrame.Shadow.Raised)
        self.RutaArchivo_2 = QLabel(self.fr_Guardado)
        self.RutaArchivo_2.setObjectName(u"RutaArchivo_2")
        self.RutaArchivo_2.setGeometry(QRect(20, 10, 161, 21))
        self.RutaArchivo_2.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        self.ln_Guardado = QLineEdit(self.fr_Guardado)
        self.ln_Guardado.setObjectName(u"ln_Guardado")
        self.ln_Guardado.setEnabled(False)
        self.ln_Guardado.setGeometry(QRect(20, 30, 371, 31))
        self.btn_guardar = QPushButton(self.fr_Guardado)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(400, 30, 31, 26))

        self.verticalLayout_2.addWidget(self.fr_Guardado)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fr_tituloCondicion = QFrame(self.frame_5)
        self.fr_tituloCondicion.setObjectName(u"fr_tituloCondicion")
        self.fr_tituloCondicion.setStyleSheet(u"#fr_tituloCondicion {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #58D68D;\n"
"    border-radius: 12px;\n"
"}")
        self.fr_tituloCondicion.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_tituloCondicion.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.fr_tituloCondicion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 161, 16))

        self.verticalLayout_3.addWidget(self.fr_tituloCondicion)

        self.fr_Condicion = QFrame(self.frame_5)
        self.fr_Condicion.setObjectName(u"fr_Condicion")
        self.fr_Condicion.setStyleSheet(u"#fr_Condicion {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #58D68D;\n"
"    border-radius: 12px;\n"
"}")
        self.fr_Condicion.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_Condicion.setFrameShadow(QFrame.Shadow.Raised)
        self.RutaArchivo_3 = QLabel(self.fr_Condicion)
        self.RutaArchivo_3.setObjectName(u"RutaArchivo_3")
        self.RutaArchivo_3.setGeometry(QRect(20, 20, 41, 21))
        self.RutaArchivo_3.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        self.RutaArchivo_4 = QLabel(self.fr_Condicion)
        self.RutaArchivo_4.setObjectName(u"RutaArchivo_4")
        self.RutaArchivo_4.setGeometry(QRect(20, 60, 41, 21))
        self.RutaArchivo_4.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        self.dt_desde = QDateEdit(self.fr_Condicion)
        self.dt_desde.setObjectName(u"dt_desde")
        self.dt_desde.setGeometry(QRect(70, 20, 123, 26))
        self.dt_desde.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dt_desde.setMaximumDate(QDate.currentDate())
        self.dt_desde.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dt_desde.setCalendarPopup(True)
        self.dt_desde.setCurrentSectionIndex(0)
        self.dt_hasta = QDateEdit(self.fr_Condicion)
        self.dt_hasta.setObjectName(u"dt_hasta")
        self.dt_hasta.setGeometry(QRect(70, 60, 123, 26))
        self.dt_hasta.setCalendarPopup(True)
        self.dt_hasta.setDate(QDate.currentDate())
        self.dt_hasta.setMaximumDate(QDate.currentDate())

        self.verticalLayout_3.addWidget(self.fr_Condicion)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.EspacioCarga)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.tb_visualizar = QTableView(self.frame_6)
        self.tb_visualizar.setObjectName(u"tb_visualizar")
        self.tb_visualizar.setGeometry(QRect(10, 10, 481, 192))

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 10, 141, 181))
        self.frame_8.setStyleSheet(u"#btn_previsualizar {\n"
"    background-color: #9B59B6;\n"
"    color: white;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 9px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"#btn_previsualizar:hover {\n"
"    background-color: #884EA0;\n"
"}\n"
"\n"
"#btn_previsualizar:pressed {\n"
"    background-color: #6C3483;\n"
"}\n"
"\n"
"#btn_deshacer {\n"
"    background-color: #E74C3C;\n"
"    color: white;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 10px;\n"
"    font-weight: 600;\n"
"    border-radius: 8px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"#btn_deshacer:hover {\n"
"    background-color: #CB4335;\n"
"}\n"
"\n"
"#btn_deshacer:pressed {\n"
"    background-color: #922B21;\n"
"}\n"
"\n"
"#btn_crear {\n"
"    background-color: #27AE60;\n"
"    color: white;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"#btn_crear:hover {\n"
"    backgroun"
                        "d-color: #229954;\n"
"}\n"
"\n"
"#btn_crear:pressed {\n"
"    background-color: #1E8449;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_previsualizar = QPushButton(self.frame_8)
        self.btn_previsualizar.setObjectName(u"btn_previsualizar")

        self.verticalLayout_4.addWidget(self.btn_previsualizar)

        self.btn_deshacer = QPushButton(self.frame_8)
        self.btn_deshacer.setObjectName(u"btn_deshacer")

        self.verticalLayout_4.addWidget(self.btn_deshacer)

        self.btn_crear = QPushButton(self.frame_8)
        self.btn_crear.setObjectName(u"btn_crear")

        self.verticalLayout_4.addWidget(self.btn_crear)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.EspacioCarga)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Exportador Excel de Asistencia y Producci\u00f3n", None))
        self.btn_asistencia.setText(QCoreApplication.translate("MainWindow", u"ASISTENCIA", None))
        self.btn_produccion.setText(QCoreApplication.translate("MainWindow", u"PRODUCCI\u00d3N", None))
        self.TituloAsistencia.setText(QCoreApplication.translate("MainWindow", u"PROCESAMIENTO DE LA ASISTENCIA", None))
        self.RutaArchivo.setText(QCoreApplication.translate("MainWindow", u"UBICACI\u00d3N DEL ARCHIVO:", None))
        self.btn_archivo.setText("")
        self.RutaArchivo_2.setText(QCoreApplication.translate("MainWindow", u"UBICACI\u00d3N DE GUARDADO:", None))
        self.btn_guardar.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ELEGIR FECHA", None))
        self.RutaArchivo_3.setText(QCoreApplication.translate("MainWindow", u"DESDE:", None))
        self.RutaArchivo_4.setText(QCoreApplication.translate("MainWindow", u"HASTA:", None))
        self.dt_desde.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.btn_previsualizar.setText(QCoreApplication.translate("MainWindow", u"PREVISUALIZAR", None))
        self.btn_deshacer.setText(QCoreApplication.translate("MainWindow", u"DESHACER", None))
        self.btn_crear.setText(QCoreApplication.translate("MainWindow", u"CREAR", None))
    # retranslateUi

