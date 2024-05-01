import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.
gCamHeight = .1

def render(camAng):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()

    # set the current matrix to the identity matrix
    # glOrtho(left,right, bottom,top, zNear,zFar)
    # glOrtho(-1,1, -1,1, -1,1)
    glOrtho(-5,5, -5,5, -10,10)

    # gluLookAt (eyex,eyey,eyez, atx,aty,atz, upx,upy,upz)
    gluLookAt(.1*np.sin(camAng), gCamHeight, .1*np.cos(camAng), 0,0,0, 0,1,0)

    # draw coordinates
    drawFrame()
    
    glColor3ub(255, 255, 255)
    drawTriangle()

def drawFrame():
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

def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0, .5, .0]))
    glVertex3fv(np.array([.0, .0, .0]))
    glVertex3fv(np.array([.5, .0, .0]))
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global gCamAng, gCamHeight
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)
        elif key == glfw.KEY_2:
            gCamHeight += .1
        elif key == glfw.KEY_W:
            gCamHeight += -.1

        # for debugging the model-view matrix
        elif key == glfw.KEY_D:
            model = glGetDoublev(GL_MODELVIEW_MATRIX).T
            print(model)


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