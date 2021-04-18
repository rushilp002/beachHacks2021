# This is the main file
import pygame
import os
import sprites
import LinkedList
import random

# Screen Variables
WIDTH, HEIGHT = 900, 500
FPS = 60
<<<<<<< HEAD
BACKGROUND_SPEED = 3
PLAYER_SPEED = 5
=======
SPEED = 5
>>>>>>> parent of b0414fa (added health hi)
SHARK_WIDTH, SHARK_HEIGHT = 100, 100
BOTTLE_WIDTH, BOTTLE_HEIGHT = 10, 10
COLLISION = pygame.USEREVENT + 1
SCREEN_COLOR = (150, 150, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

SHARK_IMAGE = pygame.image.load(os.path.join('assets', 'shark.png'))
BOTTLE_IMAGE = pygame.image.load(os.path.join('assets', 'water_bottle.png'))
OCEAN_IMAGE = pygame.image.load(os.path.join('assets', 'ocean.png'))

<<<<<<< HEAD
SHARK = pygame.transform.scale(SHARK_IMAGE, (100, 100))
BOTTLES = [BOTTLE_IMAGE, pygame.transform.rotate(BOTTLE_IMAGE, 90), pygame.transform.rotate(BOTTLE_IMAGE, 180), pygame.transform.rotate(BOTTLE_IMAGE, 270)]
OCEAN = [0, 900 , 1800]

def draw_window(list : LinkedList.LinkedList()):
    # WIN.blit(OCEAN_IMAGE, (0, 0))
    for i in range(3):
        WIN.blit(OCEAN_IMAGE, (OCEAN[i], 0))
=======

# 1 = Up, 2 = Right, 3 = Down, 4 = Left
SHARK = pygame.transform.scale(SHARK_IMAGE, (100, 100))
BOTTLES = [BOTTLE_IMAGE, pygame.transform.rotate(BOTTLE_IMAGE, 90), pygame.transform.rotate(BOTTLE_IMAGE, 180), pygame.transform.rotate(BOTTLE_IMAGE, 270)]

def draw_window(list : LinkedList.LinkedList()):
    WIN.blit(OCEAN_IMAGE, (0, 0))
>>>>>>> parent of b0414fa (added health hi)

    curr = list.head

    while curr:
        WIN.blit(curr.data.image, (curr.data.get_x(), curr.data.get_y()))
        curr = curr.next

    pygame.display.update()

def handle_avatar_movement(sprite: sprites.Sprites, keys_pressed):
    if keys_pressed[pygame.K_UP] and sprite.get_y() > 0:  # UP
        sprite.set_y(-PLAYER_SPEED)

    if keys_pressed[pygame.K_DOWN] and sprite.get_y() + sprite.hitbox.height < HEIGHT:  # DOWN
        sprite.set_y(PLAYER_SPEED)

    if keys_pressed[pygame.K_LEFT] and sprite.get_x() > 0:  # LEFT
        sprite.set_x(-PLAYER_SPEED)
        
    if keys_pressed[pygame.K_RIGHT] and sprite.get_x() + sprite.hitbox.width < WIDTH:  # RIGHT
        sprite.set_x(PLAYER_SPEED)

def collision(shark, list):
    curr = list.head.next

    while curr:
        if shark.hitbox.colliderect(curr.data.hitbox):
            pygame.event.post(pygame.event.Event(COLLISION))
            print("Hit!")

        curr = curr.next

def main():
    run = True
    shark_hp = 10
<<<<<<< HEAD
    time = 0
=======
>>>>>>> parent of b0414fa (added health hi)
    clock = pygame.time.Clock()
    list = LinkedList.LinkedList()

    shark = sprites.Sprites(SHARK, pygame.Rect(10, 300, SHARK_WIDTH, SHARK_HEIGHT))
    trash = sprites.Sprites(BOTTLES[random.randint(0, 3)], pygame.Rect(random.randint(10, 500), random.randint(10, 500), 10, 10))

    for i in range(10):
        list.push(sprites.Sprites(BOTTLES[random.randint(0, 3)], pygame.Rect(random.randint(100, 900), random.randint(10, 600), 10, 10)))

    list.push(trash)
    list.push(shark)
    pygame.display.set_caption("PISTRIS")

    while run:
        clock.tick(FPS)
        time += 1

        for i in range(3):
            OCEAN[i] -= BACKGROUND_SPEED

            if OCEAN[i] == -900:
                OCEAN[i] = 1800

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == COLLISION:
                shark_hp -= 1
        if shark_hp <= 0:
<<<<<<< HEAD
=======
            print("dead!")
>>>>>>> parent of b0414fa (added health hi)
            break
        
        keys_pressed = pygame.key.get_pressed()
        handle_avatar_movement(shark, keys_pressed)
        collision(shark, list)
        draw_window(list)

    pygame.QUIT()


if __name__ == "__main__":
    main()