import pygame
import sys
import random

pygame.init()

# 畫面與格子設定
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Menu")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# 顏色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GRAY  = (100, 100, 200)

# 遊戲狀態
game_state = "menu"
difficulty = "Easy"
FPS = 10

# 按鈕繪製函式
def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, GRAY, rect)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x + 15, y + 10))
    return rect

# 隨機產生食物
def random_food():
    return [
        random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    ]

# 初始化蛇與食物
def reset_game():
    global snake, direction, food
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = [BLOCK_SIZE, 0]
    food = random_food()

reset_game()

# 主迴圈
while True:
    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_state = "menu"

    # 主選單
    if game_state == "menu":
        title = font.render("Menu", True, (255, 255, 255))
        screen.blit(title, (250, 50))

        b1 = draw_button("Start", 200, 120, 200, 50)
        b2 = draw_button("Difficulty", 200, 190, 200, 50)
        b3 = draw_button("Setting",     200, 260, 200, 50)

        if b1.collidepoint(mouse_pos) and click:
            reset_game()
            FPS = 10 if difficulty == "Easy" else 20
            game_state = "play"
        elif b2.collidepoint(mouse_pos) and click:
            game_state = "difficulty"
        elif b3.collidepoint(mouse_pos) and click:
            game_state = "settings"

    # 遊戲畫面
    elif game_state == "play":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != [0, BLOCK_SIZE]:
            direction = [0, -BLOCK_SIZE]
        elif keys[pygame.K_DOWN] and direction != [0, -BLOCK_SIZE]:
            direction = [0, BLOCK_SIZE]
        elif keys[pygame.K_LEFT] and direction != [BLOCK_SIZE, 0]:
            direction = [-BLOCK_SIZE, 0]
        elif keys[pygame.K_RIGHT] and direction != [-BLOCK_SIZE, 0]:
            direction = [BLOCK_SIZE, 0]

        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        # 撞牆或自己
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake):
            game_state = "menu"
            continue

        snake.insert(0, new_head)
        if new_head == food:
            food = random_food()
        else:
            snake.pop()

        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # 難度選單
    elif game_state == "difficulty":
        title = font.render("Difficulty ", True, (255, 255, 255))
        screen.blit(title, (230, 50))

        easy_btn = draw_button("Easy", 200, 150, 200, 50)
        hard_btn = draw_button("Hard", 200, 220, 200, 50)

        if easy_btn.collidepoint(mouse_pos) and click:
            difficulty = "Easy"
            game_state = "menu"
        elif hard_btn.collidepoint(mouse_pos) and click:
            difficulty = "Hard"
            game_state = "menu"

    # 設定畫面
    elif game_state == "settings":
        title = font.render("設定畫面（尚未實作）", True, (255, 255, 255))
        screen.blit(title, (150, 180))

    pygame.display.flip()
    clock.tick(FPS)
