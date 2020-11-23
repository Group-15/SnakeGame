import pygame, sys, random
from pygame import mixer
from pygame.math import Vector2

#Angels code
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sounds/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size, cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):  self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
        # creates and draws the rectangle

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

#Tanees code:
# -def __init__(self): Initiates the fruit class
# -def draw_fruit(self): is a function that creates a Rectangle from the pygame library that takes (x coordinates, y coordinates, width, height)
# -def randomize(self): is a function to randomize the x and y coordinates of the apple
class FRUIT:
    def __init__(self):
       self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # create a rectangle and draw a rectangle

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

#Davids code:
# -def def __init__(self, color, x, y, width, height, text= ''): initiates the BUTTON class and gives its parameters
# -def draw_button(self, screen): draws a rectangle with pygame that takes (x-coordinates, y coordinates, width, height)
# -def isOver(self,pos): is a function that has a if statement that will check if the mouse is over the mute button or not
class BUTTON:
    def __init__(self, color, x, y, width, height, text= ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, screen):
        button_rect = pygame.Rect(self.x-2, self.y, self.width, self.height)
        screen.blit(button, button_rect)

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

# Ismail code:
# -def __init__(self): initiates all of the classes
# -def update(self): function that updates the snake moving, checks collision of the apple and snake and checks whether the snake has hit the outer screen
# -def draw_elements(self): draws the main assets to the screen
# -def check_collision(self): checks if the fruit is in the same position as the snakes head
# then it randomizes the fruit, adds a block to the snake and plays the crunch sound
# -def check_fail(self): checks whether the snake has left the main screen size, and if it has it goes to the game over function
# -def game_over(self): resets the snake to its initial position
# -def draw_score(self): calculates the score by taking the snakes initial length of 3 and subtracts  it by 3
# creates the scores position and size, along with creating the rectangle around the score
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        # button (x, y, w, h)
        self.button = BUTTON((0, 0, 0), 20, 740, 46, 46, 'Mute')
        #self.high_score()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        #self.high_score()

    def draw_elements(self):
        #self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.button.draw_button(screen)
        self.draw_score()
        #self.high_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            #self.high_score()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

            # reposition the fruit and adds another block to snake

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        # check if snake is outside of the screen and check if snake hits itself

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
    """
    def high_score(self):
        score_text = str(0)
        score_up = score_text + str(1)
        #score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_up, True, (56, 74, 12))
        score_x = int(400)
        score_y = int(100)
        score_rect = score_surface.get_rect(center=(score_x, score_y))

        bg_rect = pygame.Rect(400, 100, 60, 30)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
    """

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# music for the game - Faizah code : uses pygame to load in the music, and set the volume
mixer.music.load('Music/bgmusic2.wav')
mixer.music.play(-1)
mixer.music.set_volume(.10)

# window icon and name - Faizah code
pygame.display.set_caption("Snake Game") # sets the name of the window to snake game
icon = pygame.image.load('Graphics/snakeicon.png') # loads the icon of the window
pygame.display.set_icon(icon) # sets the icon of the snake to the window

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # sets the main window size of the game to (800 x 800) by multiplying cell_size by cell number
clock = pygame.time.Clock()

# pics of apple, button and background
apple = pygame.image.load('Graphics/apple.png').convert_alpha() # Tanees code: loads the image of the apple
button = pygame.image.load('Graphics/button.png').convert_alpha() # Davids code: loads the image of the music button
background = pygame.image.load('Graphics/background.png').convert_alpha() # Faizah code: loads the image of the background
game_font = pygame.font.Font('freesansbold.ttf', 26) # Faizah code: loads the font of the score

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()
muteMath = 0

# Evelyn's Code:
# While loop that listens for the users key inputs: up arrow key, down arrow key,
# left arrow key, right arrow key, to move the snake in all directions
# also listens whether the mouse is over the mute button or not.
# It's the main loop of the game that updates everything along with checking if the user quit the game
while True:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_game.button.isOver(pos):
                muteMath += 1
                if (muteMath % 2) == 0:
                    pygame.mixer.music.unpause()
                elif (muteMath % 2) != 0:
                    pygame.mixer.music.pause()

    screen.fill((175, 215, 70))
    #actual background image
    screen.blit(background, (0, 0))
    main_game.draw_elements()
    pygame.display.update()# updates the game
    clock.tick(60) # sets the frames per second of the game to 60
