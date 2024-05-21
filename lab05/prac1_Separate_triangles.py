import glfw
from OpenGL.GL import * 
from OpenGL.GLU import *
import numpy as np

def drawCube_glVertex():
    glBegin(GL_TRIANGLES)
    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f(  1  ,  -1   ,   1   )   # v2
    glVertex3f(  1  ,   1   ,   1   )   # v1

    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f( -1  ,  -1   ,   1   )   # v3
    glVertex3f(  1  ,  -1   ,   1   )   # v2

    glVertex3f( -1  ,   1   ,  -1   )   # v4
    glVertex3f(  1  ,   1   ,  -1   )   # v5
    glVertex3f(  1  ,  -1   ,  -1   )   # v6
    
    glVertex3f( -1  ,   1   ,  -1   )   # v4
    glVertex3f(  1  ,  -1   ,  -1   )   # v6
    glVertex3f( -1  ,  -1   ,  -1   )   # v7

    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f(  1  ,   1   ,   1   )   # v1
    glVertex3f(  1  ,   1   ,  -1   )   # v5

    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f(  1  ,   1   ,  -1   )   # v5
    glVertex3f( -1  ,   1   ,  -1   )   # v4

    glVertex3f( -1  ,  -1   ,   1   )   # v3
    glVertex3f(  1  ,  -1   ,  -1   )   # v6
    glVertex3f(  1  ,  -1   ,   1   )   # v2

    glVertex3f( -1  ,  -1   ,   1   )   # v3
    glVertex3f( -1  ,  -1   ,  -1   )   # v7
    glVertex3f(  1  ,  -1   ,  -1   )   # v6

    glVertex3f(  1  ,   1   ,   1   )   # v1
    glVertex3f(  1  ,  -1   ,   1   )   # v2
    glVertex3f(  1  ,  -1   ,  -1   )   # v6

    glVertex3f(  1  ,   1   ,   1   )   # v1
    glVertex3f(  1  ,  -1   ,  -1   )   # v6
    glVertex3f(  1  ,   1   ,  -1   )   # v5

    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f( -1  ,  -1   ,  -1   )   # v7
    glVertex3f( -1  ,  -1   ,   1   )   # v3

    glVertex3f( -1  ,   1   ,   1   )   # v0
    glVertex3f( -1  ,   1   ,  -1   )   # v4
    glVertex3f( -1  ,  -1   ,  -1   )   # v7
    glEnd()