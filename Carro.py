from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

import pygame


pygame.init()
pygame.mixer.init()

class Carro(Modelo):

    x = 0.0
    y = -0.8
    z = 0.0
    velocidad = 0.8

    def __init__(self):
        super().__init__(self.x, self.y, self.z, self.velocidad)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_superior = 0.10
        self.extremo_inferior = 0.10

    def actualizar(self, window, tiempo_delta, ventana_actual):
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
        cantidad_movimiento = self.velocidad * tiempo_delta
        if (estado_tecla_arriba or estado_tecla_w == glfw.PRESS) and ventana_actual == 1:
            self.posicion_y = self.posicion_y + cantidad_movimiento
        if (estado_tecla_abajo or estado_tecla_s == glfw.PRESS) and ventana_actual == 1:
            self.posicion_y = self.posicion_y - cantidad_movimiento
        if (estado_tecla_derecha or estado_tecla_d == glfw.PRESS) and ventana_actual == 1:
            self.posicion_x = self.posicion_x + cantidad_movimiento
        if (estado_tecla_izquierda or estado_tecla_a == glfw.PRESS) and ventana_actual == 1:
            self.posicion_x = self.posicion_x - cantidad_movimiento

        if self.posicion_x >= 0.35:
            self.posicion_x = 0.35

        if self.posicion_x <= -0.35:
            self.posicion_x = -0.35
        
        if self.posicion_y <= -0.90:
            self.posicion_y = -0.90

        if self.posicion_y >= 0.90:
            self.posicion_y = 0.90

        

    def dibujar(self):


        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)

        glPushMatrix()
        glTranslatef(-0.039,-0.01,0)
        glBegin(GL_POLYGON)
        glColor3f(31/255, 31/255, 31/255)

        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) , 0.025 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.039,-0.01,0)
        glBegin(GL_POLYGON)
        glColor3f(31/255, 31/255, 31/255)

        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) , 0.025 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.039,0.11,0)
        glBegin(GL_POLYGON)
        glColor3f(31/255, 31/255, 31/255)

        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) , 0.025 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.039,0.11,0)
        glBegin(GL_POLYGON)
        glColor3f(31/255, 31/255, 31/255)

        for angulo in range(0, 359, 5):
            glVertex3f(0.01 * math.cos(angulo * math.pi / 180) , 0.025 * math.sin(angulo * math.pi / 180) -.08, 0)
        glEnd()
        glPopMatrix()

        #CARRO
        glBegin(GL_QUADS)
        glColor3f(140/255, 0/255, 0/255)
        glVertex3f(-0.04,-0.1,0)
        glVertex3f(-0.04,0.055,0)
        glVertex3f(0.04,0.055,0)
        glVertex3f(0.04,-0.1,0)
        
        glEnd()

        glPushMatrix()
        glBegin(GL_POLYGON)

        for angulo in range(0, 359, 5):
            glVertex3f(0.04 * math.cos(angulo * math.pi / 180) , 0.04 * math.sin(angulo * math.pi / 180) +.04, 0)
    

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glBegin(GL_POLYGON)

        for angulo in range(0, 359, 5):
            glVertex3f(0.04 * math.cos(angulo * math.pi / 180) , 0.04 * math.sin(angulo * math.pi / 180) -.1, 0)
    

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0,0,0)
        glScalef(1,0.4,0)
        glRotatef(180,0,0,1)
        glBegin(GL_QUADS)
        glColor3f(15/255, 13/255, 9/255)
        glVertex3f(-0.027,0.0001,0)
        glVertex3f(-0.034,-0.07,0)
        glVertex3f(0.034,-0.07,0)
        glVertex3f(0.027,0.0001,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0,-0.05,0)
        glScalef(1,0.4,0)
        glRotatef(0,0,0,0)
        glBegin(GL_QUADS)
        glVertex3f(-0.027,0.0001,0)
        glVertex3f(-0.034,-0.07,0)
        glVertex3f(0.034,-0.07,0)
        glVertex3f(0.027,0.0001,0)
        glEnd()

        glPopMatrix()

        glPopMatrix()