"""
Script minimal para generar una versión estática del landing y copiar los assets
=> salida en ./docs/

Uso (desde la raíz del repo, con venv activado):
  python build_static.py

Explicación:
 - Carga entorno Django
 - Reproduce la lógica mínima para listar imágenes usadas en los carousels
 - Renderiza la plantilla `landing/index.html` con ese contexto
 - Copia `bonannata_site/static_collected` a `docs/static_collected`
 - Escribe `docs/index.html`

Limitaciones:
 - Formularios (contacto) quedarán estáticos (no funcionales). Se puede convertir a mailto si se desea.
 - El mapa Leaflet es cliente-side y funcionará si dispone de conexión a OSM.
"""

import os
import sys
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
os.chdir(REPO_ROOT)

# Ajustes para cargar Django
sys.path.insert(0, str(REPO_ROOT / 'bonannata_site'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bonannata_site.settings')

import django
from django.template.loader import get_template
from django.template import Context

django.setup()

# Rutas y utilidades para listar imágenes
BASE_DIR = Path(__file__).resolve().parent / 'bonannata_site'
RECURSOS = Path(__file__).resolve().parent.parent / 'recursos_download'  # proyecto/recursos_download
IMAGES_BASE = RECURSOS / 'imagenes_wsap'

# Helper para construir la lista relativa usada por la plantilla (path para {% static %})
def list_images(subdir):
    folder = IMAGES_BASE / subdir
    out = []
    if folder.exists() and folder.is_dir():
        for f in sorted(folder.iterdir()):
            if f.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
                # la plantilla espera rutas estáticas relativas a STATICFILES_DIRS
                # en collectstatic fueron copiadas a static_collected/imagenes_wsap/...
                out.append(f'imagenes_wsap/{subdir}/{f.name}')
    return out

context = {
    'ford_images': list_images('ford'),
    'iveco_images': list_images('iveco'),
    'benz_images': list_images('benz'),
    'semi_images': list_images('semi'),
    'vulcano_images': list_images('vulcano'),
    'mercelini_images': list_images('mercelini'),
    'leocor_images': list_images('leocor'),
    'tenedor_images': list_images('tenedor'),
    # context minimal adicional
    'now': None,
    'messages': [],
    'form': type('F', (), {'nombre': type('x', (), {'value': ''}), 'email': type('x', (), {'value': ''}), 'telefono': type('x', (), {'value': ''}), 'mensaje': type('x', (), {'value': ''}) })(),
    'submitted': False,
}

# Carga y render
try:
    tpl = get_template('landing/index.html')
except Exception as e:
    print('ERROR: no se pudo cargar la plantilla landing/index.html:', e)
    sys.exit(1)

rendered = tpl.render(context)

# Preparar carpeta docs
DOCS = REPO_ROOT / 'docs'
if DOCS.exists():
    shutil.rmtree(DOCS)
DOCS.mkdir(parents=True)

# Escribir index.html
(DOCS / 'index.html').write_text(rendered, encoding='utf-8')
print('Wrote', DOCS / 'index.html')

# Copiar static_collected si existe
STATIC_COLLECTED = REPO_ROOT / 'bonannata_site' / 'static_collected'
if STATIC_COLLECTED.exists():
    dest_static = DOCS / 'static_collected'
    shutil.copytree(STATIC_COLLECTED, dest_static)
    print('Copied static_collected to', dest_static)
else:
    print('Warning: static_collected not found. Run collectstatic first.')

print('\nStatic build complete. Ahora podes commitear y pushear la carpeta docs/ y activar GitHub Pages (source: main branch /docs folder).')
