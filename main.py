import pygame
import random

WIDTH, HEIGHT = 480, 640
BIRDX, BIRDY = 0, 0
TOWERX, TOWERY = WIDTH, 0
TOWER_HEIGHT = random.randint(100, 300)
SCORE = 0


def printText(string, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    pygame.display.update()


def display_tower(r):
    pygame.draw.rect(screen, (0, 255, 0), (TOWERX, TOWERY, 50, r))
    pygame.draw.rect(screen, (0, 255, 0), (TOWERX, r+130, 50, 412-r))


def crash_detection():
    if TOWERX <= BIRDX+64 <= TOWERX+50 and (BIRDY < TOWER_HEIGHT or BIRDY > TOWER_HEIGHT+88):
        return True
    else:
        return False


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('images/bg.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird by Polex')
clock = pygame.time.Clock()
vel = 1


bird = pygame.image.load('images/bird.png')
bird = pygame.transform.scale(bird, (64, 42))
screen.blit(bird, (BIRDX, BIRDY))
screen.blit(bg, (0, 0))
run = False

printText('OPALI SPACE', WIDTH//2, HEIGHT//3, 64)
printText('DA KRENES', WIDTH//2, HEIGHT//3+64, 64)
waitingToStart = True
while waitingToStart:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        run = True
        waitingToStart = False


while run:

    screen.blit(bg, (0, 0))
    display_tower(TOWER_HEIGHT)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(40):
                    BIRDY -= 2

    BIRDY += 2
    pygame.time.delay(3)
    screen.blit(bird, (BIRDX, BIRDY))
    TOWERX -= 2
    display_tower(TOWER_HEIGHT)
    # pygame.display.flip()

    crash = crash_detection()
    if crash:
        run = False

    if BIRDY == screen.get_height()-145:
        BIRDY += 1

    if TOWERX == -50:
        TOWER_HEIGHT = random.randint(150, 250)
        TOWERX = WIDTH
        SCORE += 1
    SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)
    sc = SCORE_FONT.render(f'Rezultat: {SCORE}', True, (255, 255, 255))
    screct = sc.get_rect()
    screct.center = (240, 610)
    screen.blit(sc, screct)
    pygame.display.update()


printText('PUKO SI', screen.get_width()//2, screen.get_height()//2-20, 100)
while 1:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                run = True
