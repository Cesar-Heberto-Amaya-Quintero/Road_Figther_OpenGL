from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import * 

#Importar random
from random import randint, random, seed, choice

seed(1)

class Enemigo(Modelo):


    contador_tiempo = 0.0


    posibles_posiciones = [-0.3, -0.25,-0.1, 0, 0.1, 0.25, 0.3]
    posibles_colores_enemigos = [[245/255, 215/255, 66/255], [66/255, 149/255, 245/255], [36/255, 171/255, 56/255], [72/255, 35/255, 122/255], [240/255, 41/255, 41/255]]

    def __init__(self, x, y, z, velocidad, direccion, activos, colorR, colorG, colorB):
        super().__init__(x, y, z, velocidad)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_superior = 0.09
        self.extremo_inferior = 0.09
        self.activos = activos
        self.direccion = direccion
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

    def actualizar(self, tiempo_delta):


        self.contador_tiempo = self.contador_tiempo + tiempo_delta
        if self.contador_tiempo >= 1:
            self.contador_tiempo = self.contador_tiempo - 1.0
            self.velocidad = self.velocidad + 0.03

        
        if self.activos:
            cantidad_movimiento =self.velocidad * tiempo_delta
            if self.direccion == 0:
                self.posicion_y = self.posicion_y - cantidad_movimiento
                if self.posicion_y <= -1:
                    self.posicion_y = 1.2
                    posicion = self.posibles_posiciones[randint(0,6)]
                    self.posicion_x = posicion

                    # posible_color = randint(0,4)
                    colorR = self.posibles_colores_enemigos[randint(0,4)][0]
                    colorG = self.posibles_colores_enemigos[randint(0,4)][1]
                    colorB = self.posibles_colores_enemigos[randint(0,4)][2]
                    
                    self.colorR = colorR
                    self.colorG = colorG
                    self.colorB = colorB

    def dibujar(self):
        
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)

        #LLANTAS
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

        #PARTE DEL CARRO
        glBegin(GL_QUADS)
        glColor3f(140/255, 0/255, 0/255)
        glColor3f(self.colorR, self.colorG, self.colorB)
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

        #VENTANAS
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