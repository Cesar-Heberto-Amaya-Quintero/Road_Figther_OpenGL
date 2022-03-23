from OpenGL.GL import *
from glew_wish import *
import glfw
import math

from Modelo import * 

class TextoMenu(Modelo):

    posicion_x = 0.0
    posicion_y = -1.6
    posicion_z = 0.0
    def __init__(self):
        super().__init__(self.posicion_x, self.posicion_y, self.posicion_z)
        

    def actualizar(self):
        self.posicion_y = self.posicion_y + 0.007
        if  self.posicion_y > 0.0:
            self.posicion_y = 0.0

    def dibujar(self):
        global posicion_letras

        #ENTER TO START
        glPushMatrix()
        glTranslatef(0, 0.1,0)
        glTranslatef(0, self.posicion_y,0)
        glScalef(0.7,0.7,0)
        #ENTER
        glPushMatrix()

        glTranslatef(-0.58,.5,0)

        #LETRA E
        glPushMatrix()

        glBegin(GL_QUADS)
        glColor3f(255/255, 255/255, 255/255)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,-0.3,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,-0.15,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.03, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.03, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        #LETRA N
        glPushMatrix()
        glTranslatef(.2,0.0,0)

        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.251,-0.03,0)
        glRotatef(22,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.22, 0.0)
        glVertex3f(0.1, 0.11, 0.0)
        glVertex3f(0.13, 0.11, 0.0)
        glVertex3f(0.13, -0.22, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.33,0.0,0)

        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        #LETRA T
        glPushMatrix()
        glTranslatef(.45,0.0,0)

        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.57,-0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        #LETRA E 
        glPushMatrix()
        glTranslatef(0.57,0,0)

        glPushMatrix()
        
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,-0.3,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,-0.15,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.03, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.03, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.2,0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPopMatrix()

        # LETRA R
        glPushMatrix()
        glTranslatef(0.97, -0.5, 0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.04, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.04, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.35, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.08, 0.3, 0)
        glRotatef(50, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.13, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.13, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        glPopMatrix()

        #TO
        glPushMatrix()
        glTranslatef(-0.67,0.1,0)
        #LETRA T
        glPushMatrix()
        glTranslatef(.45,0.0,0)

        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.57,-0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        #LETRA O
        glPushMatrix()
        glTranslatef(0.77, -0.5, 0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.2, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        glPopMatrix()

        #START
        glPushMatrix()
        glTranslatef(-.085,0,0)
        glPushMatrix()
        #LETRA S
        glPushMatrix()
        glTranslatef(-1.2,-0.3,0)
        glPushMatrix()
        glTranslatef(.9,-0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.9,-0.3,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.9,-0.15,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.7,0.0,0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.02, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.02, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.86,-0.15,0)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.02, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.02, 0.0)
        glEnd()
        glPopMatrix()
        
        glPopMatrix()

        glPopMatrix()

        #LETRA T
        glPushMatrix()
        glTranslatef(-0.67,-0.3,0)

        glPushMatrix()
        glTranslatef(.45,0.0,0)

        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.57,-0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()
        glPopMatrix()

        # LETRA A
        glPushMatrix()
        glTranslatef(0.1,-.8,0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.35, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        # LETRA R
        glPushMatrix()
        glTranslatef(0.31, -0.8, 0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.04, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.04, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.35, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.08, 0.3, 0)
        glRotatef(50, 0,0,1)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.13, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.13, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        #LETRA T
        glPushMatrix()
        glTranslatef(-0.05,-0.3,0)

        glPushMatrix()
        glTranslatef(.45,0.0,0)

        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.13, 0.0)
        glVertex3f(0.13, 0.13, 0.0)
        glVertex3f(0.13, -0.2, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(.57,-0.0001,0)
        glRotatef(90,0,0,1)
        glBegin(GL_QUADS)
        glVertex3f(0.1, -0.09, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.09, 0.0)
        glEnd()
        glPopMatrix()

        glPopMatrix()

        glPopMatrix()
        

        glPopMatrix()