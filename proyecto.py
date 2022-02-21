#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from time import time
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

#SOLO PARA LA MÚSICA
import pygame


pygame.init()
pygame.mixer.init()



pygame.mixer.music.load("big_blue.mp3")
pygame.mixer.music.play()
# pygame.mixer.music.set_pos(-2.0)
pygame.mixer.music.queue("big_blue.mp3")

pygame.mixer.music.set_volume(0.3)






#Importar random
from random import randint, random, seed, choice

seed(1)

posicion_carro = [0, -0.8, 0.0]
window = None
#Unidades por segundo
velocidad = 0.8
tiempo_anterior = 0.0

posiciones_enemigos = [
    [-0.3, 1.3, 0.0],
    [0.0, 1.3, 0.0], 
    [0.3, 1.3, 0.0],
    [0.2, 1.3, 0.0],
    [0.1, 1.3, 0.0]]

posibles_posiciones = [-0.3, -0.25,-0.1, 0, 0.1, 0.25, 0.3]
posibles_colores_enemigos = [[245/255, 215/255, 66/255], [66/255, 149/255, 245/255], [36/255, 171/255, 56/255], [72/255, 35/255, 122/255], [240/255, 41/255, 41/255]]

colores_enemigos = [
    [245/255, 215/255, 66/255],
    [66/255, 149/255, 245/255], 
    [245/255, 215/255, 66/255],
    [72/255, 35/255, 122/255],
    [240/255, 41/255, 41/255]]

velocidades_enemigos = [1, 1, 1, 1, 1]
direcciones_enemigos = [0,0,0,0,0]
activos_enemigos = [0,0,0,0,0 ]

posicion_cosasFondo = [0,2,0]
posicion_pajaros = [[0.8,1.2,0], [-1.7,-0.3,0]]
angulo_pajaro = 10

contador_tiempo = 0.0



#MOVIMIENTO LINEAS DE FONDO
posicion_lineas = [[0,1,0], [0,0,0]]

def actualizar_lineasFondo():
    global contador_tiempo
    posicion_lineas[0][1] = posicion_lineas[0][1] - 0.01
    posicion_lineas[1][1] = posicion_lineas[1][1] - 0.01

    if posicion_lineas[0][1] < -1:
        posicion_lineas[0][1] = 1

    if posicion_lineas[1][1] < -1:
        posicion_lineas[1][1] = 1

def actualizar_cosasFondo():
    posicion_cosasFondo[1] = posicion_cosasFondo[1] - 0.001

    if posicion_cosasFondo[1] < -2.5:
        posicion_cosasFondo[1] = 2


