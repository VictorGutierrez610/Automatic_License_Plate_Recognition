import cv2
import pytesseract

# Ruta a la instalación de Tessseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Función para reconocer y extraer el texto de la matrícula
def recognize_plate(frame):

    # Filtro de immagen para escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Filtro para mejorar la imagen
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detectar bordes
    edges = cv2.Canny(blurred, 100, 200)

    # Encotnrar los bordes en la imagen
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Reconocer los bordes encontrados y buscar aquellos 4 que formen un rectangulo ( posible matrícula)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate = frame[y:y+h, x:x+w] # Recortar el rectanguo encontrado

            # Usar Tesseract para extaer el texto de la matrícula
            text = pytesseract.image_to_string(plate, config='--psm 8').strip()

            # Si se detecta algún texto en el rectangulo encontrado, se imprime
            if text:
                print(f'Mátricula detectada: {text}')
    
    return None
