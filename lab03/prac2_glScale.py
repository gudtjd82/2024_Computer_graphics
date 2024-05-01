import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.

def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()

    # set the current matrix to the identity matrix
    glOrtho(-1,1, -1,1, -1,1)

    gluLookAt(.1*np.sin(camAng), .1, .1*np.cos(camAng), 0,0,0, 0,1,0)

    # draw coordinates
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([1.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,1.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,1.]))
    glVertex3fv(np.array([0.,0.,0.]))
    glEnd()

    glColor3ub(255, 255, 255)
    
    # 1) & 2) all draw a triangle with the same transformation

    # 1)
    glScalef(2., .5, 1.)
    drawTriangle()

    # 2)
    # S = np.identity(4)
    # S[0, 0] = 2.
    # S[1, 1] = .5
    # S[2, 2] = 0.
    # drawTriangleTransformedBy(S)

def drawTriangleTransformedBy(M):
    glBegin(GL_TRIANGLES)
    glVertex3fv((M @ np.array([.0, .5, 0., 1.])) [:-1])
    glVertex3fv((M @ np.array([.0, .0, 0., 1.])) [:-1])
    glVertex3fv((M @ np.array([.5, .0, 0., 1.])) [:-1])
    glEnd()

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0, .5, .0]))
    glVertex3fv(np.array([.0, .0, .0]))
    glVertex3fv(np.array([.5, .0, .0]))
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global gCamAng
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 640, "OpenGL Trans. Functions", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render(gCamAng)
        # render(T, camAng)
        # render(T @ R, camAng)
        # render(R @ T, camAng)

        glfw.swap_buffers(window)

    glfw.terminate

if __name__ == "__main__":
    main()