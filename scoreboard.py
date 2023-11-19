import sys
import pygame
from Pygame_Util import button
from pygame import mixer, init

pygame.init()
pygame.display.set_caption('Tablica Wyników')

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BACKGROUND_COLOR = (200, 232, 232)
text_color = (19, 38, 87)


# do tytułu
font = pygame.font.SysFont("arial",80, bold=True)
title_text = "Tablica Wyników"
title_text_width = font.size(title_text)[0]
title_text_x = (SCREEN_WIDTH - title_text_width) // 2

#do wyjasnien
fonts = pygame.font.SysFont("arial", 40, bold=True)

# Przycisk wyjścia
exit_button_width = 150
exit_button_height = 50
exit_button_x = SCREEN_WIDTH - exit_button_width - 10
exit_button_y = 10
exit_button_rect = pygame.Rect((exit_button_x, exit_button_y, exit_button_width, exit_button_height))
exit_button_color = (255, 0, 0)
exit_button_hover_color = (200, 0, 0)
exit_button_font_size = 30
exit_button_font = pygame.font.SysFont("monospace", exit_button_font_size, bold=True)
exit_button_text = exit_button_font.render("Wyjście", 1, (255, 255, 255))



SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))



# Rysowanie tytułu
def draw_text(text,font,text_color,x,y):
    img = font.render(text,True,text_color)
    SCREEN.blit(img,(x,y))

# Wczytywanie wyników z pliku
def load_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Nie można odnaleźć pliku: {file_path}")
        sys.exit()

# Wczytywanie inicjalizacja
file_path = "nicks.txt"
file_content = load_file_content(file_path)

fileW_path = "winrate.txt"
fileW_content = load_file_content(fileW_path)

fileG_path = "games.txt"
fileG_content = load_file_content(fileG_path)

fileS_path = "score.txt"
fileS_content = load_file_content(fileS_path)

lines_nicks = file_content.split('\n')
lines_winrate = fileW_content.split('\n')
lines_games = fileG_content.split('\n')
lines_score = fileS_content.split('\n')

# Uruchomienie gry
run = True
while run:
    SCREEN.fill(BACKGROUND_COLOR)

# rysowanie tytułu
    draw_text(title_text,font,text_color,title_text_x,50)

# rysowanie przycisku wyjścia
    pygame.draw.rect(SCREEN, exit_button_color, exit_button_rect)
    SCREEN.blit(exit_button_text, (exit_button_x + (exit_button_width / 2 - exit_button_text.get_width() / 2),
                                   exit_button_y + (exit_button_height / 2 - exit_button_text.get_height() / 2)))

# rysowanie "wyjasnien"
    draw_text("Nazwa",fonts, text_color,150, 250)
    draw_text("% Zwycięstw", fonts, text_color, 350, 250)
    draw_text("Rozegrane gry", fonts, text_color, 650, 250)
    draw_text("Całkowity wynik", fonts, text_color, 950, 250)

# rysowanie zawartości plików
    for i, line in enumerate(lines_nicks):
        draw_text(line, fonts, text_color, 150, 300 + i * 2 * 40)

    for i, line in enumerate(lines_winrate):
        draw_text(line, fonts, text_color, 350, 300 + i * 2 * 40)

    for i, line in enumerate(lines_games):
        draw_text(line, fonts, text_color, 650, 300 + i * 2 * 40)

    for i, line in enumerate(lines_score):
        draw_text(line, fonts, text_color, 950, 300 + i * 2 * 40)



# obsluga zdarzen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    pygame.display.flip()
pygame.quit()