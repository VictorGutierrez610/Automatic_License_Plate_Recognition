import cv2
from plate_recognition import recognize_plate

def open_camera(index=0):  # Añadimos el parámetro 'index' con un valor predeterminado de 0
    cap = cv2.VideoCapture(index)
    
    if not cap.isOpened():
        print(f"Error al abrir la cámara en el índice {index}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar el frame")
            break

        # Llamamos a la función de reconocimiento de matrículas
        plate_text = recognize_plate(frame)

        # Muestra el frame en tiempo real
        cv2.imshow("Cámara en tiempo real", frame)

        # Si detectamos una matrícula, la imprimimos en consola
        if plate_text:
            print(f"Matrícula detectada: {plate_text}")


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# llamando a la función con diferentes índices para asegurarnos abrir la cámara
if __name__ == "__main__":
    for i in range(3):  # Intenta con los índices 0, 1 y 2
        print(f"Intentando abrir la cámara en el índice {i}...")
        open_camera(i)
