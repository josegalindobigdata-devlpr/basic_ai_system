# convert_to_csv.py 
import csv
import re
from datetime import datetime

def clean_text(text):
    # Eliminar acentos y caracteres raros para los encabezados
    text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    text = text.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    text = text.replace('ñ', 'n').replace('Ñ', 'N')
    # Eliminar cualquier carácter que no sea alfanumérico o espacio
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text.strip()

def markdown_to_csv(md_file_path, csv_file_path):
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {md_file_path}")
        return

    # Buscar el inicio de la tabla
    table_start = -1
    for i, line in enumerate(lines):
        if '|' in line and i+1 < len(lines) and '---' in lines[i+1]:
            table_start = i
            break
    
    if table_start == -1:
        print("No se encontró la tabla en el archivo Markdown.")
        return

    # Encabezados exactos según protocolo V2.0
    final_headers = [
        "Posicion", "Empresa", "Ubicacion", "Modelo", 
        "Fecha Publicacion", "Años Experiencia", "Salario Orientativo", "Enlace busqueda"
    ]

    data_rows = []
    for line in lines[table_start + 2:]:
        if '|' not in line or '---' in line:
            continue
        
        # Procesar la línea de la tabla Markdown
        cells = line.strip().split('|')
        # Filtrar celdas vacías de los extremos si existen
        if cells and cells[0] == '': cells = cells[1:]
        if cells and cells[-1] == '': cells = cells[:-1]
        
        row = [cell.strip() for cell in cells]
        
        # Limpiar enlaces Markdown y emojis
        cleaned_row = []
        for cell in row:
            # Extraer URL si es un enlace [texto](url)
            link_match = re.search(r'\[.*?\]\((.*?)\)', cell)
            if link_match:
                cell = link_match.group(1)
            # Eliminar emojis y caracteres especiales de los datos, manteniendo caracteres en español y símbolos de moneda
            cell = re.sub(r'[^\x00-\x7FáéíóúÁÉÍÓÚñÑ€.,:/ -]', '', cell)
            cleaned_row.append(cell.strip())
        
        # Asegurar que la fila tenga el mismo número de columnas que el encabezado
        if len(cleaned_row) >= len(final_headers):
            data_rows.append(cleaned_row[:len(final_headers)])

    # Guardar con encoding utf-8-sig para que Excel reconozca los caracteres especiales (ñ, €, etc.)
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';') # Usar punto y coma para mejor compatibilidad con Excel en España
        writer.writerow(final_headers)
        writer.writerows(data_rows)
    
    print(f"Archivo CSV robusto generado en: {csv_file_path}")

if __name__ == "__main__":
    date_suffix = datetime.now().strftime('%Y%m%d')
    csv_filename = f'/home/ubuntu/reporte_executive_it_madrid_{date_suffix}.csv'
    markdown_to_csv('/home/ubuntu/reporte_executive_it_madrid.md', csv_filename)
    print(f"Generated: {csv_filename}")
