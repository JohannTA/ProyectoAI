import cv2
import mediapipe as mp

video=cv2.VideoCapture(1)

mano = mp.solutions.hands
Mano = mano.Hands(max_num_hands=4)
mpDraw = mp.solutions.drawing_utils

while True:
    check,img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Mano.process(imgRGB)
    puntosManos = results.multi_hand_landmarks
    h,w,_ = img.shape
    nuevos_puntos=[]
    if puntosManos:
        for puntos in puntosManos:
            #print(puntos)
            mpDraw.draw_landmarks(img, puntos, mano.HAND_CONNECTIONS)
            for id, cord in enumerate(puntos.landmark):
                cx,cy = int(cord.x*w), int(cord.y*h)
                cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
                nuevos_puntos.append((cx,cy))
                #print(nuevos_puntos)
        
        dedos =[8,12,16,20]
        contador=0
        if puntos:
            if nuevos_puntos[4][0] < nuevos_puntos[2][0]:
                contador +=1
            for x in dedos:
                if nuevos_puntos[x][1]< nuevos_puntos[x-2][1]:
                    contador += 1
        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),5)
    cv2.imshow("Imagen", img)
    cv2.waitKey(1)