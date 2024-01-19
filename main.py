
# Modification date: Sun Feb 14 22:08:46 2021

# Production date: Sun Sep  3 15:43:43 2023

import pygame
from time import *
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen(width, height)
win = pygame.display.set_mode((800, 640))

# Background
background = pygame.image.load("Bedroom.png")


# Title and icon
pygame.display.set_caption("The Giant Enemy Spider")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


clock = pygame.time.Clock()


# Walking
#walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
walkRight = [pygame.image.load('Player.png'),pygame.image.load('Player.png'),pygame.image.load('Player.png')]
walkLeft = [pygame.image.load('Player.png'),pygame.image.load('Player.png'),pygame.image.load('Player.png')]
charr = pygame.image.load('player.png')
charl = pygame.image.load('Player.png')#Playerleft



class player(object):
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 7
        self.direction = "right"

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//1], (self.x,self.y))#not 1, 3
            self.walkCount += 1
            self.direction = "left"
        elif self.right:
            win.blit(walkRight[self.walkCount//1], (self.x,self.y))#not 1, 3
            self.walkCount +=1
            self.direction = "right"
        else:
            if self.direction == "right":
                win.blit(charr, (self.x,self.y))
            if self.direction == "left":
                win.blit(charl, (self.x,self.y))


class chair(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        if emap == 2:
            win.blit(chairp, (self.x - 50, self.y))
        else:
            win.blit(chairp, (self.x + 500, self.y))


def redrawGameWindow():
    win.blit(background, (0,0))
    man.draw(win)
    pygame.display.update()



man = player(162, 100, 384, 384, "right")
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > 130:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 1240:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -7:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 7

    redrawGameWindow()

    pygame.display.update()
