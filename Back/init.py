from apis_utils import OpenAI

def main():
    # Crear una instancia de la clase OpenAI
    openai_obj = OpenAI()

    # Pedir al usuario el nombre de la comida
    comida = input("Introduce el nombre de la comida: ")

    # Obtener la receta de OpenAI
    receta = openai_obj.chatgpt_text(f"Dame la receta de {comida}, responde solamente con la receta")
    print(f"Receta de {comida}: {receta}")

    # Buscar una imagen de la comida en Google
    try:
        image_urls = openai_obj.search_image(comida)
        for item in image_urls['items']:
            if item['mime'] == 'image/jpeg' and item['image']['height'] >= OpenAI.MIN_HEIGHT and item['image']['width'] >= OpenAI.MIN_WIDTH:
                print(f"URL de la imagen: {item['link']}")
                break
    except KeyError as e:
        print("No se encontraron imágenes para la búsqueda:", e)

if __name__ == "__main__":
    main()
