# initial configurations
import pygame as pg
import random

pg.init()
pg.display.set_caption('Snake Game')
WIDTH, HEIGHT = 1200, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
CLOCK = pg.time.Clock()

# cores
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Snake parameters
SQUARE_SIZE = 20
VELOCITY = 10

def generate_food():
  food_x = round(random.randrange(0, WIDTH - SQUARE_SIZE) / 20.0) * 20.0
  food_y = round(random.randrange(0, HEIGHT - SQUARE_SIZE) / 20.0) * 20.0
  return food_x, food_y

def draw_food(food_x: int, food_y: int) -> None:
  pg.draw.rect(screen, GREEN, [food_x, food_y, SQUARE_SIZE, SQUARE_SIZE])
  
def draw_snake(pixels):
  for pixel in pixels:
    pg.draw.rect(screen, WHITE, [pixel[0], pixel[1], SQUARE_SIZE, SQUARE_SIZE])
    
def draw_score(score):
  font = pg.font.SysFont("Helvetica", 35)
  text = font.render(f"Pontos: {score}", True, RED)
  screen.blit(text, [10, 10])

def select_velocity(key, x, y, last_key):
  x_vel, y_vel = x, y
  if key == pg.K_ESCAPE:
    pg.quit()
    quit()
  if (key == pg.K_s or key == pg.K_DOWN) and last_key != 119 and last_key != pg.K_UP: #S
    y_vel = SQUARE_SIZE
    x_vel = 0
    last_key = key
  elif (key == pg.K_w or key == pg.K_UP) and last_key != 115 and last_key != pg.K_DOWN: #W
    y_vel = -SQUARE_SIZE
    x_vel = 0
    last_key = key
  elif (key == pg.K_d or key == pg.K_RIGHT) and last_key != pg.K_a and key != pg.K_LEFT: #D
    x_vel = SQUARE_SIZE
    y_vel = 0
    last_key = key
  elif (key == pg.K_a or key == pg.K_LEFT) and last_key != pg.K_d and key != pg.K_RIGHT: #A
    x_vel = -SQUARE_SIZE
    y_vel = 0
    last_key = key
  return x_vel, y_vel, last_key

def game():
  end_game = False
  x = WIDTH / 2
  y = HEIGHT / 2
  
  snake_size = 1
  pixels = []
  
  x_velocity = 0
  y_velocity = 0
  last_key = 0
  
  food_x, food_y = generate_food()

  while not end_game:
    screen.fill(BLACK)
    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        end_game = True
      elif event.type == pg.KEYDOWN:
        x_velocity, y_velocity, last_key = select_velocity(event.key, x_velocity, y_velocity, last_key)

    draw_food(food_x, food_y)

    x += x_velocity
    y += y_velocity
    # draw snake
    pixels.append([x, y])
    if len(pixels) > snake_size:
      del pixels[0]
    draw_snake(pixels)

    for pixel in pixels[:-1]:
      if pixel == [x, y]:
        end_game = True
    draw_score(snake_size - 1)

    pg.display.update()

    if x == food_x and y == food_y:
      snake_size += 1
      food_x, food_y = generate_food()
    
    if x <= 0 or x >= WIDTH or y <= 0 or y >= HEIGHT:
      end_game = True
    CLOCK.tick(VELOCITY)

game()
