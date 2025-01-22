import os
import shutil
from datetime import datetime
from pathlib import Path
import argparse

class ProjectUnifier:
    def __init__(self, project_path):
        self.project_path = Path(project_path)
        self.project_name = self.project_path.name
        self.output_dir = Path(f"unified_{self.project_name}")
        self.unified_file = self.output_dir / f"{self.project_name}_unified.txt"
        self.tree_file = self.output_dir / f"{self.project_name}_structure.txt"
        
        # Directorios a excluir
        self.excluded_dirs = {
            # Dependencias y módulos
            'node_modules',
            'bower_components',
            'vendor',
            'packages',
            
            # Entornos virtuales y cache
            'venv',
            'env',
            '.env',
            'virtualenv',
            '__pycache__',
            '.pytest_cache',
            
            # Directorios de construcción
            'dist',
            'build',
            'target',
            'bin',
            'obj',
            
            # Directorios de IDEs y configuración
            '.git',
            '.idea',
            '.vscode',
            '.vs',
            
            # Directorios de logs y datos
            'logs',
            'log',
            'temp',
            'tmp',
            
            # Directorios de cobertura y reportes
            'coverage',
            'htmlcov',
            '.coverage',
            
            # Otros directorios comunes a excluir
            '.next',
            '.nuxt',
            '.serverless'
        }

        # Archivos específicos a excluir
        self.excluded_files = {
            'package-lock.json',
            'yarn.lock',
            'pnpm-lock.yaml',
            'composer.lock',
            'Gemfile.lock',
            'poetry.lock',
            'requirements.txt',
            'Cargo.lock',
            '.gitignore',
            '.dockerignore',
            '.env',
            '.env.local',
            '.env.development',
            '.env.production',
            'Pipfile.lock',
            'package.json',
            'tsconfig.json',
            'webpack.config.js',
            'babel.config.js',
            'jest.config.js',
            'next.config.js'
        }
        
        # Extensiones a incluir
        self.included_extensions = {
            # Python
            '.py', '.pyw',
            # JavaScript/TypeScript
            '.js', '.jsx', '.ts', '.tsx',
            # Java
            '.java', '.kt', '.groovy',
            # C/C++
            '.c', '.cpp', '.h', '.hpp',
            # C#
            '.cs', '.vb',
            # Web
            '.php', '.html', '.css', '.scss', '.sass',
            # Ruby
            '.rb', '.erb',
            # Go
            '.go',
            # Rust
            '.rs',
            # Swift
            '.swift',
            # Shell
            '.sh', '.bash',
            # Configuración
            '.xml', '.json', '.yaml', '.yml',
            # Documentación
            '.md', '.rst'
        }
        
        # Extensiones a excluir explícitamente
        self.excluded_extensions = {
            # Archivos compilados
            '.pyc', '.pyo', '.pyd',
            '.so', '.dll', '.exe',
            '.class', '.jar',
            '.o', '.obj',
            
            # Archivos comprimidos
            '.zip', '.tar', '.gz', '.rar',
            
            # Archivos de base de datos y logs
            '.log', '.db', '.sqlite', '.sqlite3',
            
            # Archivos multimedia
            '.png', '.jpg', '.jpeg', '.gif',
            '.ico', '.svg', '.mp3', '.mp4',
            '.wav', '.avi', '.mov',
            
            # Archivos de documentación binaria
            '.pdf', '.doc', '.docx',
            '.xls', '.xlsx', '.ppt', '.pptx',
            
            # Archivos de caché
            '.cache',
            
            # Archivos de bloqueo y configuración grandes
            '.lock'
        }

    def should_process_directory(self, dir_path: Path) -> bool:
        """
        Verifica si un directorio debe ser procesado.
        """
        try:
            # Convertir el path a relativo para verificar cada parte del camino
            rel_path = dir_path.relative_to(self.project_path)
            path_parts = rel_path.parts

            # Verificar cada parte del camino
            for part in path_parts:
                if part in self.excluded_dirs:
                    return False
                
                # Verificación específica para node_modules y otros directorios de dependencias
                if any(part.startswith(prefix) for prefix in [
                    'node_modules',
                    'bower_components',
                    'vendor',
                    'packages',
                    '.git',
                    'venv',
                    '__pycache__'
                ]):
                    return False

        except ValueError:
            # Si no se puede obtener el path relativo, es el directorio raíz
            pass

        return True

    def is_valid_file(self, file_path: Path) -> bool:
        """Verifica si el archivo debe ser incluido en la unificación."""
        # Verificar si el archivo está en la lista de archivos excluidos
        if file_path.name in self.excluded_files:
            return False
        
        # Verificar extensiones
        return (file_path.suffix.lower() in self.included_extensions and 
                file_path.suffix.lower() not in self.excluded_extensions)

    def create_output_directory(self):
        """Crea el directorio de salida si no existe."""
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)

    def unify_files(self):
        """Unifica todos los archivos del proyecto en uno solo."""
        with open(self.unified_file, 'w', encoding='utf-8') as unified:
            unified.write(f"# Proyecto Unificado: {self.project_name}\n")
            unified.write(f"# Fecha de unificación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            unified.write(f"# Extensiones incluidas: {', '.join(sorted(self.included_extensions))}\n\n")

            files_processed = 0
            skipped_dirs = set()

            for root, dirs, files in os.walk(self.project_path):
                current_dir = Path(root)
                
                # Modificar la lista de directorios in-place
                dirs[:] = [d for d in dirs if Path(root) / d not in skipped_dirs 
                          and self.should_process_directory(Path(root) / d)]
                
                # Si el directorio actual no debe procesarse, continuar con el siguiente
                if not self.should_process_directory(current_dir):
                    skipped_dirs.add(current_dir)
                    dirs.clear()  # Limpiar la lista de directorios para evitar procesamiento adicional
                    continue
                
                for file in sorted(files):
                    file_path = current_dir / file
                    if self.is_valid_file(file_path):
                        try:
                            relative_path = file_path.relative_to(self.project_path)
                            unified.write(f"\n{'='*80}\n")
                            unified.write(f"# Archivo: {relative_path}\n")
                            unified.write(f"# Extensión: {file_path.suffix}\n")
                            unified.write(f"{'='*80}\n\n")
                            
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                unified.write(content)
                                if not content.endswith('\n'):
                                    unified.write('\n')
                            
                            files_processed += 1
                        except Exception as e:
                            unified.write(f"# Error al procesar {file_path}: {str(e)}\n")

            # Agregar resumen al final
            unified.write(f"\n{'='*80}\n")
            unified.write(f"# Resumen de unificación\n")
            unified.write(f"# Archivos procesados: {files_processed}\n")
            unified.write(f"# Directorios excluidos: {len(skipped_dirs)}\n")
            unified.write(f"# Fecha de finalización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            unified.write(f"{'='*80}\n")

    def generate_tree(self):
        """Genera la estructura del proyecto en formato árbol."""
        indent = "    "
        branch = "│   "
        tee    = "├── "
        last   = "└── "

        def write_tree(dir_path: Path, prefix: str = ""):
            if not self.should_process_directory(dir_path):
                return

            try:
                contents = list(dir_path.iterdir())
                # Filtrar contenidos
                contents = [x for x in contents if self.should_process_directory(x) if x.is_dir()
                           or (x.is_file() and self.is_valid_file(x))]
                contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
                
                pointers = [tee] * (len(contents) - 1) + [last]
                for pointer, path in zip(pointers, contents):
                    tree_file.write(f"{prefix}{pointer}{path.name}\n")
                    
                    if path.is_dir():
                        extension = branch if pointer == tee else indent
                        write_tree(path, prefix + extension)

            except PermissionError:
                tree_file.write(f"{prefix}!── Error: Permiso denegado\n")

        with open(self.tree_file, 'w', encoding='utf-8') as tree_file:
            tree_file.write(f"📁 Estructura del proyecto: {self.project_name}\n")
            tree_file.write(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            write_tree(self.project_path)

    def process_project(self):
        """Procesa el proyecto completo."""
        print(f"🚀 Iniciando unificación del proyecto: {self.project_name}")
        
        # Crear directorio de salida
        self.create_output_directory()
        
        # Unificar archivos
        print("📝 Unificando archivos...")
        self.unify_files()
        print(f"✅ Archivos unificados en: {self.unified_file}")
        
        # Generar árbol
        print("🌳 Generando estructura del proyecto...")
        self.generate_tree()
        print(f"✅ Estructura guardada en: {self.tree_file}")
        
        print("\n✨ Proceso completado exitosamente!")

def main():
    parser = argparse.ArgumentParser(description='Unificador de proyectos con generador de estructura')
    parser.add_argument('project_path', help='Ruta del proyecto a unificar')
    args = parser.parse_args()

    unifier = ProjectUnifier(args.project_path)
    unifier.process_project()

if __name__ == "__main__":
    main()