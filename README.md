# Auxilio Bonannata - Sitio Web Estático

Sitio web oficial de **Auxilio Bonannata** - Transporte y auxilios en Córdoba, Argentina.

**🌐 Dominio:** https://auxiliobonannata.com/

---

## 📁 Estructura del Proyecto

```
web-aux_bonannata/
├── .gitignore                          # Git ignore
├── .venv/                              # Virtual environment (no incluir en git)
├── bonannata_site/                     # Aplicación Django
│   ├── landing/                        # App principal
│   │   ├── templates/landing/
│   │   │   └── index.html             # ← FUENTE: plantilla principal
│   │   ├── static/landing/            # ← FUENTE: archivos estáticos
│   │   │   ├── css/main.css
│   │   │   ├── js/main.js
│   │   │   └── recursos_download/     # Iconos redes sociales
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   ├── manage.py
│   ├── db.sqlite3                     # Base de datos (no incluir en git)
│   └── bonannata_site/                # Configuración Django
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
├── dist/                               # ← OUTPUT: Sitio estático para Hostinger
│   ├── index.html                     # Generado automáticamente
│   └── static/
├── recursos_download/                 # Archivos de origen (backup)
├── build_ssg.py                       # Script para generar sitio estático
├── requirements.txt                    # Dependencias Python
├── package.json                        # Metadatos del proyecto
├── HOSTINGER_DEPLOYMENT.md            # Guía de deployment
└── README.md                           # Este archivo
```

---

## 🚀 Uso y Desarrollo

### 1. Configurar ambiente
```bash
# Crear/activar venv
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Hacer cambios
Edita los archivos en:
- **Plantilla HTML:** `bonannata_site/landing/templates/landing/index.html`
- **Estilos:** `bonannata_site/landing/static/landing/css/main.css`
- **JavaScript:** `bonannata_site/landing/static/landing/js/main.js`

### 3. Generar sitio estático
```bash
python build_ssg.py
```
Genera la carpeta `dist/` lista para Hostinger.

### 4. Subir cambios
- Abre File Manager en Hostinger
- Reemplaza los archivos en `public_html/` con el contenido de `dist/`
- Los cambios se verán en vivo en https://auxiliobonannata.com/

---

## 📝 Tecnología

- **Frontend:** HTML5 + Bootstrap 5 + CSS3
- **Backend:** Django 5.2 (solo para desarrollo/generación)
- **Static Generation:** django-distill
- **Formulario de contacto:** Formspree
- **Hosting:** Hostinger
- **Mapa:** Leaflet + OpenStreetMap

---

## ⚙️ Configuración

### Formspree (Emails)
El ID ya está configurado en el formulario:
```html
<form action="https://formspree.io/f/mdaaorgd" method="POST">
```
Los emails van a: **auxiliobonannata@hotmail.com**

### Leaflet Map
Ubicación: Ruta 5 km 35, Villa Anisacate, CP 5189

---

## 📂 Lo que NO va a Git

Estos archivos/carpetas se ignoran (ver `.gitignore`):
- `.venv/` - Virtual environment
- `db.sqlite3` - Base de datos
- `bonannata_site/static_collected/` - Generado por collectstatic
- `dist/` - Generado por build_ssg.py
- `__pycache__/` - Caché de Python

---

## 🔄 Workflow para actualizaciones

1. **Modificar** archivos en `bonannata_site/`
2. **Generar:** `python build_ssg.py`
3. **Revisar:** Abre `dist/index.html` en navegador (localmente)
4. **Subir:** Copia `dist/` a Hostinger via File Manager
5. **Verificar:** Accede a https://auxiliobonannata.com/

---

## 📋 Archivos importantes

| Archivo | Propósito |
|---------|----------|
| `bonannata_site/landing/templates/landing/index.html` | Fuente de la página web |
| `bonannata_site/landing/static/landing/css/main.css` | Estilos personalizados |
| `bonannata_site/landing/static/landing/js/main.js` | JavaScript personalizado |
| `bonannata_site/bonannata_site/settings.py` | Configuración Django |
| `build_ssg.py` | Script para generar sitio estático |
| `dist/index.html` | Salida final para Hostinger |

---

## 🐛 Troubleshooting

### Error de permisos al ejecutar build_ssg.py
```powershell
Remove-Item -Recurse -Force dist
python build_ssg.py
```

### Las imágenes no cargan
Verifica que `/static/` esté en `public_html/` de Hostinger.

### El formulario no envía emails
Verifica que el ID de Formspree es correcto: `mdaaorgd`

---

## 📞 Contacto

- **Email:** auxiliobonannata@hotmail.com
- **WhatsApp:** +54 9 3547 632007
- **Instagram:** @auxilio.bonannata
- **TikTok:** @auxilio.bonannata
- **Facebook:** Auxilio Bonannata

---

**Última actualización:** 15 de enero de 2026  
**Versión:** 1.0 (Producción - Sitio Estático)