def actualizar_pajaro(tiempo_delta):
    global angulo_pajaro
    fase= 90
    cantidad_movimiento = 0.6 * tiempo_delta
    posicion_pajaros[0][0] = posicion_pajaros[0][0] + (math.cos((angulo_pajaro + fase) * math.pi/ 180)  * cantidad_movimiento )
    posicion_pajaros[0][1] = posicion_pajaros[0][1] + (math.sin((angulo_pajaro + fase) * math.pi/ 180)  * cantidad_movimiento )

    posicion_pajaros[1][0] = posicion_pajaros[1][0] + (math.cos((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )
    posicion_pajaros[1][1] = posicion_pajaros[1][1] - (math.sin((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )

    angulo_pajaro = angulo_pajaro + 0.2

def actualizar_enemigos(tiempo_delta):
    global contador_tiempo

    if glfw.get_time() > 1.0: # get_time dice el tiempo transcurrido en seg desde que corriste el programa
        activos_enemigos[0] = 1
    if glfw.get_time() > 2.0:
        activos_enemigos[1] = 1
    if glfw.get_time() > 2.6:
        activos_enemigos[2] = 1
    if glfw.get_time() > 1.5:
        activos_enemigos[3] = 1
    if glfw.get_time() > 2.3:
        activos_enemigos[4] = 1

    contador_tiempo = contador_tiempo + tiempo_delta
    if contador_tiempo >= 1:
        contador_tiempo = contador_tiempo - 1.0
        for i in range(5):
            velocidades_enemigos[i] = velocidades_enemigos[i] + 0.03

    for i in range(5):
        if activos_enemigos[i]:
            cantidad_movimiento = velocidades_enemigos[i] * tiempo_delta
            if direcciones_enemigos [i] == 0:
                posiciones_enemigos[i] [1] = posiciones_enemigos[i] [1] - cantidad_movimiento
                if posiciones_enemigos [i][1] <= -1:
                    posiciones_enemigos [i][1] = 1.1
                    posicion = posibles_posiciones[randint(0,6)]
                    posiciones_enemigos [i][0] = posicion

                    # posible_color = randint(0,4)
                    colorR = posibles_colores_enemigos[randint(0,4)][0]
                    colorG = posibles_colores_enemigos[randint(0,4)][1]
                    colorB = posibles_colores_enemigos[randint(0,4)][2]
                    colores_enemigos[i][0] = colorR
                    colores_enemigos[i][1] = colorG
                    colores_enemigos[i][2] = colorB
                    # direcciones_cuadrados [i] = 1
            # else:
            #     posiciones_cuadrados[i] [1] = posiciones_cuadrados[i] [1] + cantidad_movimiento
            #     if posiciones_cuadrados [i][1] >= 0.75:
            #         direcciones_cuadrados [i] = 0
        

def actualizar():
    global window
    global posicion_carro
    global tiempo_anterior

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecución actual y la inmediata anterior de este función
    tiempo_delta = tiempo_actual - tiempo_anterior

    #ESTADO TRIANGULO
    #Leer los estados de las teclas que queremos
    estado_tecla_arriba  = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo  = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha  = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda  = glfw.get_key(window, glfw.KEY_LEFT)

    estado_tecla_w  = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s  = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d  = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a  = glfw.get_key(window, glfw.KEY_A)

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta
    if estado_tecla_arriba or estado_tecla_w == glfw.PRESS:
        posicion_carro[1] = posicion_carro[1] + cantidad_movimiento
    if estado_tecla_abajo or estado_tecla_s == glfw.PRESS:
        posicion_carro[1] = posicion_carro[1] - cantidad_movimiento
    if estado_tecla_derecha or estado_tecla_d == glfw.PRESS:
        posicion_carro[0] = posicion_carro[0] + cantidad_movimiento
    if estado_tecla_izquierda or estado_tecla_a == glfw.PRESS:
        posicion_carro[0] = posicion_carro[0] - cantidad_movimiento

    if posicion_carro[0] >= 0.35:
        posicion_carro[0] = 0.35

    if posicion_carro[0] <= -0.35:
        posicion_carro[0] = -0.35
    
    if posicion_carro[1] <= -0.90:
        posicion_carro[1] = -0.90

    if posicion_carro[1] >= 0.90:
        posicion_carro[1] = 0.90


    actualizar_enemigos(tiempo_delta)
    actualizar_lineasFondo()
    actualizar_cosasFondo()
    actualizar_pajaro(tiempo_delta)

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    colisionando_calle = False
    #Método de bounding box:
    # El extremo derecho del triangulo >= extremo izquierdo del cuadrado
    # El extremo izquierdo del triangulo <= extremo derecho del cuadrado
    # El extremo superior del triangulo >= extremo inferior del cuadrado
    # El extremo inferior del triangulo <= extremo superior del cuadrado

    for i in range(5):

        if (posicion_carro[0] + 0.05 >= posiciones_enemigos[i][0] -0.05 and 
        posicion_carro[0] - 0.05 <= posiciones_enemigos[i][0] + 0.05 and 
        posicion_carro[1] + 0.1 >= posiciones_enemigos[i][1] -0.15 and 
        posicion_carro[1] - 0.1 <= posiciones_enemigos[i][1] + 0.15):
            colisionando = True


    return colisionando

def draw_carro():
    global posicion_carro

    glPushMatrix()
    glTranslatef(posicion_carro[0], posicion_carro[1], 0.0)
    glBegin(GL_QUADS)

    

    #CARRO PARTE EN FRENTE
    glColor3f(31/255, 31/255, 31/255)
    glVertex3f(-0.03,-0.1,0)
    glVertex3f(-0.03,0.1,0)
    glVertex3f(0.03,0.1,0)
    glVertex3f(0.03,-0.1,0)

    #Revisar colisión
    if colisionando():
        
        glfw.set_window_should_close(window)
        glColor3f(0,1,0)
    else:
        glColor3f(209/255, 21/255, 40/255)
        
    #CARRO
    glVertex3f(-0.05,-0.1,0)
    glVertex3f(-0.05,0.055,0)
    glVertex3f(0.05,0.055,0)
    glVertex3f(0.05,-0.1,0)

    glEnd()



    glPopMatrix()

def draw_cosasFondo():

    #CALLE y banqueta
    glPushMatrix()
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
    glBegin(GL_QUADS)

    #Banqueta
    glColor3f(214/255, 162/255, 90/255)
    glVertex3f(-0.1,-0.1,0)
    glVertex3f(-0.1,0.1,0)
    glVertex3f(1,0.1,0)
    glVertex3f(1,-0.1,0)

    glEnd()
    glPopMatrix()

    glBegin(GL_QUADS)
    #Calle
    glColor3f(64/255, 64/255, 64/255)
    glVertex3f(-0.41,-1,0)
    glVertex3f(-0.41,1,0)
    glVertex3f(0.41,1,0)
    glVertex3f(0.41,-1,0)

    glColor3f(93/255, 97/255, 94/255)
    glVertex3f(-0.4,-1,0)
    glVertex3f(-0.4,1,0)
    glVertex3f(0.4,1,0)
    glVertex3f(0.4,-1,0)

    glEnd()
    


    #PARA LA COLISION CON LA CALLE
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.4,-1,0)
    glVertex3f(-0.4,1,0)
    glVertex3f(0.4,1,0)
    glVertex3f(0.4,-1,0)

    glEnd()
    


    #LINEAS CALLE
    glPushMatrix()
    glTranslatef(posicion_lineas[0][0], posicion_lineas[0][1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(215/255, 216/255, 217/255)
    glVertex3f(-0.015,-0.1,0)
    glVertex3f(-0.015,0.1,0)
    glVertex3f(0.015,0.1,0)
    glVertex3f(0.015,-0.1,0)

    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(posicion_lineas[1][0], posicion_lineas[1][1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(215/255, 216/255, 217/255)
    glVertex3f(-0.015,-0.1,0)
    glVertex3f(-0.015,0.1,0)
    glVertex3f(0.015,0.1,0)
    glVertex3f(0.015,-0.1,0)

    glEnd()
    glPopMatrix()
    

    #AGUAAAA
    glBegin(GL_QUADS)
    glColor3f(41/255, 171/255, 226/255)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.6,-1,0)

    glEnd()

    #LINEAS AGUAAAAA
    
    glPushMatrix()
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glBegin(GL_QUADS)
    glColor3f(166/255, 222/255, 237/255)
    glVertex3f(-0.7,-1.5,0)
    glVertex3f(-0.7,0.9,0)
    glVertex3f(-0.68,0.9,0)
    glVertex3f(-0.68,-1.5,0)

    glVertex3f(-0.9,-1.8,0)
    glVertex3f(-0.9,0,0)
    glVertex3f(-0.88,0,0)
    glVertex3f(-0.88,-1.8,0)

    glVertex3f(-0.95,0.5,0)
    glVertex3f(-0.95,1.5,0)
    glVertex3f(-0.93,1.5,0)
    glVertex3f(-0.93,0.5,0)

    glVertex3f(-0.7,1.5,0)
    glVertex3f(-0.7,2.7,0)
    glVertex3f(-0.68,2.7,0)
    glVertex3f(-0.68,1.5,0)

    glEnd()
    glPopMatrix()

    #ARBOLESSSS
    glPushMatrix()
    glTranslatef(0.8, 0.8, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glColor3f(17/255, 46/255, 16/255)
    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.08 * math.cos(angulo * math.pi / 180) , 0.15 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.13 * math.cos(angulo * math.pi / 180) , 0.1 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    #ARBOL 2
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.85, -0.3, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glColor3f(17/255, 46/255, 16/255)
    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.08 * math.cos(angulo * math.pi / 180) , 0.15 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.13 * math.cos(angulo * math.pi / 180) , 0.1 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    glPopMatrix()

    #ARBOL 3
    glPushMatrix()
    glTranslatef(0.6, 0.4, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glColor3f(17/255, 46/255, 16/255)
    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.08 * math.cos(angulo * math.pi / 180) , 0.15 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.13 * math.cos(angulo * math.pi / 180) , 0.1 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()
    glPopMatrix()

    #ARBOL 4
    glPushMatrix()
    glTranslatef(0.6, 1.15, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glColor3f(17/255, 46/255, 16/255)
    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.08 * math.cos(angulo * math.pi / 180) , 0.15 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()

    glBegin(GL_POLYGON)

    for angulo in range(0, 359, 5):
        glVertex3f(0.13 * math.cos(angulo * math.pi / 180) , 0.1 * math.sin(angulo * math.pi / 180) , 0)
   
    glEnd()
    glPopMatrix()

    #BARDA PARA EL AGUA
    glBegin(GL_QUADS)
    glColor3f(64/255, 64/255, 64/255)
    glVertex3f(-0.6,-1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.56,1,0)
    glVertex3f(-0.56,-1,0)

    glEnd()

    #TRONCO
    glPushMatrix()
    glTranslatef(-0.1,-0.2,0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.32, 0.2, 0.11)

    glVertex3f(-0.75, -0.3, 0.0)
    glVertex3f(-0.75, -0.1, 0.0)
    glVertex3f(-0.85,-0.1, 0.0)
    glVertex3f(-0.85, -0.3, 0.0)

    glColor3f(28/255, 23/255, 21/255)
    glVertex3f(-0.78, -0.27, 0.0)
    glVertex3f(-0.78, -0.13, 0.0)
    glVertex3f(-0.788,-0.13, 0.0)
    glVertex3f(-0.788, -0.27, 0.0)

    glColor3f(28/255, 23/255, 21/255)
    glVertex3f(-0.81, -0.25, 0.0)
    glVertex3f(-0.81, -0.13, 0.0)
    glVertex3f(-0.818,-0.13, 0.0)
    glVertex3f(-0.818, -0.25, 0.0)
    
    glEnd()
    glPopMatrix()

    #TIERRA
    glPushMatrix()
    glTranslatef(-0.13,0,0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
    
    glBegin(GL_QUADS)
    glColor3f(214/255, 162/255, 90/255)
    glVertex3f(0.58, -0.75, 0.0)
    glVertex3f(0.58, -0.15, 0.0)
    glVertex3f(0.8,-0.15, 0.0)
    glVertex3f(0.8, -0.75, 0.0)

    #BANCA
    glColor3f(82/255, 42/255, 19/255)
    glVertex3f(0.65, -0.55, 0.0)
    glVertex3f(0.65, -0.2, 0.0)
    glVertex3f(0.75,-0.2, 0.0)
    glVertex3f(0.75, -0.55, 0.0)

    glColor3f(82/255, 42/255, 19/255)
    glVertex3f(0.63, -0.54, 0.0)
    glVertex3f(0.63, -0.212, 0.0)
    glVertex3f(0.73,-0.212, 0.0)
    glVertex3f(0.73, -0.54, 0.0)

    #BOTE
    glColor3f(58/255, 58/255, 58/255)
    glVertex3f(0.65, -0.7, 0.0)
    glVertex3f(0.65, -0.58, 0.0)
    glVertex3f(0.75,-0.58, 0.0)
    glVertex3f(0.75, -0.7, 0.0)
    glEnd()
    glPopMatrix()


    #PARTE DE LA BARDA DEL AGUA
    glBegin(GL_QUADS)
    
    glColor3f(61/255, 61/255, 56/255)
    glVertex3f(-0.52,0.-1,0)
    glVertex3f(-0.52,1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.6,-1.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.55,0.55,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.6,0.55,0)

    glColor3f(161/255, 161/255, 161/255)
    glVertex3f(-0.53,0.55,0)
    glVertex3f(-0.53,1,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.55,0.55,0)
    glEnd()

    glPushMatrix()
    glTranslatef(0.0, -0.77,0)

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.55,0.55,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.6,0.55,0)

    glColor3f(161/255, 161/255, 161/255)
    glVertex3f(-0.53,0.55,0)
    glVertex3f(-0.53,1,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.55,0.55,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, -1.55,0)

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-0.55,0.55,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.6,1,0)
    glVertex3f(-0.6,0.55,0)

    glColor3f(161/255, 161/255, 161/255)
    glVertex3f(-0.53,0.55,0)
    glVertex3f(-0.53,1,0)
    glVertex3f(-0.55,1,0)
    glVertex3f(-0.55,0.55,0)
    glEnd()
    glPopMatrix()



def draw_torti():
    #TORTUGA
    glPushMatrix()
    glTranslatef(-1.1, 0.2, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
    glBegin(GL_POLYGON)
    glColor3f(8/255, 58/255, 17/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.015 * math.cos(angulo * math.pi / 180) + 0.38 , 0.02 * math.sin(angulo * math.pi / 180) - 0.3, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(8/255, 58/255, 17/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.015 * math.cos(angulo * math.pi / 180) + 0.42 , 0.02 * math.sin(angulo * math.pi / 180) - 0.3, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(8/255, 58/255, 17/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.4 , 0.02 * math.sin(angulo * math.pi / 180) - 0.19, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(8/255, 58/255, 17/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.06 * math.cos(angulo * math.pi / 180) + 0.4 , 0.02 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(44/255, 147/255, 3/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.4 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()
    glPopMatrix()

    #PATO
    glPushMatrix()
    glTranslatef(-1.3, 0.7, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glBegin(GL_TRIANGLES)

    glColor3f(196/255, 96/255, 8/255)

    glVertex3f(0.38, -0.18, 0.0)
    glVertex3f(0.4, -0.15, 0.0)
    glVertex3f(0.42, -0.18, 0.0)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(226/255, 193/255, 0.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.4 , 0.02 * math.sin(angulo * math.pi / 180) - 0.19, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(226/255, 193/255, 0.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.06 * math.cos(angulo * math.pi / 180) + 0.4 , 0.02 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(226/255, 193/255, 0.0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.04 * math.cos(angulo * math.pi / 180) + 0.4 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()
    glPopMatrix()

    #PAJARO
    glPushMatrix()

    glTranslatef(posicion_pajaros[0][0], posicion_pajaros[0][1], 0)
    
    glBegin(GL_TRIANGLES)
    glColor3f(196/255, 96/255, 8/255)
    glVertex3f(0.44, -0.26, 0.0)
    glVertex3f(0.43, -0.2, 0.0)
    glVertex3f(0.53, -0.26, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(48/255, 32/255, 22/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.024 * math.cos(angulo * math.pi / 180) + 0.48 , 0.025 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(48/255, 32/255, 22/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.43 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(48/255, 32/255, 22/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.03 * math.cos(angulo * math.pi / 180) + 0.43 , 0.07 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glPopMatrix()

    #PAJARO 2
    glPushMatrix()

    glTranslatef(posicion_pajaros[1][0], posicion_pajaros[1][1], 0)
    
    glBegin(GL_TRIANGLES)
    glColor3f(196/255, 96/255, 8/255)
    glVertex3f(0.44, -0.26, 0.0)
    glVertex3f(0.43, -0.2, 0.0)
    glVertex3f(0.53, -0.26, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.024 * math.cos(angulo * math.pi / 180) + 0.48 , 0.025 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.43 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.03 * math.cos(angulo * math.pi / 180) + 0.43 , 0.07 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()

    glPopMatrix()

    #FLOR 1
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,1.2,0)

    glBegin(GL_POLYGON)
    glColor3f(247/255, 0, 148/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 0, 148/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 0, 148/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 0, 148/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()
    
    #FLOR 2
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,0.6,0)

    glBegin(GL_POLYGON)
    glColor3f(255/255, 111/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(255/255, 111/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(255/255, 111/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(255/255, 111/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR 3
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,1.8,0)

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(186/255, 15/255, 15/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR 4
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,0.1,0)

    glBegin(GL_POLYGON)
    glColor3f(15/255, 93/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(15/255, 93/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(15/255, 93/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(15/255, 93/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR 5
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,-0.6,0)

    glBegin(GL_POLYGON)
    glColor3f(139/255, 15/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(139/255, 15/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(139/255, 15/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(139/255, 15/255, 153/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR 6
    glPushMatrix()
    glScalef(.6,.6,0)
    glTranslatef(-1.08,-1.2,0)

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.23, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.17, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.33 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.27 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(247/255, 227/255, 0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.3 , 0.025 * math.sin(angulo * math.pi / 180) - 0.2, 0)
    glEnd()
    glPopMatrix()

    #FLOR CON HOJA
    #HOJA
    glPushMatrix()
    glTranslatef(-1.3, -0.6, 0.0)
    glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

    glBegin(GL_POLYGON)
    glColor3f(44/255, 147/255, 3/255)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.5 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
   
    glEnd()
    glPopMatrix()


def draw_enemigos():
    global posiciones_enemigos
    for i in range(5):
        glPushMatrix()
        glTranslatef(posiciones_enemigos[i][0], posiciones_enemigos[i][1], 0.0)

        glBegin(GL_QUADS)
        glColor3f(31/255, 31/255, 31/255)
        glVertex3f(-0.03,-0.1,0)
        glVertex3f(-0.03,0.1,0)
        glVertex3f(0.03,0.1,0)
        glVertex3f(0.03,-0.1,0)

        glEnd()

        glBegin(GL_QUADS)
        # glColor3f(245/255, 215/255, 66/255)
        glColor3f(colores_enemigos[i][0], colores_enemigos[i][1], colores_enemigos[i][2] )
        glVertex3f(-0.05,0.05,0)
        glVertex3f(0.05,0.05,0)
        glVertex3f(0.05,-0.15,0)
        glVertex3f(-0.05,-0.15,0)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0)
        glVertex3f(0.05,0.05,0)
        glVertex3f(0.05,-0.15,0)
        glVertex3f(-0.05,-0.15,0)

        glEnd()

        glPopMatrix()

def draw():
    draw_cosasFondo()
    draw_carro()
    draw_enemigos()
    draw_torti()
    
   


def main():
    global window
    width = 1300
    height = 1080
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Road Fighter", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(69/255, 145/255, 2/255,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar()
        colisionando()
        #Dibujar
        draw()
        

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
