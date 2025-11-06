# Auxilio Bonannata – Landing (Django)

Sitio tipo landing page en una sola plantilla con Bootstrap y Leaflet.

## Requisitos

- Python 3.10+
- Entorno virtual recomendado

## Instalación (Windows PowerShell)

```pwsh
# Crear venv (opcional pero recomendado)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Migraciones iniciales
python .\bonannata_site\manage.py migrate

# Ejecutar servidor de desarrollo
python .\bonannata_site\manage.py runserver
```

Luego abrir http://127.0.0.1:8000 en el navegador.

## Estructura

- `bonannata_site/` proyecto Django
  - `landing/` app con plantilla `index.html`, estáticos y vista
- `requirements.txt` dependencias

## Notas

- El formulario de contacto usa backend de email a consola para desarrollo (ver la salida del terminal al enviar).
- El mapa usa Leaflet + OpenStreetMap sin necesidad de claves.
- Para imágenes de fondo, podés reemplazar estilos del hero en `landing/static/landing/css/main.css` o integrar tus imágenes en `landing/static/landing/img/` y referenciarlas desde la plantilla.
# web-aux_bonannata
