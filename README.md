# 🔄 GitHub Project Unifier v2.0

## 📋 Descripción
Una herramienta automatizada que unifica y organiza todos los archivos de un proyecto de GitHub en un único directorio, facilitando la gestión y visualización del código fuente completo. Excluye automáticamente archivos de dependencias, configuración y archivos binarios para mantener solo el código fuente relevante.

## ⚙️ Características
- Unificación automática de archivos del proyecto
- Generación de estructura de árbol del proyecto
- Exclusión inteligente de dependencias y archivos no deseados
- Soporte para múltiples lenguajes de programación
- Formato organizado y legible
- Resumen detallado de la unificación

## 🚀 Instalación
```bash
git clone https://github.com/caosinf777/unify-repos.git
cd unify-repos
```

## 🛠️ Requisitos
- Python 3.6 o superior
- Permisos de lectura/escritura en el directorio de trabajo

## 📖 Uso
<<<<<<< HEAD
```bash
 python unify_repo.py /ruta/del/proyecto
```

## 🔍 Ejemplo de salida
```
unified_proyecto/
├── proyecto_unified.txt     # Archivo con todo el código unificado
└── proyecto_structure.txt   # Estructura del proyecto en formato árbol
=======
```python
python unify_repo.py [ruta-del-proyecto]
```

## 🔍 Ejemplo
```python
python unify_repo.py /ruta/a/mi/proyecto/

```

## 📋 Tipos de archivos soportados
- Python (.py, .pyw)
- JavaScript/TypeScript (.js, .jsx, .ts, .tsx)
- Java (.java, .kt, .groovy)
- C/C++ (.c, .cpp, .h, .hpp)
- C# (.cs, .vb)
- Web (.php, .html, .css, .scss, .sass)
- Ruby (.rb, .erb)
- Go (.go)
- Rust (.rs)
- Swift (.swift)
- Shell (.sh, .bash)
- Documentación (.md, .rst)

## 🚫 Exclusiones automáticas
- Directorios de dependencias (node_modules, vendor, etc.)
- Archivos de configuración (.env, package.json, etc.)
- Archivos binarios y multimedia
- Archivos de caché y logs
- Archivos de bloqueo (package-lock.json, yarn.lock, etc.)

## ⚠️ Consideraciones
- Se recomienda revisar el contenido generado
- Los archivos muy grandes pueden requerir más tiempo de procesamiento
- Algunos archivos pueden contener caracteres no compatibles

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu característica
3. Envía un pull request

## 📄 Licencia
MIT License

## 👤 Autor
Julio Cesar IA

## 📝 Notas de la Versión 2.0
- Implementación inicial del unificador
- Sistema de exclusión inteligente
- Generación de estructura en árbol
- Soporte para múltiples lenguajes
- Manejo de errores robusto

## 🔜 Próximas Características
- Soporte para configuraciones personalizadas
- Opciones de línea de comandos adicionales
- Interfaz gráfica de usuario
- Integración con API de GitHub
- Estadísticas de código
- Detección de duplicados

---
⌨️ con ❤️ por Julio Cesar

