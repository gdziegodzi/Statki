import Pygame_Util as pu
import pygame
from pygame import mixer
import tkinter as tk

from game_screen import SCREEN_WIDTH

pygame.display.set_caption('Statki')
pygame.font.init()
volume = 0.5
pygame.init()
pygame.mixer.init()
mixer.music.load('background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(volume)

def change_volume(new_volume):
    volume = float(new_volume)
    mixer.music.set_volume(volume)


def show_volume_settings():
    root = tk.Tk()
    root.title("Zmiana głośności")
    root.geometry("400x100")

    volume_scale = tk.Scale(root, label="Głośność", from_=0.01, to=1.00, resolution=0.01, orient="horizontal", command=change_volume)
    volume_scale.set(mixer.music.get_volume())  # Ustaw aktualną głośność
    volume_scale.pack()
    root.mainloop()


background_colour = (135,206,235) 
screen = pygame.display.set_mode((1920, 1080)) 
screen.fill(background_colour) 

# Tab declaration
BoardSize = []
Ships = [[],[],[],[]]

# Inicjalizacja przycisku wyjścia
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
exit_sound = pygame.mixer.Sound('button.mp3')

# Add the Settings button
settings_button_width = 160
settings_button_height = 50
settings_button_x = SCREEN_WIDTH - settings_button_width - 200
settings_button_y = 10  # Adjust the vertical position
settings_button_rect = pygame.Rect((settings_button_x, settings_button_y, settings_button_width, settings_button_height))
settings_button_color = (128,128,128)  # Green button color
settings_button_hover_color = (128,128,200)  # Green hover color
settings_button_font_size = 30
settings_button_font = pygame.font.SysFont("monospace", settings_button_font_size, bold=True)
settings_button_text = settings_button_font.render("Settings", 1, (255, 255, 255))



def Custom_page_draw():


    fonth1 = pygame.font.SysFont("arial.ttf", 70)
    fonth2 = pygame.font.SysFont("arial.ttf", 50)
    # fonth3 = pygame.font.SysFont("arial.ttf", 20)
    text = fonth1.render("Rozmiar planszy", False, (0,0,0))
    screen.blit(text, (100,50))

    #Ability overlay
    text = fonth1.render("Special ability", False, (0,0,0))
    screen.blit(text, (1200,300))
    text = fonth2.render("Coming soon", False, (0,0,0))
    screen.blit(text, (1250,400))

    #Board Button overlay 
    for x in range(0,4):
        BoardSize.append((pu.checkbox((110,0,0), 115 + (x*200), 120, 30, 30)))
        BoardSize[x].draw(screen)

    # but_tab.append(BoardSize1)


    #Board Text overlay 
    text = fonth2.render("9x9", False, (0,0,0))
    screen.blit(text, (100,150))
    text = fonth2.render("10x10", False, (0,0,0))
    screen.blit(text, (280,150))
    text = fonth2.render("11x11", False, (0,0,0))
    screen.blit(text, (485,150))
    text = fonth2.render("12x12", False, (0,0,0))
    screen.blit(text, (680,150))

    #Ships Text overlay

    text = fonth1.render("Ships", False, (0,0,0))
    screen.blit(text, (100,250))

    text = fonth2.render("Number of 1 block ship", False, (0,0,0))
    screen.blit(text, (130,320))
    text = fonth2.render("Number of 2 block ship", False, (0,0,0))
    screen.blit(text, (130,470))
    text = fonth2.render("Number of 3 block ship", False, (0,0,0))
    screen.blit(text, (130,620))
    text = fonth2.render("Number of 4 block ship", False, (0,0,0))
    screen.blit(text, (130,770))


    for j in range (0,4):
        for i in range (0,9):
            text = fonth2.render(str(i), False, (0,0,0))
            screen.blit(text, (135+(i*100),410+(j*150)))
    #Ships Button overlay 
            Ships[j].append((pu.checkbox((0,0,0), 130+(i*100), 380+(j*150), 30, 30)))
            Ships[j][i].draw(screen)


    # Update the display using flip 
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
Custom_page_draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Sprawdź przyciski na planszy i statki
            for b in BoardSize:
                if b.isOver(pygame.mouse.get_pos()):
                    for p in BoardSize:
                        if p.isChecked():
                            p.convert(screen)
                    b.convert(screen)
                    pygame.display.flip()
            for s in Ships:
                for z in s:
                    if z.isOver(pygame.mouse.get_pos()):
                        for d in s:
                            if d.isChecked():
                                d.convert(screen)
                        z.convert(screen)
                        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if settings_button_rect.collidepoint(event.pos):
                show_volume_settings()
            elif exit_button_rect.collidepoint(event.pos):
                mixer.music.stop()
                exit_sound.play()
                pygame.time.delay(3000)
                running = False

    # Rysuj przyciski i tekst na ekranie
    pygame.draw.rect(screen, exit_button_color if not exit_button_rect.collidepoint(
        pygame.mouse.get_pos()) else exit_button_hover_color, exit_button_rect)
    pygame.draw.rect(screen, settings_button_color if not settings_button_rect.collidepoint(
        pygame.mouse.get_pos()) else settings_button_hover_color, settings_button_rect)

    # Tekst na przyciskach
    screen.blit(settings_button_text, (settings_button_x + 10, settings_button_y + 10))
    screen.blit(exit_button_text, (exit_button_x + 10, exit_button_y + 10))

    pygame.display.update()

# Zakończenie gry
pygame.quit()
