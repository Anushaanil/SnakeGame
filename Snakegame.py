import pygame
import colors
from random import randint
window_width = 640
window_height = 700
Window_Dimension = window_width, window_height
segment_size =20
key_map = {
        273: "Up",
        274: "Down",
        275: "Right",
        276: "Left"
    }
pygame.init()
pygame.display.set_caption("SNAKE GAME")
screen = pygame.display.set_mode(Window_Dimension)
clock = pygame.time.Clock()

def draw_objects(snake_positions,food_position):
    pygame.draw.rect(screen,colors.Food,[food_position,(segment_size,segment_size)])

    for x,y in snake_positions:
        pygame.draw.rect(screen,colors.Snake,[x,y,segment_size,segment_size])

def set_food_position(snake_positions):
    while True:
        x_position = randint(0,39) * segment_size
        y_position = randint(2, 41) * segment_size
        food_position = (x_position,y_position)
        if food_position not in snake_positions:
            return food_position

def move_snake(snake_positions,direction):
    x_head_pos, y_head_pos = snake_positions[0]
    if direction == 'Left':
        new_head_pos = (x_head_pos - segment_size,y_head_pos)
    elif direction == 'Right':
        new_head_pos = (x_head_pos + segment_size,y_head_pos)
    elif direction == 'Up':
        new_head_pos = (x_head_pos, y_head_pos - segment_size)
    elif direction == 'Down':
        new_head_pos = (x_head_pos, y_head_pos + segment_size)
    snake_positions.insert(0, new_head_pos)
    del snake_positions[-1]

def on_key_press(event,current_direction):
    key = event.__dict__["key"]
    new_direction = key_map[key]

    all_directions = ("Up","Down","Left","Right")
    opposites = ({"Up","Down"},{"Left","Right"})

    if new_direction in all_directions and {new_direction, current_direction} not in opposites:
        return new_direction
    return  current_direction

def check_collision(snake_positions):
    x_head_pos, y_head_pos = snake_positions[0]
    return(x_head_pos in (-20,window_width) or
         y_head_pos in (20, window_height) or
         (x_head_pos,y_head_pos) in snake_positions[1:])

def check_food_collision(snake_positions, food_position):
    if snake_positions[0] == food_position:
        snake_positions.append(snake_positions[-1])
        return True

def playgame():
    score = 0
    current_direction = "Right"
    snake_positions=[(100,100),(80,100),(60,100)]
    food_position = set_food_position(snake_positions)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event,current_direction)
        screen.fill(colors.Background)
        draw_objects(snake_positions,food_position)

        font = pygame.font.Font(None,28)
        text = font.render(f"Score: {score}",True,colors.Text)
        screen.blit(text,(10,10))

        pygame.display.update()
        move_snake(snake_positions,current_direction)
        if check_collision(snake_positions):
            return
        if check_food_collision(snake_positions, food_position):
            food_position = set_food_position(snake_positions)
            score += 1
        clock.tick(10)
playgame()
