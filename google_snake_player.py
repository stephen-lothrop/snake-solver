#! python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:42:50 2018

@author: Stephen Lothrop
"""

import pyautogui

#pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
pos = pyautogui.position()
pyautogui.click(pos)
width, height = pyautogui.size()

apple = 'apple.png'
top_left_corner = 'top_left_corner.png'
bottomr_right_corner = 'bottom_right_corner.png'

snake_color = (78, 124, 246)
apple_color = (232, 72, 29)

cols = 16
rows = 14

left, top = pyautogui.center(pyautogui.locateOnScreen(top_left_corner))
right, bottom = pyautogui.center(pyautogui.locateOnScreen(bottomr_right_corner))
sqr_width = (right - left) / 17
sqr_height = (bottom - top) / 15
class Snake(object):
    # A snake has an x, y coordinates of its head
    # the snake is moving in direction, which is a string
    # direction is one of: up, down, left, right
    def __init__(self, x, y, direction, left, top, sqr_width, sqr_height):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 0
        self.direction = direction
        self.color = (78, 124, 246)
        self.left = left
        self.top = top
        self.sqr_width = sqr_width
        self.sqr_height = sqr_height
        
    def newDir(self, direction):
        pyautogui.press(direction)
        self.direction = direction
        old_coord = (s.x, s.y)
        if(direction == 'up'):
            self.dy = -1
            self.dx = 0
        elif(direction == 'down'):
            self.dy = 1
            self.dx = 0
        elif(direction == 'right'):
            self.dx = 1
            self.dy = 0
        elif(direction == 'left'):
            self.dx = -1
            self.dy = 0
        while((s.x, s.y) == old_coord):
            s.track()
    
    def track(self):
        if(pyautogui.pixelMatchesColor(round((left + (sqr_width * 
                                                      (s.x + 0.5 + self.dx)))),
                                       round((top + (sqr_height * 
                                                 (s.y + 0.5 + self.dy)))),
                                       self.color,
                                       tolerance=10)):
            self.x += self.dx
            print('x: ' + str(self.x))
            self.y += self.dy
            print('y: ' + str(self.y))
                
    
def main_loop():
    if(s.x == cols and s.direction == "right"):
        s.newDir("down")
        s.newDir("left")
    elif(s.x == 1 and s.direction == "left"):
        s.newDir("down")
        s.newDir("right")        
    
    
s = Snake(4, 7, 'right', left, top, sqr_width, sqr_height)
s.newDir('up')
i = 0
loop_num = 0
while(s.y > 0):
    s.track()
    print(s.dy)
    
while True:
    i += 1
    s.track()
    if(s.y == rows and s.direction == "down"):
        s.newDir("left")
    elif(s.x == 0 and s.direction == "left"):
        s.newDir("up")
    elif(s.y == 0 and s.direction == "up"):
        s.newDir("right")
    elif(s.y == (rows - 2) and s.x == cols):
        s.newDir('down')
    elif(s.y < (rows - 2) or s.y == (rows - 1)):
        main_loop()
        print("main loop")        
    if(i == 4000):
        break
    #print('s.x: ' + str(s.x) + ' s.y: ' + str(s.y) + ' s.dir: ' + str(s.direction))
        
#elif(s.x == 0 and s.direction == "left"):
#    s.newDir("down")
#    temp = s.y
#    while(s.y <= temp):
#        s.track()
#    s.newDir("right")    