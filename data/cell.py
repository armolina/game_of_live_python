from re import S
import numpy as np

class GameStatus:

    game_status = []
    number_cells_x = 0
    number_cells_y = 0

    def status(self, number_cells_x, number_cells_y):
        
        self.number_cells_x = number_cells_x
        self.number_cells_y = number_cells_y

        self.game_status = np.zeros((number_cells_x, number_cells_y))
        
        self.game_status[2,2] = 1
        self.game_status[2,3] = 1
        self.game_status[2,4] = 1

        self.game_status[11,11] = 1
        self.game_status[12,12] = 1
        self.game_status[12,13] = 1
        self.game_status[11,13] = 1
        self.game_status[10,13] = 1

        return self.game_status

    def get_neighbours(self, game_status, x,y):
        neigh_alive = game_status[(x-1) % self.number_cells_x, (y-1) % self.number_cells_y] + \
                      game_status[x % self.number_cells_x, (y-1) % self.number_cells_y] + \
                      game_status[(x+1) % self.number_cells_x, (y-1) % self.number_cells_y] + \
                      game_status[(x-1) % self.number_cells_x, y % self.number_cells_y] + \
                      game_status[(x+1) % self.number_cells_x, y % self.number_cells_y] + \
                      game_status[(x-1) % self.number_cells_x, (y+1) % self.number_cells_y] + \
                      game_status[x % self.number_cells_x,  (y+1) % self.number_cells_y] + \
                      game_status[(x+1) % self.number_cells_x, (y+1) % self.number_cells_y]

        
        if(neigh_alive!=0):
            print (neigh_alive)

        return neigh_alive