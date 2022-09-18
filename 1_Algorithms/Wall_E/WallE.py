import math, pygame
from math import pi

class WallE:

    def turn(self, angle):
        x = self.direction[0]
        y = self.direction[1]
        self.direction = [int(x*math.cos(angle)-y*math.sin(angle)),
                            int(x*math.sin(angle)+y*math.cos(angle))]
        self.image = self.imageDict[str(self.direction)]

    def turn_right(self):
        self.turn(0.5*pi)

    def turn_left(self):
        self.turn(-0.5*pi)

    def check_on_box(self):
        if self.board[self.position[0]][self.position[1]] == 2:
            return True
        else:
            return False

    def check_wall(self):
        x = self.position[0] + self.direction[0]
        y = self.position[1] + self.direction[1]
        if -1 < x < len(self.board) and -1 < y < len(self.board[0]):
            if self.board[x][y]==1:
                return True
            return False
        else:
            return True

    #Requires an action
    def pick_up_box(self):
        if not self.action:
            if self.board[self.position[0]][self.position[1]] == 2:
                self.board[self.position[0]][self.position[1]] = 0
            else:
                self.broken = True
            self.action = True
        else:
            self.broken = True

    #Requires an action
    def drop_box(self):
        if not self.action:
            if self.board[self.position[0]][self.position[1]] == 0:
                self.board[self.position[0]][self.position[1]] = 2
            else:
                self.broken = True
            self.action = True
        else:
            self.broken = True

    #Requires an action
    def move(self):
        if not self.action:
            self.position[0] += self.direction[0]
            self.position[1] += self.direction[1]
            if -1 < self.position[0] < len(self.board) and -1 < self.position[1] < len(self.board[0]):
                if self.board[self.position[0]][self.position[1]]==1:
                    self.broken = true
            else:
                self.broken = True
            self.action = True
        else:
            self.broken = True

    def __init__(self, position, board, image):
        self.position = position
        self.board = board
        self.direction = [1,0]
        self.image = image
        il = pygame.transform.flip(self.image, True, False)
        ir = pygame.transform.rotate(self.image, 0)
        id = pygame.transform.rotate(self.image, -90)
        iu = pygame.transform.rotate(self.image, 90)
        self.imageDict = {'[1, 0]':ir, '[-1, 0]':il, '[0, 1]':id, '[0, -1]':iu}
        self.action = False
        self.broken = False

        #-----------------------------------------------------------------------
        # Declare variables you need here:
        self.turns = 0


    def walk_back_and_forth(self):
        if not self.check_wall():
            self.move()
        elif self.turns<2:
            self.turn_left()
            self.turns+=1

    def walk_a_lap(self):
        if not self.turns == 4:
            if not self.check_wall():
                self.move()
            else:
                self.turn_right()
                self.turns+=1

    def find_the_box(self):
        pass

    def swap_all_boxes(self):
        pass

    def walk_around_obstacle(self):
        pass
