import pygame
import time



#ini_set
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("bouncy_ball_simulator")
red = (255, 0, 0)

#costume attrbute
velocity = 0
ball_y = 300
ball_x = 300
mass = 5
ce=0.9
vx=10
force = 10
acc=10/mass

mass = float(input("Please enter the mass of the ball (kg): "))
ce = float(input("Please enter the coefficient of restitution (between 0 and 1): "))
gravity = float(input("Please enter the gravitational acceleration (default 9.8): "))
vx = float(input("Please enter the initial horizontal velocity (px/s): "))

last_time = time.perf_counter()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 计算时间差
    current_time = time.perf_counter()
    dt = current_time - last_time
    last_time = current_time

    screen.fill((255,255,255))
    acceleration = 10/mass

    dt = min(dt, 0.05)
    velocity += acc * dt
    ball_y += velocity * dt
    ball_x += vx * dt

    if ball_y >= 600 - 20:
        ball_y = 600 - 20  # 防止穿透地面
        velocity = -velocity * ce

        if abs(velocity) < 1:
            velocity = 0
    if ball_x <= 20 or ball_x >= 800 - 20:
        ball_x = max(20, min(ball_x, 800 - 20))
        vx = -vx * ce



    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), 20)
    pygame.display.flip()