import pygame
import random
import os

# from tut17 import screen_height

pygame.mixer.init()
# pygame.mixer.music.load('back.mpeg')
# pygame.mixer.music.play()


pygame.init()

# Color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)

screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))

# # Background Image
# bgimg = pygame.image.load("green.jpg")
# bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("SnakesWithRoni")
pygame.display.update()

#

clock = pygame.time.Clock()
font=pygame.font.SysFont(None,55)


def text_screen(text, color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_x ,snake_y,snake_size):
    # print(snk_list)
    for x,y in snk_list:
        if x == snake_x and y== snake_y:
            pygame.draw.rect(gameWindow,(38, 38, 30) ,[x,y, snake_size, snake_size])        # Rectangle
        else:
        # pygame.draw.rect(gameWindow,color,[snake_x, snake_y, snake_size, snake_size])        # Rectangle
            pygame.draw.rect(gameWindow,(108, 187, 60) ,[x,y, snake_size, snake_size])        # Rectangle

def draw_back(gameWindow,bg_image):
    list=[]
    background=pygame.image.load(bg_image)
    _,_,width,height = background.get_rect()
    for i in range(screen_width//width + 1):
        for j in range(screen_height//height + 1):
            pos=[i*width,j*height]
            list.append(pos)

    for t in list:
        gameWindow.blit(background,t)


playlist=["back.mpeg","love_your_self.mpeg","let_me_love.mpeg","star_boy.mpeg","PnB_Rock.mp3"]
current_song= 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play(-1)

def welcome():
    exit_game = False
    while not exit_game:
        # gameWindow.fill(white)
        gameWindow.fill((34, 139, 34))
        text_screen("Welcome To Roni's Snake Game",black,190,250)
        text_screen("Press Space Bar To Play",black,235,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Starting sound
                    pygame.mixer.music.load('beep.mp3')
                    pygame.mixer.music.play()
                    # pygame.time.delay(500)
                    # pygame.mixer.music.load('back.mpeg')
                    # pygame.mixer.music.play(-1)
                    play_music()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables

    exit_game = False
    game_over = False
    velocity_x=0
    velocity_y=0
    snake_x = 45
    snake_y = 55
    snk_list = []
    snk_length = 1
    # Check if hiscore file existes
    if (not os.path.exists("heighest_Score.txt")):
        with open("Heighest_Score.txt", "w") as f:
            f.write("0")
    with open("Heighest_Score.txt", "r") as f:
        Hiscore = f.read()

    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 30

    while not exit_game:
        if game_over:
            with open("Heighest_Score.txt", "w") as f:
                f.write(str(Hiscore))
            # gameWindow.fill(white)
            gameWindow.fill((233, 220, 229))
            text_screen("Score: "+str(score), blue, 100,210)
            text_screen("Game Over ! Press Enter To Continue", red, 100,250)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # gameloop()
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    # NEXT SONG
                    global current_song
                    if event.key == pygame.K_n:
                        current_song = (current_song + 1) % len(playlist)
                        play_music()

                    # PREVIOUS SONG
                    if event.key == pygame.K_b:
                        current_song = (current_song - 1) % len(playlist)
                        play_music()

                    if event.key == pygame.K_RIGHT:
                        snake_x = snake_x + 5
                        velocity_x = init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_LEFT:
                        snake_x = snake_x - 5
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        snake_y -= 5
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        snake_y += 5
                        velocity_y= init_velocity
                        velocity_x = 0

                    # if event.key == pygame.K_q:         #Cheat code
                    #     score += 50

                    if event.key == pygame.K_v:
                        velocity_x += 1
                    if event.key == pygame.K_a:
                        velocity_x -= 1
                    if event.key == pygame.K_s:
                        snake_size -=5
                    if event.key == pygame.K_m:
                        snake_size +=5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                # print("score: ",score)
                # text_screen("score: "+ str(score),red,5,5)
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snk_length += 5
                if score>int(Hiscore):
                    Hiscore = score

            gameWindow.fill(white)
            # gameWindow.blit(bgimg, (0,0))
            draw_back(gameWindow,"Brown.png")
            text_screen("score: "+ str(score) + "  Hiscore: "+str(Hiscore),blue,5,5)
            # pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            pygame.draw.circle(gameWindow,red,(food_x, food_y), snake_size//2)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1] :         # list[START:STOP] So, list[:-1] means it stop before -1/last element
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                # print("Game Over")
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size, snake_size])        # Rectangle
            plot_snake(gameWindow,black,snk_list,snake_x ,snake_y,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
# gameloop()