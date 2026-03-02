from PySide6.QtWidgets import QApplication
import sys
from processor import Ventana

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()