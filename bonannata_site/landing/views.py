from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from pathlib import Path

from .forms import ContactForm


def index(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f"Consulta desde el sitio - {data['nombre']}"
            body = (
                f"Nombre: {data['nombre']}\n"
                f"Email: {data['email']}\n"
                f"Teléfono: {data.get('telefono','')}\n\n"
                f"Mensaje:\n{data['mensaje']}"
            )
            # En desarrollo usamos backend a consola (config en settings)
            send_mail(
                subject,
                body,
                'no-reply@auxiliobonannata.com',
                ['auxiliobonannata@hotmail.com'],
                fail_silently=True,
            )
            messages.success(
                request,
                'Gracias por contactarnos. Te responderemos a la brevedad.',
            )
            submitted = True
            form = ContactForm()  # limpiar
        else:
            messages.error(request, 'Por favor, revisá los campos del formulario.')
    else:
        form = ContactForm()

    # Construir listas de imágenes por carpeta
    def list_images(rel_dir: str):
        try:
            base = Path(settings.BASE_DIR).parent / 'recursos_download' / 'imagenes_wsap' / rel_dir
            if not base.exists():
                return []
            exts = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
            files = [f for f in sorted(base.iterdir()) if f.suffix.lower() in exts and f.is_file()]
            # Devolver rutas relativas para el tag static
            return [str(Path('imagenes_wsap') / rel_dir / f.name).replace('\\', '/') for f in files]
        except Exception:
            return []

    ford_images = list_images('ford_400')
    iveco_images = list_images('iveco_daily')
    benz_images = list_images('benz_1624')
    semi_images = list_images('semiremolque_1450')
    vulcano_images = list_images('vulcano_21')
    mercelini_images = list_images('mercelini_2ejes')
    leocor_images = list_images('leocor_3ejes')
    tenedor_images = list_images('grua_plancha_tenedor')

    return render(
        request,
        'landing/index.html',
        {
            'form': form,
            'submitted': submitted,
            'ford_images': ford_images,
            'iveco_images': iveco_images,
            'benz_images': benz_images,
            'semi_images': semi_images,
            'vulcano_images': vulcano_images,
            'mercelini_images': mercelini_images,
            'leocor_images': leocor_images,
            'tenedor_images': tenedor_images,
        },
    )
