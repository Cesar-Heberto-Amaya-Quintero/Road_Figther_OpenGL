from OpenGL.GL import *
from glew_wish import *
import glfw
import math

from TextoMenu import * 

textoMenu = TextoMenu()

class CosasMenu():

    def dibujar(self):
        #CALLE y BANQUETA
        glPushMatrix()

        glBegin(GL_QUADS)

        #BANQUETA
        glColor3f(214/255, 162/255, 90/255)
        glVertex3f(-0.1,-0.1,0)
        glVertex3f(-0.1,0.1,0)
        glVertex3f(1,0.1,0)
        glVertex3f(1,-0.1,0)

        glEnd()
        glPopMatrix()

        glBegin(GL_QUADS)

        #CALLE
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
        
        #AGUA
        glBegin(GL_QUADS)
        glColor3f(41/255, 171/255, 226/255)
        glVertex3f(-1,-1,0)
        glVertex3f(-1,1,0)
        glVertex3f(-0.6,1,0)
        glVertex3f(-0.6,-1,0)

        glEnd()

        #LINEAS AGUA
        
        glPushMatrix()

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

        #ARBOLES
        #ARBOL 1
        glPushMatrix()
        glTranslatef(0.8, 0.8, 0.0)

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

        glPushMatrix()
        glTranslatef(0.0, -0.8, 0.0)
        #glScalef(2,2,0)

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

        #TORTUGA
        glPushMatrix()
        glTranslatef(-1.1, 0.2, 0.0)
        # glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
        glScalef(0.7,0.7,0)
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
        glTranslatef(-1.2, 0.55, 0.0)
        # glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)
        glScalef(0.7,0.7,0)
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

        #HOJA
        glPushMatrix()
        glTranslatef(-1.3, -0.6, 0.0)
        #glTranslatef(posicion_cosasFondo[0], posicion_cosasFondo[1], 0.0)

        glBegin(GL_POLYGON)
        glColor3f(44/255, 147/255, 3/255)
        for angulo in range(0, 359, 5):
            glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.5 , 0.05 * math.sin(angulo * math.pi / 180) - 0.25, 0)
    
        glEnd()
        glPopMatrix()

        textoMenu.dibujar()
        textoMenu.actualizar()
