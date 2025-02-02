import pygame, sys, random
import math
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\head_up2.png').convert_alpha()
        self.head_down = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\head_down2.png').convert_alpha()
        self.head_right = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\head_right2.png').convert_alpha()
        self.head_left = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\head_left2.png').convert_alpha()

        self.tail_up = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\tail_up2.png').convert_alpha()
        self.tail_down = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\tail_down2.png').convert_alpha()
        self.tail_right = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\tail_right2.png').convert_alpha()
        self.tail_left = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_vertical2.png').convert_alpha()
        self.body_horizontal = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_horizontal2.png').convert_alpha()

        self.body_tr = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_tr2.png').convert_alpha()
        self.body_tl = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_tl2.png').convert_alpha()
        self.body_br = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_br2.png').convert_alpha()
        self.body_bl = pygame.image.load('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\body_bl2.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound ('C:\\Users\\mehdi\\Desktop\\nsi\\titanic\\my_tita\\myenv\\snakegame\\crunch.wav')




    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)

            elif index == len (self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)

                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else :
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
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    
    def play_crunch_sound (self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.state = 'menu'

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over

    def game_over(self):
        self.snake.reset()
        self.state = 'menu'

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size , cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size , cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)

    def draw_menu(self, background_image):
        screen.blit(background_image,(0, 0))
        play_button.draw()
        credits_button.draw()
        

    def draw_credits(self):
        screen.fill((0, 0, 0))
        credits_text = game_font.render("Credits", True, (255, 255, 255))
        name1_text = game_font.render("Mehdi Benkhadra", True, (255, 255, 255))
        name2_text = game_font.render("Fahd EL Rhazouani", True, (255, 255, 255))
        back_button.draw()
        credits_rect = credits_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2 - 50))
        name1_rect = name1_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2))
        name2_rect = name2_text.get_rect(center=(cell_number * cell_size // 2, cell_number * cell_size // 2 + 50))
        screen.blit(credits_text, credits_rect)
        screen.blit(name1_text, name1_rect)
        screen.blit(name2_text, name2_rect)

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(None, 50)
        if feedback == "":
            self.feedback = text
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, True, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('C:/Users/mehdi/Desktop/nsi/titanic/my_tita/myenv/snakegame/apple2.png').convert_alpha()
background_image = pygame.image.load('C:/Users/mehdi/Desktop/nsi/titanic/my_tita/myenv/snakegame/menu_background.jpg').convert_alpha()
game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

play_button = Button("Play", (cell_number * cell_size // 2 - 50, cell_number * cell_size // 2), game_font)
credits_button = Button("Credits", (cell_number * cell_size // 2 - 50, cell_number * cell_size // 2 + 50), game_font)
back_button = Button("Back", (cell_number * cell_size // 2 - 50, cell_number * cell_size // 2 + 100), game_font)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #up
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_2: #down
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_3: #left
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_4: #right 
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_game.state == 'menu':
                if play_button.is_clicked(event.pos):
                    main_game.state = 'game'
                if credits_button.is_clicked(event.pos):
                    main_game.state = 'credits'
            elif main_game.state == 'credits':
                if back_button.is_clicked(event.pos):
                    main_game.state = 'menu'
        
    if main_game.state == 'menu':
        main_game.draw_menu(background_image)
    elif main_game.state == 'credits':
        main_game.draw_credits()
    elif main_game.state == 'game':
        screen.fill((175,215,70))
        main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)