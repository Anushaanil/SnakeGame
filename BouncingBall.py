import pygame
from collections import namedtuple
from random import randint


Color = namedtuple("Color", ["red","green","blue"])
Background_color = Color(red=153,green=0,blue=76)
#Rectangle_color = Color(red=255,green=255,blue=255)
Round_color = Color(red=255,green=204,blue=253)
clock = pygame.time.Clock()
Ball_radius = 20

pygame.init()
pygame.display.set_caption("Bouncing Ball")
screen = pygame.display.set_mode([640, 480])

# pygame.draw.rect(screen, Rectangle_color, [0, 0, 150, 50])
# pygame.draw.circle(screen, Round_color,[320,240], 40)


def main():
    Ball_pos = [screen.get_width() // 2, screen.get_height() // 2]
    Ball_velocity = [randint(-5,5),randint(-5,5)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #elif event.type == pygame.MOUSEMOTION: round_pos = event.__dict__["pos"]
        screen.fill(Background_color)
        font = pygame.font.Font(None, 28)
        text = font.render("wowwww", True, (0, 0, 0))
        screen.blit(text, (50, 50))
        pygame.draw.circle(screen, Round_color, Ball_pos , Ball_radius)
        pygame.display.update()

        if Ball_pos[0]-Ball_radius <0:
            Ball_velocity[0]=-Ball_velocity[0]
        elif Ball_pos[0]+Ball_radius>screen.get_width():
            Ball_velocity[0]=-Ball_velocity[0]

        if Ball_pos[1]-Ball_radius <0:
            Ball_velocity[1]=-Ball_velocity[1]
        elif Ball_pos[1]+Ball_radius>screen.get_height():
            Ball_velocity[1]=-Ball_velocity[1]

        Ball_pos[0] += Ball_velocity[0]
        Ball_pos[1] += Ball_velocity[1]


        clock.tick(70)
main()