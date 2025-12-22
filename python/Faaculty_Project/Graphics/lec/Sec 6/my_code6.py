from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
angle = 0.0


def display_view():
    glClearColor(0, 0, 0, 1.0)
    glLoadIdentity()
    gluPerspective(45, 1, 1.0, 100)
    glEnable(GL_DEPTH_TEST)


def object1():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # الوجه الخلفي (أخضر)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # الوجه العلوي (أحمر)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # الوجه السفلي (أصفر)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    # الوجه الأيمن (أرجواني)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)

    # الوجه الأيسر (سماوي)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    glEnd()


def display():
    global angle
    angle += 0.1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    glRotatef(angle, 1, 1, 1)
    object1()
    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"3D Object")

    display_view()
    glutDisplayFunc(display)
    glutMainLoop()


main()
