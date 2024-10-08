import cv2

# Abrir la cámara (el índice '0' es generalmente para la cámara por defecto)
# Si tienes múltiples cámaras conectadas, prueba con '1', '2', etc.
cap = cv2.VideoCapture(0)

# Comprobar si la cámara está abierta correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Bucle para capturar el video en tiempo real
while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    # Si no se capturan frames correctamente, salir
    if not ret:
        print("No se pudo recibir el frame. Saliendo ...")
        break

    # Mostrar el frame en una ventana
    cv2.imshow('Video en vivo', frame)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar el recurso cuando todo termina
cap.release()
cv2.destroyAllWindows()