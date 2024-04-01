import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("스키 게임")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 플레이어 설정
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10
player_speed = 10  # 플레이어 이동속도

# 코인 설정
coin_width, coin_height = 20, 20
coin_x, coin_y = random.randint(0, WIDTH - coin_width), 0
coin_speed = 5

# 장애물 설정
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 7
obstacles = []  # 장애물 리스트

# 점수 초기화
score = 0
obstacle_spawn_rate = 30  # 장애물 생성 빈도

# 게임 루프
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # 코인 이동
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_x, coin_y = random.randint(0, WIDTH - coin_width), 0

    # 장애물 이동
    for obstacle in obstacles:
        obstacle['y'] += obstacle_speed + score // 10  # 점수에 따라 장애물 속도 증가
        if obstacle['y'] > HEIGHT:
            obstacles.remove(obstacle)

    # 새로운 장애물 생성
    if random.randint(1, obstacle_spawn_rate) == 1:
        obstacles.append({'x': random.randint(0, WIDTH - obstacle_width), 'y': 0})

    # 충돌 검사
    for obstacle in obstacles:
        if player_x < obstacle['x'] + obstacle_width and player_x + player_width > obstacle['x'] and \
                player_y < obstacle['y'] + obstacle_height and player_y + player_height > obstacle['y']:
            running = False

    # 코인과 충돌 검사
    if player_x < coin_x + coin_width and player_x + player_width > coin_x and \
            player_y < coin_y + coin_height and player_y + player_height > coin_y:
        coin_x, coin_y = random.randint(0, WIDTH - coin_width), 0
        score += 1
        obstacle_spawn_rate -= 1  # 장애물 생성 빈도 감소

    # 화면 업데이트
    win.fill(WHITE)

    # 스코어 보드 업데이트
    text = font.render("Score: " + str(score), True, BLACK)
    win.blit(text, (10, 10))

    # 게임 오브젝트 그리기
    pygame.draw.rect(win, BLACK, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, YELLOW, (coin_x, coin_y, coin_width, coin_height))
    for obstacle in obstacles:
        pygame.draw.rect(win, RED, (obstacle['x'], obstacle['y'], obstacle_width, obstacle_height))

    pygame.display.update()

pygame.quit()
