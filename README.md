# Gestión de Créditos

## Descripción
Este proyecto es una aplicación web para la gestión de créditos, que incluye funcionalidades como registro de créditos, visualización de estadísticas y una barra lateral interactiva.

## Requisitos
- Python 3.10 o superior
- Un entorno virtual configurado (opcional pero recomendado)
- Las dependencias listadas en `requirements.txt`

## Instrucciones para ejecutar el proyecto

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd EJCreditos
   ```

2. **Crear y activar un entorno virtual (opcional)**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   - Asegúrate de que el archivo `creditos.db` existe en la carpeta `instance/`.
   - Si no existe, crea uno ejecutando el script de inicialización (si está disponible).

5. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

6. **Abrir la aplicación en el navegador**
   - Ve a [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Funcionalidades
- Registro de créditos con validación de datos.
- Visualización de estadísticas con gráficos interactivos.
- Barra lateral dinámica con íconos.
- Ventanas emergentes para notificaciones.

## Dependencias principales
- Flask
- Chart.js
- Font Awesome

## Notas adicionales
- Asegúrate de que los archivos estáticos (CSS, JS) y las plantillas HTML estén correctamente servidos.
- Si encuentras problemas, revisa la consola del navegador para errores de JavaScript o el terminal para errores del servidor.

¡Disfruta usando mi aplicación! 🎉