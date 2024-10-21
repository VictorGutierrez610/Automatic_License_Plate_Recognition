import cv2
import time
import numpy as np

def open_camera():

    # creación de una ventana de carga
    cv2.namedWindow('Loading', cv2.WINDOW_NORMAL)

    # escribir texto en la ventana de carga
    loading_image = np.zeros((100, 400, 3), dtype = np.uint8) # tres canales para imagen en color
   
    cv2.putText(img = loading_image, 
                text = 'Cargando...', 
                org = (50, 50), 
                fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale = 1, 
                color = (255, 255, 255), 
                thickness = 2)
    

    cv2.imshow('Loading', loading_image) # mostrar la imagen de carga


    time.sleep(2) # pausar para simular la carga durante 2 segundos


    cv2.destroyWindow('Loading') #Cerrar la ventana de carga


    cap = cv2.VideoCapture(0) # abrir la cámara con el ID 0, que normalmente es ell de la cámara del portatil

    if not cap.isOpened(): # confirmar si se ha podido abrir la cámara
        print('Error: No se pudo abrir la cámara')
        return
    
    while True:
        ret, frame = cap.read() # capturar cada frame de la cámara, ret para saber si la captura fue exitosa y frame es la imagen capturada

        if not ret: # mensaje por si la captura no fue exitosa
            print('Error: No se pudo obener la imagen de la cámara')
            break

        cv2.imshow('Camera', frame) # muestra los frames en una ventana nueva



        """if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1: # Comproborar si la ventana se cerró con la 'x'
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # Salir si se presiona la tecla 'q'
            break
            """
        # salir del bucle si se pulsa la letra 'q' o la X de la ventana
        if cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1 or cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow('Camera')
            break
            

    # Liberar la cámara y cerrar ventanas
    cap.release() 
    cv2.destroyAllWindows() 


if __name__ == '__main__':
    open_camera()