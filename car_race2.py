
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2 Player Car Race - AI Opponent")
clock = pygame.time.Clock()
p1 = pygame.Rect(300, 500, 40, 70)
ai = pygame.Rect(500, 500, 40, 70)
obstacles = []
for i in range(8):
    obstacles.append(
        pygame.Rect(
            random.randint(220, 540),
            random.randint(-1000, 0),
            40,
            60
        )
    )

lap1 = 0
lap_ai = 0
player_speed = 5
ai_speed = 4
game = True
winner = ""
def ai_control():
    ai.y -= ai_speed
    danger = None
    closest_distance = 9999

    for obstacle in obstacles:
        if obstacle.bottom > ai.top - 180 and obstacle.top < ai.bottom:

            if abs(obstacle.centerx - ai.centerx) < 70:

                distance = abs(obstacle.centery - ai.centery)

                if distance < closest_distance:
                    closest_distance = distance
                    danger = obstacle

    if danger is not None:

        if ai.centerx < danger.centerx:
            ai.x -= 5
        else:
            ai.x += 5

    ai.x = max(210, min(550, ai.x))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1.x -= player_speed
    if keys[pygame.K_d]:
        p1.x += player_speed
    if keys[pygame.K_w]:
        p1.y -= player_speed
    if keys[pygame.K_s]:
        p1.y += player_speed
    p1.x = max(210, min(550, p1.x))
    p1.y = max(0, min(530, p1.y))
    ai_control()
    if p1.y <= 20:
        lap1 += 1
        p1.y = 500
    if ai.y <= 20:
        lap_ai += 1
        ai.y = 500
    screen.fill((30, 130, 40))
    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (180, 0, 440, 600)
    )

    pygame.draw.line(
        screen,
        "white",
        (180, 0),
        (180, 600),
        5
    )

    pygame.draw.line(
        screen,
        "white",
        (620, 0),
        (620, 600),
        5
    )

    for y in range(0, 600, 60):
        pygame.draw.rect(
            screen,
            "white",
            (395, y, 10, 30)
        )

    pygame.draw.rect(
        screen,
        "white",
        (180, 0, 440, 20)
    )
    for obstacle in obstacles:

        obstacle.y += 4

        if obstacle.y > 600:
            obstacle.y = random.randint(-500, -50)
            obstacle.x = random.randint(210, 550)

        pygame.draw.rect(
            screen,
            "yellow",
            obstacle
        )
        if p1.colliderect(obstacle):
            p1.y += 20

        # AI collision
        if ai.colliderect(obstacle):
            ai.y += 20

    pygame.draw.rect(
        screen,
        "blue",
        p1
    )

    pygame.draw.rect(
        screen,
        "red",
        ai
    )

    font = pygame.font.SysFont(None, 30)

    text1 = font.render(
        "PLAYER 1: " + str(lap1) + "/5",
        True,
        "white"
    )

    text_ai = font.render(
        "AI: " + str(lap_ai) + "/5",
        True,
        "white"
    )
    screen.blit(text1, (20, 20))
    screen.blit(text_ai, (700, 20))

    control_text = font.render(
        "P1: W A S D",
        True,
        "white"
    )

    screen.blit(
        control_text,
        (20, 550)
    )

    if lap1 >= 5:
        winner = "PLAYER 1 WINS!"

    elif lap_ai >= 5:
        winner = "AI WINS!"

    if winner != "":
        win_font = pygame.font.SysFont(None, 55)

        win_text = win_font.render(
            winner,
            True,
            "yellow"
        )

        screen.blit(
            win_text,
            (280, 280)
        )

        pygame.display.update()
        pygame.time.wait(2500)

        game = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
