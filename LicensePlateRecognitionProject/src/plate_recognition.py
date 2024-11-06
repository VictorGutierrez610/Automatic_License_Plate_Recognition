import cv2
import pytesseract
import re

# Configuración opcional para la ruta de Tesseract en Windows (ajusta si es necesario)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def recognize_plate(frame):
    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplica un filtro para mejorar los bordes de la matrícula
    gray = cv2.bilateralFilter(gray, 11, 17, 17)  # reduce el ruido y mantiene los bordes
    edged = cv2.Canny(gray, 30, 200)  # detector de bordes

    # Detecta contornos en la imagen procesada
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]  # selecciona los más grandes
    
    plate_text = ""
    for contour in contours:
        # Aproximación para detectar un contorno cuadrado/rectangular
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        # Si tiene 4 lados, es un posible candidato a matrícula
        if len(approx) == 4:
            # Extrae la región de la matrícula
            x, y, w, h = cv2.boundingRect(approx)
            plate = gray[y:y + h, x:x + w]
            
            # OCR en la región de la matrícula
            text = pytesseract.image_to_string(plate, config='--psm 8')
            
            # Busca patrones compatibles con matrículas españolas
            match = re.search(r'\b[A-Z]{3}\d{4}\b|\b\d{4}[A-Z]{3}\b', text.replace(" ", ""))
            if match:
                plate_text = match.group(0)
                print(f"Matrícula detectada: {plate_text}")
                break

    return plate_text
