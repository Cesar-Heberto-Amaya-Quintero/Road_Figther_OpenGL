from OpenGL.GL import *
from glew_wish import *
import glfw
import math

from Modelo import * 

class Pajaro2(Modelo):
    #posicion_pajaros = [[0.8,1.2,0], [-1.7,-0.3,0]]
    x = -1.7
    y=  -0.3
    z= 0.0
    fase = 90
    angulo= 10

    def __init__(self):
        super().__init__(self.x, self.y, self.z)
        
    
    def actualizar(self, tiempo_delta):
        # fase= 90
        # angulo_pajaro = 10
        cantidad_movimiento = 0.6 * tiempo_delta
        self.posicion_x = self.posicion_x + (math.cos((self.angulo - self.fase) * math.pi/ 180)  * cantidad_movimiento )
        self.posicion_y = self.posicion_y - (math.sin((self.angulo - self.fase) * math.pi/ 180)  * cantidad_movimiento )

        # posicion_pajaros[1][0] = posicion_pajaros[1][0] + (math.cos((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )
        # posicion_pajaros[1][1] = posicion_pajaros[1][1] - (math.sin((angulo_pajaro - fase) * math.pi/ 180)  * cantidad_movimiento )

        self.angulo = self.angulo + 0.4


    def dibujar(self):
        #PAJARO 2
        glPushMatrix()

        glTranslatef(self.posicion_x, self.posicion_y, 0)
        
        glPushMatrix()
        glTranslatef(0.41,-0.2,0)
        glScalef(0.2,0.2,0)
        glBegin(GL_TRIANGLES)
        glColor3f(196/255, 96/255, 8/255)
        glVertex3f(0.44, -0.26, 0.0)
        glVertex3f(0.43, -0.2, 0.0)
        glVertex3f(0.53, -0.26, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.08,-0.022,0)
        glBegin(GL_TRIANGLES)
        glColor3f(255/255, 255/255, 255/255)
        glVertex3f(0.44, -0.26, 0.0)
        glVertex3f(0.45, -0.2, 0.0)
        glVertex3f(0.53, -0.26, 0.0)
        glEnd()
        glPopMatrix()

        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 255/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.024 * math.cos(angulo * math.pi / 180) + 0.48 , 0.025 * math.sin(angulo * math.pi / 180) - 0.25, 0)
    
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 255/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.43 , 0.03 * math.sin(angulo * math.pi / 180) - 0.25, 0)
    
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 255/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.02 * math.cos(angulo * math.pi / 180) + 0.43 , 0.07 * math.sin(angulo * math.pi / 180) - 0.25, 0)
    
        glEnd()
        glPushMatrix()
        glTranslatef(0.41,-0.19,0)
        glScalef(0.2,0.2,0)
        glBegin(GL_POLYGON)
        glColor3f(0/255, 0/255, 0/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.025 * math.cos(angulo * math.pi / 180) + 0.4 , 0.025 * math.sin(angulo * math.pi / 180) - 0.25, 0)
    
        glEnd()
        glPopMatrix()

        glPopMatrix()