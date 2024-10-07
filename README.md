# Sistema de Reconocimiento Automático de Matrículas para Control de Puertas de Garaje

Este proyecto tiene como objetivo construir un **sistema de reconocimiento automático de matrículas** para abrir la puerta de un garaje para vehículos autorizados. El sistema utiliza el **Reconocimiento Óptico de Caracteres (OCR) de Azure**, **Python** para el procesamiento, y una **base de datos** para gestionar la lista de matrículas autorizadas.

## Descripción del Proyecto 📓

El objetivo es crear un sistema automatizado que pueda:
- Reconocer las matrículas de los vehículos que se acerquen.
- Verificar la matrícula detectada con una base de datos de vehículos autorizados.
- Abrir automáticamente la puerta del garaje para vehículos autorizados.

## Tecnologías 📲

- **API de OCR de Azure**: Para detectar y extraer con precisión el número de la matrícula a partir de las imágenes.
- **Python**: Para gestionar el procesamiento de imágenes y la lógica del sistema, utilizando bibliotecas como OpenCV para manipulación de imágenes e interacción con la API de OCR de Azure.
- **Base de datos (SQL)**: Para almacenar y gestionar las matrículas autorizadas. Esto permitirá una verificación rápida y flexibilidad en la actualización de la lista de vehículos permitidos.
- **Raspberry Pi** (Opcional): Si deseas integrar el hardware para el control de la puerta del garaje.

## Pasos para Desarrollar el Proyecto 📋

1. **Instalación de la Cámara**: 
   - Instalar una cámara para capturar imágenes de los vehículos que se aproximen. Podría ser una cámara USB o una cámara IP.
   
2. **Procesamiento de Imágenes y Detección de Matrículas**: 
   - Usar **OpenCV** en Python para procesar las imágenes capturadas y aislar la zona de la matrícula. Esto incluye aplicar filtros, detectar bordes y extraer la región de la matrícula.

3. **Reconocimiento de Matrículas**: 
   - Usar **Azure OCR** para extraer el texto de la imagen procesada de la matrícula. La API de OCR convertirá la imagen de la matrícula en texto legible.

4. **Base de Datos para Verificación**:
   - Crear una **base de datos SQL** para almacenar la lista de matrículas autorizadas. Cada vez que se detecte una matrícula, el sistema consultará esta base de datos para comprobar si el vehículo está autorizado.

5. **Control Automático de la Puerta del Garaje**: 
   - Si el vehículo está autorizado, se enviará una señal al sistema de control de la puerta del garaje para que se abra automáticamente.

6. **Interfaz de Usuario (Opcional)**: 
   - Desarrollar una interfaz web sencilla para gestionar la lista de vehículos autorizados, permitiendo que los usuarios añadan, editen o eliminen entradas en la base de datos.

## Funcionalidades Futuras 📅

- **Notificaciones en Tiempo Real**: Recibir alertas de intentos de acceso no autorizados.
- **Registros de Acceso**: Mantener un registro de todas las entradas y salidas de vehículos para un análisis futuro.
- **Integración con Machine Learning en situaciones especiales de imagen**: Mejorar la capacidad del sistema para reconocer matrículas parcialmente ocultas utilizando modelos de aprendizaje automático.

## Reflexiones Finales 🎯

Este proyecto me permitirá profundizar en áreas como la **visión por computadora**, **soluciones de OCR en la nube** y **gestión de bases de datos**, mientras creo un sistema práctico y útil. Demuestra cómo la IA puede aplicarse a desafíos cotidianos de automatización.
