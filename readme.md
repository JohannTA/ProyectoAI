1. **Configuración Inicial:**
   - Importa las bibliotecas necesarias: `cv2` y `mediapipe`.

2. **Configuración de la Cámara:**
   - Inicia la captura de video desde la cámara (número de dispositivo 1).

3. **Configuración de MediaPipe para el Seguimiento de Manos:**
   - Utiliza la biblioteca MediaPipe para configurar el modelo de seguimiento de manos.

4. **Bucle Principal:**
   - Inicia un bucle infinito para el seguimiento en tiempo real.

5. **Captura y Conversión de Fotograma:**
   - Captura un fotograma del video.
   - Convierte el fotograma a formato RGB para el procesamiento de MediaPipe.

6. **Procesamiento con MediaPipe:**
   - Procesa la imagen para obtener los resultados del seguimiento de manos.

7. **Dibujo de Landmarks:**
   - Si se detectan manos, dibuja los landmarks (puntos clave) en la imagen.

8. **Lógica de Conteo de Dedos:**
   - Identifica los dedos levantados y realiza un conteo.

9. **Mostrar Contador en la Imagen:**
   - Muestra el contador de dedos en la imagen.

10. **Visualización de la Imagen:**
    - Muestra la imagen con los landmarks y el contador en una ventana.