import pygame as pg
import random
pg.init()

#Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#Class to represent one piece of the snake
class SnakePiece:
    def __init__(self, x_location, y_location):
        self.x_location = x_location
        self.y_location = y_location

    #Draws snake piece
    def draw(self, dir):
        if dir == 'right':
            self.x_location += 20
        elif dir == 'left':
            self.x_location += -20
        elif dir == 'up':
            self.y_location += -20
        elif dir == 'down':
            self.y_location += 20

        pg.draw.rect(screen, BLUE, [self.x_location, self.y_location, 20, 20])


#Class for our snake object
class Snake:
    def __init__(self):
        self.snake_pieces = [SnakePiece(20, 20)]
        self.length = 1
        self.direction = ['right']

    #Draws each piece of the snake
    def draw_snake(self, dir):
        self.direction.insert(0, dir)
        counter = 0
        for piece in self.snake_pieces:
            piece.draw(self.direction[counter])
            counter += 1

#Class to represent food 
class Food:
    def __init__(self):
        self.x_location = 180
        self.y_location = 180

    #Draws food on screen
    def draw_food(self):
        pg.draw.ellipse(screen, RED,
                        [self.x_location, self.y_location, 20, 20], 0)


#Pygame setup
size = [500, 500]
screen = pg.display.set_mode(size)
screen2 = pg.display.set_mode(size)
clock = pg.time.Clock()
pg.mouse.set_visible(0)

#Initialize snake and food objects
player = Snake()
food = Food()

#Initialize snake coordinates and direction
direction = 'right'
x_coor = 20
y_coor = 20

#Start of game loop
done = False
while not done:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    #Read keyboard input
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        direction = 'left'
    if keys[pg.K_RIGHT]:
        direction = 'right'
    if keys[pg.K_UP]:
        direction = 'up'
    if keys[pg.K_DOWN]:
        direction = 'down'

    screen.fill(GREEN)

    if (player.snake_pieces[0].x_location == food.x_location
            and player.snake_pieces[0].y_location == food.y_location):

        if (player.direction[player.length - 1] == 'right'):
            player.snake_pieces.append(
                SnakePiece(
                    player.snake_pieces[player.length - 1].x_location - 20,
                    player.snake_pieces[player.length - 1].y_location))

        elif (player.direction[player.length - 1] == 'left'):
            player.snake_pieces.append(
                SnakePiece(
                    player.snake_pieces[player.length - 1].x_location + 20,
                    player.snake_pieces[player.length - 1].y_location))

        elif (player.direction[player.length - 1] == 'up'):
            player.snake_pieces.append(
                SnakePiece(
                    player.snake_pieces[player.length - 1].x_location,
                    player.snake_pieces[player.length - 1].y_location + 20))

        elif (player.direction[player.length - 1] == 'down'):
            player.snake_pieces.append(
                SnakePiece(
                    player.snake_pieces[player.length - 1].x_location,
                    player.snake_pieces[player.length - 1].y_location - 20))

        player.length += 1
        food.x_location = random.randint(1, 23) * 20
        food.y_location = random.randint(1, 23) * 20
    food.draw_food()
    player.draw_snake(direction)
    pg.display.update()

    if (player.snake_pieces[0].x_location >= 500
            or player.snake_pieces[0].x_location <= 0
            or player.snake_pieces[0].y_location >= 500
            or player.snake_pieces[0].y_location <= 0):
        done = True
    
    for i in range(1, player.length):
      if (player.snake_pieces[0].x_location == player.snake_pieces[i].x_location and player.snake_pieces[0].y_location == player.snake_pieces[i].y_location):
        done = True
