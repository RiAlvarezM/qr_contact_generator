"""
Generador de Códigos QR para vCards.

Este script utiliza la biblioteca 'segno' para crear un código QR
que contiene información de contacto en formato vCard.
El formato vCard es un estándar para tarjetas de visita electrónicas.
"""

import segno
from segno import helpers

def create_vcard_qr(contact_info, output_filename='contacto_qr.png', scale=5):
    """
    Crea y guarda un código QR a partir de la información de contacto.

    Args:
        contact_info (dict): Un diccionario con los datos de la vCard.
        output_filename (str): El nombre del archivo de imagen para el QR.
        scale (int): El factor de escala para la imagen del QR. Un número más
                     alto genera una imagen más grande.
    """
    try:
        # 1. Creación de la estructura de datos vCard
        # La función `make_vcard_data` de la librería `helpers` formatea
        # los datos del diccionario en una cadena de texto compatible con vCard.
        vcard_data = helpers.make_vcard_data(
            name=contact_info.get('full_name'),
            displayname=contact_info.get('display_name'),
            email=contact_info.get('email'),
            url=contact_info.get('url'),
            country=contact_info.get('country'),
            city=contact_info.get('city'),
            cellphone=contact_info.get('cellphone')
        )

        # 2. Generación del Código QR
        # `segno.make()` toma los datos (en este caso la vCard) y genera el QR.
        # El parámetro 'error' se establece en 'H' (High) para una alta corrección
        # de errores, lo que hace que el QR sea legible incluso si está parcialmente dañado.
        qrcode = segno.make(vcard_data, error='H')

        # 3. Guardado del Código QR como imagen
        # El método `.save()` exporta el QR a un archivo de imagen.
        qrcode.save(output_filename, scale=scale)
        print(f"¡Éxito! Código QR guardado como '{output_filename}'")

    except Exception as e:
        print(f"Ocurrió un error al generar el código QR: {e}")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
if __name__ == '__main__':
    # --- CONFIGURACIÓN DE DATOS ---
    # Modifica los valores de este diccionario para generar tu propio QR.
    # Es una buena práctica mantener los datos de configuración separados de la lógica.
    contact_details = {
        'full_name': 'Apellido;Nombre', # Formato: Apellido;Nombre
        'display_name': 'Nombre Apellido',
        'email': 'tu.correo@ejemplo.com',
        'url': 'https://www.tusitio-web.com',
        'country': 'Tu País',
        'city': 'Tu Ciudad',
        'cellphone': '+1234567890'
    }

    # Llamada a la función principal para crear el QR
    create_vcard_qr(
        contact_info=contact_details,
        output_filename='mi_contacto_qr.png',
        scale=10 # Puedes ajustar la escala para un QR más grande o pequeño
    )
