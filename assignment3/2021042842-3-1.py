import glfw
from OpenGL.GL import * 
from OpenGL.GLU import *
import numpy as np

move_x = 0
rotate = np.radians(0)
# global_M = np.identity(3)
reset = False

def key_callback(window, key, scancode, action, mods):
    global move_x, rotate, reset
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_Q:
            move_x += -0.1
        elif key == glfw.KEY_E:
            move_x += 0.1
        elif key == glfw.KEY_A:
            rotate += np.radians(10)
        elif key == glfw.KEY_D:
            rotate += np.radians(-10)
        elif key == glfw.KEY_1:
            reset = True
    pass

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # draw cooridnate
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.])) 
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.])) 
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
    glEnd()

def main():
    global move_x, rotate, reset

    if not glfw.init():
        return
    window = glfw.create_window(480,480, "2021042842-3-1", None,None)
    if not window: 
        glfw.terminate() 
        return

    glfw.make_context_current(window) 
    glfw.set_key_callback(window, key_callback)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window): 
        glfw.poll_events()
        
        M = np.identity(3)
        
        if reset:
            move_x = 0
            rotate = np.radians(0)
            reset = False
        else:
            T = np.identity(3)
            R = np.identity(3)

            T[:2, 2] = [move_x, 0]
            R[:2, :2] = [[np.cos(rotate), -np.sin(rotate)],
                         [np.sin(rotate), np.cos(rotate)]]
            M = M @ T @ R

        render(M)

        glfw.swap_buffers(window) 
    glfw.terminate()

if __name__ == "__main__": 
    main()
