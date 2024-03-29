import glfw
from OpenGL.GL import *

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0., 0.)
    glVertex2f(0., 1.)
    glColor3f(.0, 1., 0.)
    glVertex2f(-1., -1.)
    glColor3f(.0, 0., 1.)
    glVertex2f(1., -1.)
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render()

        glfw.swap_buffers(window)

    glfw.terminate

if __name__ == "__main__":
    main()