import time
import numpy as np
import pygame

from data.cell import GameStatus
from data.rules import Rules

def init(width, height):
    pygame.init()

    screen = pygame.display.set_mode((width, height))

    bg = 25,25,25
    screen.fill(bg)

    grid(width, height, screen)
    

def grid(width, height, screen):
    number_cells_x = 25
    number_cells_y = 25

    width_cell = width/number_cells_x
    height_cell = height/number_cells_y

    game_status = GameStatus()
    status = game_status.status(number_cells_x, number_cells_y)
    rules = Rules()

    while True:
        new_game_status = np.copy(status)
        
        bg = 25,25,25
        screen.fill(bg)
        time.sleep(1)

        for y in range(0, number_cells_x):
            for x in range(0, number_cells_y):
                
                cell = [(x * width_cell      , y * height_cell),
                        ((x+1) * width_cell    , y * height_cell),
                        ((x+1) * width_cell    , (y+1) * height_cell),
                        (x * width_cell     , (y+1) * height_cell)]

                if(status[x,y] == 0 and game_status.get_neighbours(status,x,y)==3):
                    new_game_status[x,y]=1
                elif(status[x,y] == 1 and (game_status.get_neighbours(status,x,y) < 2 or game_status.get_neighbours(status,x,y) > 3)):
                    new_game_status[x,y]=0


                if(new_game_status[x,y]==0):
                    pygame.draw.polygon(screen, (128,128,128), cell, 1)
                else:
                    pygame.draw.polygon(screen, (255,255,255), cell, 0)
            
        status = np.copy(new_game_status)
        pygame.display.flip()