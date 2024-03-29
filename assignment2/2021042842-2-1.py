import glfw
from OpenGL.GL import *
import numpy as np

primitive_type = 1

def render():
    global primitive_type
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # draw triangle
    if primitive_type == 1:
        glBegin(GL_POINTS)
    elif primitive_type == 2:
        glBegin(GL_LINES)
    elif primitive_type == 3:
        glBegin(GL_LINE_STRIP)
    elif primitive_type == 4:
        glBegin(GL_LINE_LOOP)
    elif primitive_type == 5:
        glBegin(GL_TRIANGLES)
    elif primitive_type == 6:
        glBegin(GL_TRIANGLE_STRIP)
    elif primitive_type == 7:
        glBegin(GL_TRIANGLE_FAN)
    elif primitive_type == 8:
        glBegin(GL_QUADS)
    elif primitive_type == 9:
        glBegin(GL_QUAD_STRIP)
    elif primitive_type == 0:
        glBegin(GL_POLYGON)
        
    glColor3ub(255, 255, 255)
    for i in range(12):
        th = np.radians(30*i)
        # glVertex2f(np.cos(th)*0.5, np.sin(th)*0.5)
        glVertex2f(np.cos(th), np.sin(th))
    glEnd()

def key_callback(window, key, scancode, action, mods): 
    global primitive_type
    if key==glfw.KEY_1 and action == glfw.PRESS:
        primitive_type = 1
    elif key==glfw.KEY_2 and action == glfw.PRESS:
        primitive_type = 2
    elif key==glfw.KEY_3 and action == glfw.PRESS:
        primitive_type = 3
    elif key==glfw.KEY_4 and action == glfw.PRESS:
        primitive_type = 4
    elif key==glfw.KEY_5 and action == glfw.PRESS:
        primitive_type = 5
    elif key==glfw.KEY_6 and action == glfw.PRESS:
        primitive_type = 6
    elif key==glfw.KEY_7 and action == glfw.PRESS:
        primitive_type = 7
    elif key==glfw.KEY_8 and action == glfw.PRESS:
        primitive_type = 8
    elif key==glfw.KEY_9 and action == glfw.PRESS:
        primitive_type = 9
    elif key==glfw.KEY_0 and action == glfw.PRESS:
        primitive_type = 0


def main():
    if not glfw.init():
        return

    window = glfw.create_window(480, 480, "2021042842-2-1", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)

    glfw.make_context_current(window)

    # glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render()

        glfw.swap_buffers(window)

    glfw.terminate

if __name__ == "__main__":
    main()