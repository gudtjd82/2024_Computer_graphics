import glfw
from OpenGL.GL import *

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_A:
        if action == glfw.PRESS:
            print("press a")
        elif action == glfw.RELEASE:
            print("release a")
        elif action == glfw.REPEAT:
            print("repeat a")
    elif key == glfw.KEY_SPACE and action == glfw.PRESS:
        print("press sapce: (%d, %d)" %glfw.get_cursor_pos(window))

def cursor_callback(window, xpos, ypos):
    print("mouse cursor moving: (%d, %d)" %(xpos, ypos))

def button_callback(window, button, action, mod):
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            print("press left btn:(%d, %d)" %glfw.get_cursor_pos(window))
        elif action == glfw.RELEASE:
            print("release left btn:(%d, %d)" %glfw.get_cursor_pos(window))

def scroll_callback(window, xoffset, yoffset):
    print("mouse whell scroll: %d, %d" %(xoffset, yoffset))
        

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.set_key_callback(window, key_callback)
    glfw.set_cursor_pos_callback(window, cursor_callback)
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_scroll_callback(window, scroll_callback)

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render()

        glfw.swap_buffers(window)

    glfw.terminate

if __name__ == "__main__":
    main()