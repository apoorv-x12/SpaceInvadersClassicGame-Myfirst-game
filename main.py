import math
import random

import pygame
from pygame import mixer

# Initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('gameBackground.png')

# Sound
# mixer.music.load("background.wav")
# mixer.music.play(-1)

# change title to SThe LOST WORLD PART 1
pygame.display.set_caption("The LOST WORLD PART 1")
# load icon and set game logo to this icon
icon = pygame.image.load("icon2.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullets.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("LOST WORLD begins..", True, (255, 255, 255))
    screen.blit(over_text, (50, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # bulletSound = mixer.Sound("laser.wav")
                    # bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # explosionSound = mixer.Sound("explosion.wav")
            # explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
'''
# 0-> import
import pygame
# 16-> for enemy movement we need random integer import random
import random

# 1-> initialize pygame module
pygame.init()
# 2-> setting up screen
screen = pygame.display.set_mode((800, 600))
# 22-> game background
background = pygame.image.load('gameBackground.png')
# 6-> change title to SThe LOST WORLD PART 1
pygame.display.set_caption("The LOST WORLD PART 1")
# 7-> load icon and set game logo to this icon
icon = pygame.image.load("icon2.png")
pygame.display.set_icon(icon)

# 10-> defining player
playerImage = pygame.image.load("Player.png")
playerX = 368
playerY = 480
playerXChange = 0

# 17-> define enemy
enemyImage = pygame.image.load("Enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyXChange = 3  # this can't be zero initially
enemyYChange = 40  # this is constant

# 24-> define bullet
bulletImage = pygame.image.load("bullets.png")
bulletX = 0  # this will be assigned playerX in while loop's for loop on line 56
bulletY = 480
bulletXChange = 0
bulletYChange = 5
bullet_state = "ready"


# "ready" state mean user can't see bullet on screen and  "fire" state mean bullet is moving on screen


# 11-> define player function
def player(x, y):
    # screen.blit function shifts playerImage to x,y pixel
    screen.blit(playerImage, (x, y))


# 18-> define enemy function just like player function
def enemy(x, y):
    screen.blit(enemyImage, (x, y))


# 25-> define bullet function
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


# 3-> create a while loop for game looping
running = True
while running:
    # 8-> setting screen colour
    screen.fill((45, 40, 90))
    # 23-> set game background
    screen.blit(background, (0, 0))

    # 4-> loop over events
    for event in pygame.event.get():
        # 5-> if close is clicked (quit event occurs close window or running=False)
        if event.type == pygame.QUIT:
            running = False
        # 13 A-> change playerXChange value based on left and right keys pressed
        if event.type == pygame.KEYDOWN:
            # if any key is pressed we get inside this if statement
            if event.key == pygame.K_LEFT:
                # if left arrow key was pressed we do this
                playerXChange = -4
            if event.key == pygame.K_RIGHT:
                # if right arrow key was pressed we do this
                playerXChange = 4
            # 26->add what to do when space is pressed
            if event.key == pygame.K_SPACE:
                # if space was pressed we do this
                # 29-> we have to below only when state is ready
                if bullet_state == "ready":
                    # basically to restrict user from pressing space while bullet is already moving
                    # 28-> we save initial playerX in bulletX as playerX will change
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        # 13 B-> we change playerXChange to 0 when arrow keys are released
        if event.type == pygame.KEYUP:
            # if any key is released we get inside this if statement
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # if right arrow or left arrow key was released we do this
                playerXChange = 0

    # 14-> then add playerXChange to playerX
    playerX += playerXChange

    # 15->make sure before calling player function with playerX , player or spaceship is within game window 800*600
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # 21-> change enemy coordinates
    enemyX += enemyXChange

    # 20->  enemy movement __  set boundaries of enemy movement
    if enemyX <= 0:
        enemyXChange = 3
        enemyY += enemyYChange
    elif enemyX >= 736:
        enemyXChange = -3
        enemyY += enemyYChange
    # 27-> bullet movement __ set boundaries of bullet movement
    if bulletY <= 0:  # this if was added after below one
        bullet_state = "ready"
        bulletY = 480
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletYChange
    # 19-> call enemy method
    enemy(enemyX, enemyY)
    # 12-> call player function with playerX and playerY
    player(playerX, playerY)
    # 9-> updating screen for display of above code's changes on each iteration
    pygame.display.update()
'''
