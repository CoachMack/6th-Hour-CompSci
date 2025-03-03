#Name: Coach Mack
#Class: 5th Hour
#Assignment: Lecture - Minecwaf

#This... is not Minecraft. This is a Large Language Model's attempt at hallucinating something
#resembling Minecraft. LLMs, or "AI" as they tend to be marketed, is a prompt interpreter software
#that takes the user prompt and uses an incredible amount of data to basically "answer" that question.
#LLMs are robust and can essentially paraphrase complex questions into simpler answers, or generate
#simple products for you but as these examples below show, they cannot generate something as complex
#as Minecraft.

#Ultimately, my belief is that LLMs should not be used to replace one of three things:
#People's jobs
#People's creativity
#People's curiosity

#Especially when the average ChatGPT query consumes 2.9Wh of electricity compared to a Google search
#which produces 0.3 Wh. If you are having it write a research paper for you, you can't know if it
#didn't make anything up accidentally without doing the research to verify and at that point, it
#would make more sense to just have googled in the first place. In a similar vein, having it generate
#code for you makes you unable to understand the code and thus unable to expand features for future
#use cases. If you knew how to expand features, you would've just made the code yourself in the first
#place. Or in other words: https://www.youtube.com/watch?v=TbllP2FOvEE

#Minecwaf

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
'''
# Define the 3D cube vertices
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the surfaces (faces) of the cube
surfaces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
]

# Color scheme for cubes (for a more Minecraft-like feel)
# Let's keep it simple with stone-like and grass-like textures
block_colors = [
    (0.6, 0.6, 0.6),  # Stone
    (0.6, 0.3, 0.1),  # Dirt
    (0.0, 1.0, 0.0),  # Grass (green)
]

# Function to draw a single cube with a specific color
def draw_cube(color):
    glBegin(GL_QUADS)
    glColor3fv(color)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Black for edges (subtle, not neon)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Function to initialize the game window
def init_game():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

# Function to handle user input for camera movement
def handle_input():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glTranslatef(0.1, 0, 0)
    if keys[K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keys[K_UP]:
        glTranslatef(0, 0.1, 0)
    if keys[K_DOWN]:
        glTranslatef(0, -0.1, 0)

# Function to generate a simple world of blocks (dirt, stone, and grass)
def generate_world():
    world = []
    for x in range(-5, 5):
        for y in range(-5, 5):
            for z in range(-5, 5):
                if z == -5:  # Ground level: dirt
                    world.append((x, y, z, block_colors[1]))
                elif z == 0:  # Grass on top of dirt
                    world.append((x, y, z, block_colors[2]))
                else:  # Stone in the air
                    world.append((x, y, z, block_colors[0]))
    return world

# Main game loop
def game_loop():
    init_game()
    world = generate_world()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_input()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for block in world:
            x, y, z, color = block
            glPushMatrix()
            glTranslatef(x, y, z)
            draw_cube(color)
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    game_loop()
'''

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Define the 3D cube vertices
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the surfaces (faces) of the cube
surfaces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
]

# Define colors for the cube faces
colors = [
    (1, 0, 0),  # red
    (0, 1, 0),  # green
    (0, 0, 1),  # blue
    (1, 1, 0),  # yellow
    (1, 0, 1),  # magenta
    (0, 1, 1)   # cyan
]

# Function to draw a single cube
def draw_cube():
    glBegin(GL_QUADS)
    for surface, color in zip(surfaces, colors):
        glColor3fv(color)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Black for edges
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Function to initialize the game window
def init_game():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Function to handle user input for camera movement
def handle_input():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glTranslatef(0.1, 0, 0)
    if keys[K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keys[K_UP]:
        glTranslatef(0, 0.1, 0)
    if keys[K_DOWN]:
        glTranslatef(0, -0.1, 0)

# Function to generate a random 3D world of cubes
def generate_world():
    world = []
    for x in range(-5, 5):
        for y in range(-5, 5):
            for z in range(-5, 5):
                if random.random() > 0.7:  # 30% chance to generate a block
                    world.append((x, y, z))
    return world

# Main game loop
def game_loop():
    init_game()
    world = generate_world()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_input()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for block in world:
            glPushMatrix()
            glTranslatef(block[0], block[1], block[2])
            draw_cube()
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    game_loop()
