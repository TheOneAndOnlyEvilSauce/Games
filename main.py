import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == UP and self.direction != DOWN:
            self.direction = new_direction
        elif new_direction == DOWN and self.direction != UP:
            self.direction = new_direction
        elif new_direction == LEFT and self.direction != RIGHT:
            self.direction = new_direction
        elif new_direction == RIGHT and self.direction != LEFT:
            self.direction = new_direction

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        return False

    def check_boundary(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        return False

    def grow_snake(self):
        self.grow = True

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def respawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the snake and food
snake = Snake()
food = Food()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()

    if snake.body[0] == food.position:
        snake.grow_snake()
        food.respawn()

    if snake.check_collision() or snake.check_boundary():
        running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the food
    pygame.draw.rect(screen, WHITE, (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)

pygame.quit()
sys.exit()
