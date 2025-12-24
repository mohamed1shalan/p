from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1, 100)  # تصحيح: إضافة فاصلة ناقصة
    glMatrixMode(GL_MODELVIEW)  # تصحيح: GL_MODELVIEW بدلاً من GL_PROELVIEW

    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5,  # تصحيح: gluLookAt بدلاً من glLuLookAt
              0, 0, 0,
              0, 1, 0)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # تصحيح: GL_LIGHT0 بدلاً من GL_LIGHT
    # تصحيح: glLightfv بدلاً من glLight
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])

    # تصحيح: glutSolidSphere بدلاً من glutsolidSphere
    glutSolidSphere(1, 50, 50)
    glutSwapBuffers()  # تصحيح: glutSwapBuffers بدلاً من glutSnapBuffers


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"3D Sphere in PyOpenGL")  # تصحيح: إضافة b قبل النص

glClearColor(0.1, 0.1, 0.1, 1)
init()
glutDisplayFunc(display)
glutMainLoop()
