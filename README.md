# PruebaHP

MyApp es una aplicación web desarrollada en Django que muestra información sobre Pokémon.

## Configuración inicial

1. **Clonar el repositorio:**
   ```
   git clone https://github.com/JulianBelizan/PruebaHP.git
   ```

2. **Crear y activar un entorno virtual:**
   ```
   python -m venv myenv
   ```

   - **Activar el entorno virtual en Windows:**
     ```
     myenv\Scripts\activate
     ```

   - **Activar el entorno virtual en macOS y Linux:**
     ```
     source myenv/bin/activate
     ```

3. **Instalar dependencias:**
   ```
   pip install -r requirements.txt
   ```

## Ejecutar la aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:
```
python manage.py runserver
```

Luego, abre tu navegador web y ve a `http://localhost:8000` para ver la aplicación en funcionamiento.

## Estructura del proyecto

- **PruebaHP/**: Directorio principal del proyecto.
  - **myapp/**: Directorio de la aplicación Django.
  - **mysite/**: Directorio del proyecto Django.
  - **templates/**: Directorio que contiene las plantillas HTML.
  - **static/**: Directorio que contiene archivos estáticos como CSS, JavaScript e imágenes.
  - **manage.py**: Archivo de gestión de Django.
