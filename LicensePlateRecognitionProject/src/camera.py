import cv2

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

        cv2.imshow("Cámara en tiempo real", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Prueba llamando a la función con diferentes índices
if __name__ == "__main__":
    for i in range(3):  # Intenta con los índices 0, 1 y 2
        print(f"Intentando abrir la cámara en el índice {i}...")
        open_camera(i)
