# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:40:26 2024

@author: El Mehdi
"""

from OpenGL.GL import (
    glClearColor,
    glColor3f,
    glPointSize,
    glClear,
    glBegin,
    glVertex2f,
    glEnd,
    glFlush,
    GL_COLOR_BUFFER_BIT,
    GL_POINTS,
)
from OpenGL.GLUT import (
    glutInit,
    glutInitDisplayMode,
    glutInitWindowSize,
    glutInitWindowPosition,
    glutCreateWindow,
    glutDisplayFunc,
    glutMainLoop,
    GLUT_SINGLE,
    GLUT_RGB,
)
from OpenGL.GLU import gluOrtho2D


def myInit():
    glClearColor(0, 0, 1.0, 1.0)
    glColor3f(0.2, 0.5, 0.4)
    glPointSize(10.0)
    gluOrtho2D(0, 500, 0, 500)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    glVertex2f(100, 100)
    glVertex2f(300, 200)
    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Test window")
myInit()
glutDisplayFunc(display)
glutMainLoop()
