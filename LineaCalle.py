from OpenGL.GL import *
from glew_wish import *
import glfw
import math

from Modelo import * 

class LineaCalle(Modelo):
    x = 0.0
    y = 0.0
    z = 0.0
    posicion_lineas = [[0,1,0], [0,0,0]]

    def __init__(self):
        super().__init__(self, self.x, self.y, self.z)

    def actualizar(self):
        self.posicion_lineas[0][1] = self.posicion_lineas[0][1] - 0.01
        self.posicion_lineas[1][1] = self.posicion_lineas[1][1] - 0.01

        if self.posicion_lineas[0][1] < -1:
            self.posicion_lineas[0][1] = 1

        if self.posicion_lineas[1][1] < -1: 
            self.posicion_lineas[1][1] = 1

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_lineas[0][0], self.posicion_lineas[0][1], 0.0)
        glBegin(GL_QUADS)
        glColor3f(215/255, 216/255, 217/255)
        glVertex3f(-0.015,-0.1,0)
        glVertex3f(-0.015,0.1,0)
        glVertex3f(0.015,0.1,0)
        glVertex3f(0.015,-0.1,0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.posicion_lineas[1][0], self.posicion_lineas[1][1], 0.0)
        glBegin(GL_QUADS)
        glColor3f(215/255, 216/255, 217/255)
        glVertex3f(-0.015,-0.1,0)
        glVertex3f(-0.015,0.1,0)
        glVertex3f(0.015,0.1,0)
        glVertex3f(0.015,-0.1,0)

        glEnd()
        glPopMatrix()