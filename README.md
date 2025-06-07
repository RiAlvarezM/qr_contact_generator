# Generador de Códigos QR para vCard

Este es un simple pero potente script de Python para generar códigos QR de contacto (vCard) utilizando la biblioteca `segno`.

El script está diseñado para ser fácilmente configurable, permitiendo al usuario introducir sus propios datos de contacto para generar un QR personalizado.

## Características

-   Genera un código QR a partir de datos de contacto.
-   Guarda el QR como un archivo de imagen `.png`.
-   Configuración de datos separada de la lógica del programa.
-   Alta corrección de errores (Nivel 'H') para asegurar la legibilidad del QR.
-   Permite ajustar la escala (tamaño) de la imagen del QR generado.

## Requisitos

-   Python 3.6 o superior
-   Biblioteca `segno`

## Instalación

1.  **Clona el repositorio (o descarga los archivos):**

    ```bash
    git clone [https://github.com/RiAlvarezM/qr_contact_generator.git](https://github.com/RiAlvarezM/qr_contact_generator.git)
    cd tu-repositorio
    ```

2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**

    El archivo `requirements.txt` contiene todas las bibliotecas necesarias.

    ```bash
    pip install -r requirements.txt
    ```

## ¿Cómo usarlo?

1.  **Abre el archivo `qr_generator.py`** en tu editor de texto o IDE favorito.

2.  **Modifica el diccionario `contact_details`** con tu propia información:

    ```python
    contact_details = {
        'full_name': 'Apellido;Nombre', # Importante: Apellido;Nombre
        'display_name': 'Nombre Apellido',
        'email': 'tu.correo@ejemplo.com',
        'url': '[https://www.tusitio-web.com](https://www.tusitio-web.com)',
        'country': 'Tu País',
        'city': 'Tu Ciudad',
        'cellphone': '+1234567890' # Formato internacional
    }
    ```

3.  **(Opcional) Cambia el nombre del archivo de salida** y la escala si lo deseas:
    ```python
     create_vcard_qr(
        contact_info=contact_details,
        output_filename='mi_qr_personalizado.png', # Nuevo nombre de archivo
        scale=10 # Tamaño de la imagen
    )
    ```
4.  **Ejecuta el script** desde tu terminal:
    ```bash
    python qr_generator.py
    ```

Se creará un nuevo archivo de imagen (por ejemplo, `mi_contacto_qr.png`) en la misma carpeta con tu código QR.

## Contribuciones

Las sugerencias y contribuciones son siempre bienvenidas. Por favor, abre un "issue" para discutir los cambios que te gustaría hacer.
