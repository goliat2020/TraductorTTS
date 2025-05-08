import easyocr

def extraer_texto_de_imagen(ruta_imagen):
    # Crear un lector con los idiomas más comunes (puedes agregar más si lo deseas)
    lector = easyocr.Reader(['en', 'es', 'fr', 'de', 'it'], gpu=False)

    # Leer el texto de la imagen
    resultado = lector.readtext(ruta_imagen, detail=0)

    # Unir todo el texto detectado como un solo string
    return "\n".join(resultado)