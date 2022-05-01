#!/usr/bin/env python
# coding: utf-8
import pygame
from random import randint
import os
import sys
import time
from pygame import mixer


pygame.init()
mixer.init()

SCREEN = pygame.display.set_mode((1000,600))

#mixer.music.load("soundtrack.mp3")


BG = pygame.image.load("stars.jpeg")
BG = pygame.transform.scale(BG,(1000,600))

SHIP = pygame.image.load("spaceship.png")
SHIP = pygame.transform.scale(SHIP,(70,70))

LASER = pygame.image.load("laser1.png")
LASER = pygame.transform.scale(LASER,(20,30))

INVADER = pygame.image.load("invader.png")
INVADER = pygame.transform.scale(INVADER,(50,30))

pygame.display.set_caption('Space Cadet')
font = pygame.font.Font('freesansbold.ttf', 32)
font_win = pygame.font.Font('freesansbold.ttf', 40)
text = font.render('Hello', True, (25,0,255))
textRect = text.get_rect()
textRect2 = text.get_rect()
textRect.center=(880,15)
textRect2.center = (45,15)
textRect3 = text.get_rect()
textRect3.center=(100,300)

class SpaceShip:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.score=0
    def move(self,by_x,by_y):
        self.x += by_x
        self.y += by_y
        if self.x>950:
            self.x=950
        if self.x<0:
            self.x=0
        if self.y>520:
            self.y=520
        if self.y<350:
            self.y=350
    def shoot(self):
        pass
        
class Laser:
    
    def __init__(self,x,y):
        self.x=x+25   
        self.y=y
        self.rect=pygame.Rect((self.x,self.y),(20,30))
    def move(self,x,y):
        self.x=x
        self.y=y
        if self.x<=1000 and self.x>=0 and self.y<=600 and self.y >= -40:
            self.y -= 5
        self.rect=pygame.Rect((self.x,self.y),(20,30))

class Invader:
    def __init__(self,speed,*args):
        self.x= randint(200,800)
        self.y= 0
        self.speed=speed
        self.teleport=speed
        self.rect=pygame.Rect((self.x,self.y),(50,30))
    def move(self,x,y):
        if self.x <1100 and self.x>0:
            self.x=self.x+self.speed
        if self.x>=950:
            self.speed= -self.teleport
        if self.x<=60:
            self.speed = self.teleport
        self.y += 0.3
        self.rect=pygame.Rect((self.x,self.y),(50,30))
        if self.y >=600 and self.x != 1200:
            print("YOU LOST")
            sys.exit()
    def destroy(self):
        self.x=1200
        self.y=0
        #def move():
        #    pass
        ship.score +=1


ship=SpaceShip(300,130)

invaders0 = []
for i in range(2):
    invaders0.append(Invader(2))
invaders1  = []
for i in range(4):
    invaders1.append(Invader(3))

invaders2 = []
for i in range(6):
    invaders2.append(Invader(4))

invaders3=[]
for i in range(10):
    invaders3.append(Invader(1))
    
invaders4=[]
for i in range(12):
    invaders4.append(Invader(1))

invaders5=[]
for i in range(20):
    invaders5.append(Invader(0.5))

invaders6=[]
for i in range(60):
    invaders6.append(Invader(0.3))

filler=[]
 
#last level doesnt show up for watever reason
levels=[invaders0,invaders1,invaders2,invaders3,invaders4,invaders5,
invaders6,filler]
lasers=[]
laser_shoot=False
laser=Laser(-10,-10)
invaders_curent=invaders0;
lvl=1
text_won=font_win.render(f"CONGRATS! YOU DEFENDED WELL (for now)",True,(0,200,0))
while True:
    text_score = font.render(f'Score:  {ship.score}', True, (20,200,255))
    text_level = font.render(f"Level:{lvl}",True,(255,200,20))
    
    SCREEN.blit(BG,(0,0))
    SCREEN.blit(SHIP,(ship.x,ship.y))
    SCREEN.blit(text_score, textRect)
    SCREEN.blit(text_level, textRect2)
    
    if lvl==7:
        SCREEN.blit(text_won, textRect3)

    #new stuff
    for level in levels:
        if lvl==7:
            SCREEN.blit(text_level, textRect2)
            break
        for invader in levels[lvl]:
            SCREEN.blit(INVADER,(invader.x,invader.y))
            invader.move(invader.x,invader.y)
            if laser_shoot:
                for x,laser in enumerate(lasers):
                        SCREEN.blit(LASER,(lasers[x].x,lasers[x].y))
                        laser.move(lasers[x].x,lasers[x].y)
                if pygame.Rect.colliderect(invader.rect,lasers[x].rect):
                    invader.destroy()
                    levels[lvl].remove(invader)
        if len(levels[lvl])==0:
            lvl=lvl+1
            #print(len(levels[lvl])) 
        print(f"LEVEL:{lvl}")
    """
    if ship.score>=1:
        invaders_curent=invaders1
    if ship.score>=5:
        invaders_curent=invaders2
    if ship.score>=13:
        invaders_curent=invaders3
    if ship.score>=29:
        invaders_curent=invaders4
    if ship.score>=49:
        invaders_curent=invaders5
    if ship.score==90:
        print("YOU WON")        
    """
    #print("SCORE:{}".format(ship.score))
    """
    for invader in invaders_curent:
        SCREEN.blit(INVADER,(invader.x,invader.y))
        invader.move(invader.x,invader.y)
        if pygame.Rect.colliderect(invader.rect,laser.rect):
            invader.destroy()
    """
    if laser_shoot:
        for laser in lasers:
            SCREEN.blit(LASER,(laser.x,laser.y))
            laser.move(laser.x,laser.y)


    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        ship.move(0,-5)
    if keys[pygame.K_DOWN]:
        ship.move(0,5)
    if keys[pygame.K_RIGHT]:
        ship.move(5,0)
    if keys[pygame.K_LEFT]:
        ship.move(-5,0)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_shoot=True
                mixer.music.load("shoot2.mp3")
                mixer.music.play()
                lasers.append(Laser(ship.x,ship.y))
    

    pygame.display.update()
    time.sleep((1/60))  
