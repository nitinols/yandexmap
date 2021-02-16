import pygame
import requests
import sys

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
while True:
    try:
        w, h, m = map(float, input().split())
        break
    except ValueError:
        print('Не правильно введены данные')
        continue


screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)




while True:
    clock.tick(FPS)

    map_request = f"http://static-maps.yandex.ru/1.x/?ll={w},{h}&spn={m},{m}&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    # write map
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if -90 <= h <= 90:
            h += 0.25
    elif keys[pygame.K_DOWN]:
        if -90 <= h <= 90:
            h -= 0.25
    if keys[pygame.K_LEFT]:
        if -180 <= w <= 180:
            w -= 0.5
    elif keys[pygame.K_RIGHT]:
        if -180 <= w <= 180:
            w += 0.5
    if keys[pygame.K_MINUS]:
        if 0.5 <= m:
            m -= 1
    elif keys[pygame.K_EQUALS]:
        if m <= 8:
            m += 1

    screen.fill(BLACK)
    screen.blit(pygame.transform.scale(pygame.image.load(map_file), (720, 480)), (0, 0))
    pygame.display.update()
