from OpenGL.GL import *
from glew_wish import *
import glfw
import math

class CosasGameOver():
    def dibujar(self):
        #FONDO
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glVertex3f(-1,-1,0)
        glVertex3f(-1,1,0)
        glVertex3f(1,1,0)
        glVertex3f(1,-1,0)

        glEnd()

        # TODO EL TEXTO
        
        #PALABRA GAME
        glPushMatrix()
        glTranslatef(-0.15,-0.2,0)
        # LETRA G
        glPushMatrix()
        glTranslatef(-0.5, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.3, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.3, 0.2, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.32, 0.4, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.06, 0.0)
        glVertex3f(0.13, 0.06, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.24, 0.36, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.05, 0.0)
        glVertex3f(0.1, 0.08, 0.0)
        glVertex3f(0.13, 0.08, 0.0)
        glVertex3f(0.13, -0.05, 0.0)

        glEnd()
        glPopMatrix()

        # LETRA A
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        #LETRA M
        glPushMatrix()
        glTranslatef(0.1, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.3, 0.5, 0)
        glRotatef(90, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.13, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.13, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.3, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.2, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        #LETRA E
        glPushMatrix()
        glTranslatef(0.4, 0.5, 0)
        glPushMatrix()
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        
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
        glTranslatef(.2,0.00001,0)
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

        # LETRAS OVER
        glPushMatrix()
        glTranslatef(-0.1, -0.15, 0)
        #LETRA O
        glPushMatrix()
        glTranslatef(-0.3, -0.5, 0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        #LETRA V
        glPushMatrix()
        glTranslatef(-0.18, -0.34, 0)
        glPushMatrix()
        glTranslatef(0, 0.2, 0)
        glRotatef(20, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.24, 0.0)
        glVertex3f(0.13, 0.24, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.07, 0.275, 0)
        glRotatef(-20, 0,0,1)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.1, 0.0)
        glVertex3f(0.1, 0.24, 0.0)
        glVertex3f(0.13, 0.24, 0.0)
        glVertex3f(0.13, -0.1, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix()

        #LETRA E
        glPushMatrix()
        glTranslatef(0.05, 0, 0)
        glPushMatrix()
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        
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
        glTranslatef(.2,0.00001,0)
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
        glTranslatef(0.5, -0.5, 0)
        glPushMatrix()
        glTranslatef(-0.2, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.2, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.2, 0.0)

        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.03, 0.5, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

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
        glColor3f(1.0, 0.0, 0.0)

        glVertex3f(0.1, -0.13, 0.0)
        glVertex3f(0.1, 0.1, 0.0)
        glVertex3f(0.13, 0.1, 0.0)
        glVertex3f(0.13, -0.13, 0.0)

        glEnd()
        glPopMatrix()

        glPopMatrix() # PARA LA LETRA R

        glPopMatrix() # PARA LA PALABRA OVER

        # glPopMatrix() # PARA TODO EL TEXTO