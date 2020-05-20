#initialising
import pygame
import math
import random
import sys
from pygame import mixer
pygame.init()

#colour
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BACKGROUND_COLOR=(0,0,0)

#screen
WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))

# Caption and Icon
pygame.display.set_caption("COVID-19")
icon = pygame.image.load('Covid1.png')
pygame.display.set_icon(icon)

#font
font_style = pygame.font.SysFont("Times", 70)
myFont = pygame.font.SysFont("comicsansms", 25)
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
info_font=pygame.font.Font('freesansbold.ttf',16)
com=pygame.font.SysFont("comicsansms",25)
#Clock
clock = pygame.time.Clock()

#Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Score
score=0
score_value = 0

#background
bg_6 = pygame.image.load('bg6.jpg')
bg_1=pygame.image.load('bg1.jpg')
bg_2=pygame.image.load('bg2.jpg')
bg_3=pygame.image.load('bg3.jpg')
bg_4=pygame.image.load('bg4.png')
bg_5=pygame.image.load('bg5.jpg')
bg_7=pygame.image.load('bg7.jpg')

#player_game1
player_size=50
player_image=pygame.image.load('player.png')
player_pos=[400,500]

# Player_game2
playerImg = pygame.image.load('doctor.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy_game1
enemy_image=pygame.image.load('covid.png')
enemy_pos=[random.randint(0,750),0]
enemy_list=[enemy_pos]
enemy_size=50

# Enemy_game2
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('covid.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#pills
pillImg = pygame.image.load('pill.png')
pillX = 0
pillY = 480
pillX_change = 0
pillY_change = 10
pill_state = "ready"

#others
SPEED=10
textX = 10
testY = 10

#game_1 functions

def notice_1(msg,colour):
    no_1=font_style.render(msg,True,colour)
    screen.blit(no_1,[250,200])
def notice_2(msg,colour):
    no_2=com.render(msg,True,colour)
    screen.blit(no_2,[350,350])
def notice_3(msg,colour):
    no_3=myFont.render(msg,True,colour)
    screen.blit(no_3,[150,500])
def message(msg, color):
    mesg = myFont.render(msg, True, color)
    screen.blit(mesg, [300,300])
def notice_4(msg,colour):
    no_4=font_style.render(msg,True,colour)
    screen.blit(no_4,[50,100])
def notice_5(msg,colour):
    no_5=info_font.render(msg,True,colour)
    screen.blit(no_5,[300,300])
def notice_6(msg,colour):
    no_6=com.render(msg,True,colour)
    screen.blit(no_6,[300,200])
def notice_7(msg,colour):
    no_7=info_font.render(msg,True,colour)
    screen.blit(no_7,[50,500])

def set_level(score, SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 12
    else:
        SPEED = 15
    return SPEED
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0,WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
                screen.blit(enemy_image,(enemy_pos[0],enemy_pos[1]))


def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
    return False

#game_1 loop
intro=True
while intro:
    screen.fill((0,0,0))
    screen.blit(bg_1,(0,0))
    notice_1("COVID-19",RED)
    notice_2("Press ENTER",WHITE)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                intro=False
                break
ins=True
while ins:
    screen.blit(bg_6,(0,0))
    notice_4("LEVEL 1: ESCAPE",WHITE)
    notice_5("*Score 200 to unlock next level",YELLOW)
    notice_6("Press ENTER",RED)
    notice_7("HINT:Use arrow keys to navigate",YELLOW)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                ins=False
                break


def game_loop():
    game_over=False
    game_close=False

    player_pos=[400,500]
    x=player_pos[0]
    y=player_pos[1]
    score=0
    SPEED=10

    while not  game_over:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= player_size
                elif event.key == pygame.K_RIGHT:
                    x += player_size
        player_pos = [x,y]
        if x<=0:
            x=0
        if x>=736:
            x=736


        screen.fill(BACKGROUND_COLOR)
        screen.blit(bg_2,(0,0))
        drop_enemies(enemy_list)
        score = update_enemy_positions(enemy_list, score)
        if score>=200:
            game_over=True
            break

        SPEED = set_level(score, SPEED)
        text1 = "Score:" + str(score)
        label = myFont.render(text1, 1, BLUE)
        screen.blit(label, (WIDTH-200, HEIGHT-40))

        if collision_check(enemy_list,player_pos):
            game_close=True
            while game_close==True:
                screen.blit(bg_1,(0,0))
                message("You Lost! Press Esc-Quit", WHITE)
                notice_4("Better Luck Next Time...",YELLOW)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_over = True
                            game_close=False
                            pygame.quit()
                            quit()


        draw_enemies(enemy_list)
        screen.blit(player_image,(player_pos[0],player_pos[1]))
        clock.tick(30)
        pygame.display.update()

game_loop()

#game_2 functions

def info_1(x,y):
    info=font_style.render("Lvl2: Kill them all",True,(RED))
    screen.blit(info,(x,y))
def info_2(x,y):
    info=myFont.render("PRESS ENTER",True,(RED))
    screen.blit(info,(x,y))
def info_3(x,y):
    info=myFont.render("HINT:use SPACEBAR to shoot",True,(YELLOW))
    screen.blit(info,(x,y))
def info_4(x,y):
    info=info_font.render("#Stay Home",True,(YELLOW))
    screen.blit(info,(x,y))
def info_5(x,y):
    info=info_font.render("#Stay Safe",True,(YELLOW))
    screen.blit(info,(x,y))

def info_6(x,y):
    info=font_style.render("Congratulations!!!!",True,(YELLOW))
    screen.blit(info,(x,y))
def info_7(x,y):
    info=myFont.render("PRESS ENTER",True,(RED))
    screen.blit(info,(x,y))

def info_8(x,y):
    info=myFont.render("You unlocked next level",True,(RED))
    screen.blit(info,(x,y))
def info_9(x,y):
    info=myFont.render("Press Esc to quit",True,(WHITE))
    screen.blit(info,(x,y))
def info_10(x,y):
    info=font_style.render("YOU WON",True,(WHITE))
    screen.blit(info,(x,y))
def info_11(x,y):
    info=com.render("*score 500 to win the game",True,(WHITE))
    screen.blit(info,(x,y))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (BLUE))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_pill(x, y):
    global pill_state
    pill_state = "fire"
    screen.blit(pillImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, pillX, pillY):
    distance = math.sqrt(math.pow(enemyX - pillX, 2) + (math.pow(enemyY - pillY, 2)))
    if distance < 27:
        return True
    else:
        return False

#game_2 loop
congrat=True
while congrat:
    screen.blit(bg_3,(0,0))
    info_8(250,400)
    info_6(200,200)
    info_7(300,300)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                congrat=False
                break
note=True
while note:
    screen.blit(bg_4,(0,0))
    info_1(120,160)
    info_2(300,350)
    info_3(50,500)
    info_11(50,550)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                note=False
                break

running = True
quit=False
win=False
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_5, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if pill_state is "ready":
                    pillSound = mixer.Sound("pill.wav")
                    pillSound.play()
                    pillX = playerX
                    fire_pill(pillX, pillY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            quit=True
            while quit:
                screen.blit(bg_1,(0,0))
                info_4(300,400)
                info_5(400,400)
                game_over_text()
                info_9(250,350)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                            quit=False
                            running=False
                            pygame.quit()
                            quit()


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]


        collision = isCollision(enemyX[i], enemyY[i], pillX, pillY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            pillY = 480
            pill_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if pillY <= 0:
        pillY = 480
        pill_state = "ready"

    if pill_state is "fire":
        fire_pill(pillX, pillY)
        pillY -= pillY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
    if score_value>=500:
        win=True
        while win:
            screen.blit(bg_7,(0,0))
            info_4(300,400)
            info_5(400,400)
            info_10(250,300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    win=False
                    running=False
pygame.quit()
quit()
