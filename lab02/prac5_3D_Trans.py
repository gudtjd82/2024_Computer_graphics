import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def render(M, camAng):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()

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

    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex3fv((M @ np.array([.0, .5, 0., 1.]))[:-1])
    glVertex3fv((M @ np.array([.0, .0, 0., 1.]))[:-1])
    glVertex3fv((M @ np.array([.5, .0, 0., 1.]))[:-1])
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 640, "3D Trans", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)
    count = 0

    while not glfw.window_should_close(window):
        glfw.poll_events()

        t = glfw.get_time()

        # rotation
        th = np.radians(-60)
        R = np.array([[1., 0., 0., 0.],
                      [0., np.cos(th), -np.sin(th), 0.],
                      [0., np.sin(th), np.cos(th), 0.],
                      [0., 0., 0., 1.]])
        
        # translate by (.4, 0., .2)
        T = np.array([[1., 0., 0., .4],
                      [0., 1., 0., 0.],
                      [0., 0., 1., .2],
                      [0., 0., 0., 1.]])

        I = np.identity(4)

        camAng = t

        # render(R, camAng)
        # render(T, camAng)
        # render(T @ R, camAng)
        render(I, camAng)
        # render(R @ T, camAng)

        glfw.swap_buffers(window)

    glfw.terminate

if __name__ == "__main__":
    main()