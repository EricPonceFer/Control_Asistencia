from src.proyecto.models import AsistenciaService


def main():

    servicio = AsistenciaService()
    ruta = servicio.ejecutar_proceso_completo()
    print("Archivo guardado en:", ruta)

if __name__ == "__main__":
    main()