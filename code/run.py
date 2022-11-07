#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:55:11 2021

@author: kris

MIT License

Copyright (c) [2021] [Liangyawei Kuang @HKUST]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import pygame
from pygame.locals import *
from constants import *
from agent import Agent 

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
# =============================================================================
# pygame.display.set_mode(size=(0, 0), flags=0, depth=0)
# pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0)
# size=(SCREENWIDTH, SCREENHEIGHT)
# The flags argument controls which type of display you want.
# The depth argument represents the number of bits to use for color.
# The display index 0 means the default display is used. If no display index argument is provided, the default display can be overridden with an environment variable.
# The vsync means vertical sync.
# =============================================================================
        self.background = None
        self.clock = pygame.time.Clock()
        
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(WHITE)
        
    def startGame(self):
        self.setBackground()
        self.agent = Agent()

    def update(self):
        dt = self.clock.tick(30) / 1000.0
        self.agent.update(dt)
        self.checkEvents()
        self.render()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.agent.render(self.screen)
        pygame.display.update()
        
if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()