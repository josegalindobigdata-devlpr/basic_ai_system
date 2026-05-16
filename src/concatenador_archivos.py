# File: concatenador_archivos.py
#
from pathlib import Path


def solicitar_ruta_valida() -> Path:
    """
    Solicita al usuario una ruta válida hasta que sea correcta.
    """
    while True:
        ruta_input = input("Introduce la ruta de la carpeta origen: ").strip()
        ruta = Path(ruta_input)

        if ruta.exists() and ruta.is_dir():
            return ruta

        print("Ruta no válida. Inténtalo de nuevo.")


def listar_archivos(ruta: Path) -> list[Path]:
    """
    Lista todos los archivos de la ruta indicada.
    """
    archivos = [archivo for archivo in ruta.iterdir() if archivo.is_file()]

    if not archivos:
        print("No se encontraron archivos en la ruta especificada.")
    else:
        print("\nArchivos disponibles:")
        for archivo in archivos:
            print(f"- {archivo.name}")

    return archivos


def solicitar_nombre_salida() -> str:
    """
    Solicita el nombre del archivo de salida.
    """
    while True:
        nombre = input("\nIntroduce el nombre del archivo de salida (sin extensión opcional): ").strip()

        if nombre:
            if not nombre.endswith(".txt"):
                nombre += ".txt"
            return nombre

        print("Nombre no válido.")


def concatenar_archivos(ruta_origen: Path, archivos_disponibles: list[Path]) -> str:
    """
    Solicita archivos en bucle y concatena su contenido.
    """
    nombres_validos = {archivo.name: archivo for archivo in archivos_disponibles}
    contenido_final = []

    print("\nIntroduce nombres de archivos a concatenar (escribe 'exit' para finalizar):")

    while True:
        nombre_archivo = input("Archivo: ").strip()

        if nombre_archivo.lower() == "exit":
            break

        if nombre_archivo not in nombres_validos:
            print("Archivo no encontrado en la ruta indicada.")
            continue

        archivo_path = nombres_validos[nombre_archivo]

        try:
            with archivo_path.open("r", encoding="utf-8") as f:
                contenido = f.read()

            contenido_final.append(f"### FILE: {archivo_path.stem}")
            contenido_final.append(contenido)
            contenido_final.append(f"### END_OF_FILE: {archivo_path.stem}")

            print(f"Archivo '{nombre_archivo}' añadido correctamente.")

        except Exception as e:
            print(f"Error leyendo '{nombre_archivo}': {e}")

    return "\n".join(contenido_final)


def guardar_resultado(contenido: str, nombre_salida: str):
    """
    Guarda el archivo final en la carpeta /data del repositorio.
    """
    repo_root = Path(__file__).resolve().parent.parent
    carpeta_data = repo_root / "data"
    carpeta_data.mkdir(exist_ok=True)

    ruta_salida = carpeta_data / nombre_salida

    with ruta_salida.open("w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"\nArchivo generado correctamente en: {ruta_salida}")


def main():
    print("=== CONCATENADOR DE ARCHIVOS ===")

    ruta_origen = solicitar_ruta_valida()
    archivos_disponibles = listar_archivos(ruta_origen)

    if not archivos_disponibles:
        return

    nombre_salida = solicitar_nombre_salida()
    contenido_final = concatenar_archivos(ruta_origen, archivos_disponibles)

    guardar_resultado(contenido_final, nombre_salida)


if __name__ == "__main__":
    main()