#!/usr/bin/env python3
import os
import sys
from datetime import datetime

def unify_repository(repo_path):
    """
    Lee todos los archivos de código de un repositorio y los unifica en un solo archivo.
    
    Args:
        repo_path (str): Ruta al directorio del repositorio
    """
    # Extensiones comunes de código fuente
    extensions = ['.py', '.js', '.java', '.cpp', '.h', '.hpp', '.c', '.cs', '.php', '.rb', '.tsx', '.ts', '.jsx']
    
    # Crear nombre del archivo de salida con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Obtener el nombre de la última carpeta del repositorio
    repo_name = os.path.basename(os.path.normpath(repo_path))
    output_file = f"codigo_unificado_{repo_name}_{timestamp}.txt"
    
    # Obtener la ruta del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_file)
    
    print(f"\nIniciando unificación del repositorio: {repo_path}")
    print(f"El archivo de salida se creará en: {output_path}\n")
    
    total_files = 0
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(f"Repositorio: {repo_path}\n")
        outfile.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        outfile.write("="*80 + "\n\n")
        
        for root, dirs, files in os.walk(repo_path):
            # Ignorar directorios comunes que no contienen código fuente
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', '__pycache__', 'dist', 'build']]
            
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1].lower()
                
                if file_ext in extensions:
                    try:
                        # Escribir el nombre del archivo como encabezado
                        relative_path = os.path.relpath(file_path, repo_path)
                        outfile.write(f"\n{'='*80}\n")
                        outfile.write(f"Archivo: {relative_path}\n")
                        outfile.write(f"{'='*80}\n\n")
                        
                        # Leer y escribir el contenido del archivo
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                            outfile.write('\n\n')
                            
                        total_files += 1
                        print(f"Procesado: {relative_path}")
                            
                    except Exception as e:
                        print(f"Error al leer {file_path}: {str(e)}")
                        outfile.write(f"Error al leer {file_path}: {str(e)}\n\n")

    print(f"\nProceso completado!")
    print(f"Total de archivos procesados: {total_files}")
    print(f"Archivo generado: {output_file}")
    print(f"Ubicación: {output_path}")

def main():
    # Verificar si se proporcionó un argumento
    if len(sys.argv) != 2:
        print("Uso: python unify_repo.py <ruta_del_repositorio>")
        print("  o simplemente arrastre la carpeta del repositorio sobre este script")
        sys.exit(1)
    
    # Obtener la ruta del repositorio del primer argumento
    repo_path = sys.argv[1].strip('"').strip("'")  # Eliminar comillas si existen
    
    # Verificar si la ruta existe
    if not os.path.exists(repo_path):
        print(f"Error: La ruta {repo_path} no existe")
        sys.exit(1)
    
    # Ejecutar la unificación
    unify_repository(repo_path)

if __name__ == "__main__":
    main()