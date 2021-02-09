import os
import sys

import pygame
import requests



coordsx = float(input())
coordsy = float(input())
mashtab = 0.2
map_request = f"http://static-maps.yandex.ru/1.x/?ll={coordsx},{coordsy}&spn={mashtab},{mashtab}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
while pygame.event.wait().type != pygame.QUIT:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and mashtab < 70:
                mashtab *= 2
            elif event.key == pygame.K_DOWN and mashtab > 0.00001:
                mashtab /= 2
        elif event.type == pygame.QUIT:
            pygame.quit()
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coordsx},{coordsy}&spn={mashtab},{mashtab}&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)