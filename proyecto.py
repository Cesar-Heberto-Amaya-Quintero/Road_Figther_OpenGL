#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from time import time
from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Carro import *
from Enemigo import* 
from CosasFondo import * 
from CosasMenu import * 
from CosasGameOver import *
from Pajaro import * 
from Pajaro2 import * 
 
#SOLO PARA LA MÚSICA
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("menu_pou.mp3")
pygame.mixer.music.play()
# pygame.mixer.music.set_pos(-2.0)
pygame.mixer.music.queue("menu_pou.mp3")

pygame.mixer.music.set_volume(0.2) #0.2

#Importar random
from random import randint, random, seed, choice

seed(1)

carro = Carro()
# enemigo = Enemigo()
enemigos = []
pajaro1 = Pajaro()
pajaro2 = Pajaro2()
cosasFondo = CosasFondo()
cosasMenu = CosasMenu()
cosasGameOver = CosasGameOver()

window = None
#Unidades por segundo
tiempo_anterior = 0.0

posicion_pajaros = [[0.8,1.2,0], [-1.7,-0.3,0]]
angulo_pajaro = 10

posiciones_enemigos = [
    [-0.3, 1.3, 0.0],
    [0.0, 2.1, 0.0], 
    [0.3, 2.9, 0.0],
    [0.2, 1.8, 0.0],
    [0.1, 2.5, 0.0]]

colores_enemigos = [
    [245/255, 215/255, 66/255],
    [66/255, 149/255, 245/255], 
    [245/255, 215/255, 66/255],
    [72/255, 35/255, 122/255],
    [240/255, 41/255, 41/255]]

velocidades_enemigos = [1, 1, 1, 1, 1]
direcciones_enemigos = [0,0,0,0,0]
activos_enemigos = [1,1,1,1,1]

# CAMBIAR VENTANA
# 0 = MENU  1 = VENTANA JUEGO  2 GAME OBVER
ventana_actual = 0

#MOVIMIENTO LINEAS DE FONDO
posicion_lineas = [[0,1,0], [0,0,0]]

def inicializar_enemigos():
    for i in range(5):
        posicion_x = posiciones_enemigos[i][0]
        posicion_y = posiciones_enemigos[i][1]
        direccion = direcciones_enemigos[i]
        velocidad = velocidades_enemigos[i]
        activos = activos_enemigos[i]
        colorR = colores_enemigos[i][0]
        colorG = colores_enemigos[i][1]
        colorB = colores_enemigos[i][2]
        enemigos.append(Enemigo(posicion_x, posicion_y, 0.0, velocidad, direccion, activos, colorR, colorG, colorB))
        
def actualizar():
    global window
    # global posicion_carro
    global tiempo_anterior
    global ventana_actual

    if ventana_actual == 2:
        return
        
    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecución actual y la inmediata anterior de este función
    tiempo_delta = tiempo_actual - tiempo_anterior

    estado_enter  = glfw.get_key(window, glfw.KEY_ENTER)

    if estado_enter == glfw.PRESS and tiempo_actual > 2.5 and ventana_actual == 0:
        ventana_actual = 1
        pygame.mixer.music.load("big_blue_8bit.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.4) # 0.4
        pygame.mixer.music.queue("big_blue_8bit.mp3")

    carro.actualizar(window, tiempo_delta, ventana_actual)
    
    #Revisar colisión
    for enemigo in enemigos:
        if enemigo.colisionando(carro):
            ventana_actual = 2
            pygame.mixer.music.load("auto.mp3")
            pygame.mixer.music.play()

    if ventana_actual == 1:
        # actualizar_enemigos(tiempo_delta)
        for enemigo in enemigos:   
            enemigo.actualizar(tiempo_delta)
        # actualizar_lineasFondo()
        # actualizar_cosasFondo(tiempo_delta)
        cosasFondo.actualizar(tiempo_delta)
        # actualizar_pajaro(tiempo_delta)
        pajaro1.actualizar(tiempo_delta)
        pajaro2.actualizar(tiempo_delta)
        

    tiempo_anterior = tiempo_actual

def draw():
    # draw_cosasFondo()
    # draw_carro()
    cosasFondo.dibujar()
    carro.dibujar()
    # enemigos.dibujar()
    for enemigo in enemigos:
        enemigo.dibujar()
    pajaro1.dibujar()
    pajaro2.dibujar()
    # draw_enemigos()
    # draw_torti()

def draw_menu():
    # cosas_menu()
    cosasMenu.dibujar()
    # texto_menu()

def draw_gameOver():
    cosasGameOver.dibujar()
    #cosas_gameOver()

def main():
    global window
    width = 1100
    height = 880
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

    inicializar_enemigos()
    
    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(69/255, 145/255, 2/255,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar()
        # colisionando()
        
        #Dibujar
        if ventana_actual == 0:
            draw_menu()
        elif ventana_actual == 1:
            draw()
        elif ventana_actual == 2:
            draw_gameOver()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()