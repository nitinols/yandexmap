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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if w > -180 + m:
                    w -= 0.1
            elif event.key == pygame.K_RIGHT:
                if w < 180 - m:
                    w += 0.1
            elif event.key == pygame.K_UP:
                if h < 90 - m:
                    h += 0.1
            elif event.key == pygame.K_DOWN:
                if h > -90 + m:
                    h -= 0.1

    screen.fill(BLACK)
    screen.blit(pygame.transform.scale(pygame.image.load(map_file), (720, 480)), (0, 0))
    pygame.display.update()