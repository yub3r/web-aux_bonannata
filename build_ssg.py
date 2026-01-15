#!/usr/bin/env python
"""
Script para generar el sitio web estático con django-distill
y prepararlo para subir a Hostinger.

Uso:
    python build_ssg.py

Salida:
    - Crea carpeta /dist con el sitio estático completo
    - Todos los archivos listos para subir a Hostinger
"""

import os
import sys
import shutil
import stat
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
os.chdir(REPO_ROOT)

# Setup Django
sys.path.insert(0, str(REPO_ROOT / 'bonannata_site'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bonannata_site.settings')

import django
django.setup()

print("=" * 70)
print("🏗️  Generando sitio web estático con django-distill...")
print("=" * 70)

BONANNATA_DIR = REPO_ROOT / 'bonannata_site'
DIST_DIR = REPO_ROOT / 'dist'

# Nota: No eliminamos la carpeta anterior para evitar problemas de permisos en Windows
# django-distill sobrescribirá los archivos automáticamente

# Paso 1: Ejecutar collectstatic
print("\n📦 Recopilando archivos estáticos...")
os.chdir(BONANNATA_DIR)
result = subprocess.run(
    [sys.executable, 'manage.py', 'collectstatic', '--noinput'],
    capture_output=True,
    text=True
)
if result.returncode != 0:
    print(f"❌ Error en collectstatic:\n{result.stderr}")
    sys.exit(1)
print("✅ Archivos estáticos recopilados")

# Paso 2: Generar sitio estático con distill
print("\n🔨 Generando HTML estático...")
result = subprocess.run(
    [sys.executable, 'manage.py', 'distill-local', str(DIST_DIR), '--force'],
    capture_output=True,
    text=True
)
if result.returncode != 0:
    print(f"❌ Error en distill-local:\n{result.stderr}")
    sys.exit(1)
print("✅ HTML generado correctamente")

# Paso 3: Copiar archivos estáticos a dist/static
print("\n📋 Organizando archivos para Hostinger...")
static_collected = BONANNATA_DIR / 'static_collected'
dist_static = DIST_DIR / 'static'

if static_collected.exists():
    if dist_static.exists():
        shutil.rmtree(dist_static)
    shutil.copytree(static_collected, dist_static)
    print(f"✅ Archivos copiados a {dist_static}")

# Resumen final
print("\n" + "=" * 70)
print("✨ ¡SITIO ESTÁTICO LISTO!")
print("=" * 70)
print(f"\n📁 Carpeta de salida: {DIST_DIR}")
print(f"\n📂 Estructura para Hostinger:")
print("""
dist/
├── index.html          (página principal)
└── static/             (CSS, JS, imágenes)
    ├── landing/
    │   ├── css/
    │   ├── js/
    │   └── recursos_download/
    └── imagenes_wsap/
        └── hero/
""")

print("\n🚀 PASOS PARA SUBIR A HOSTINGER:")
print("""
1. Abre el File Manager de Hostinger
2. Sube todos los archivos de la carpeta 'dist/' a la raíz de tu hosting
   (o en public_html/ si tienes subdominio)
3. Asegúrate de subir también la carpeta 'static/' completa
4. La estructura final en Hostinger debe ser:
   public_html/
   ├── index.html
   └── static/
       └── [todos los archivos CSS, JS, imágenes]

5. Ingresa a tu dominio y verifica que funciona

⚠️  IMPORTANTE - FORMSPREE:
   - Ve a https://formspree.io
   - Crea una cuenta gratis
   - Copia tu ID de Formspree (ej: f/ABCDEF)
   - Reemplaza 'FORMSPREE_ID' en el action del formulario de contacto
   - Los emails irán a auxiliobonannata@hotmail.com
""")

print("\n✅ Proceso completado exitosamente!\n")
