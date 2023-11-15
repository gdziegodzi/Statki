import pygame
from pygame import mixer
import Pygame_Util as pu

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

background_colour = (200, 232, 232)
fontcolor = (19, 38, 87)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
screen.fill(background_colour) 

#volume sliders
slidersWidth = 600
slidersHeight = 40
volumeMusic = 0.20
volumeMusicSlider = pu.slider((255,125,0),(SCREEN_WIDTH - slidersWidth) / 2,SCREEN_HEIGHT - 300,slidersWidth,slidersHeight,volumeMusic,0,1)
volumeEffects = 0.20
volumeEffectsSlider = pu.slider((255,125,0),(SCREEN_WIDTH - slidersWidth) / 2,SCREEN_HEIGHT - 200,slidersWidth,slidersHeight,volumeEffects,0,1)

# Dźwiek gry
pygame.mixer.init()
mixer.music.load('background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(volumeMusic)

# Przycisiki

    # Zawartość tekstowa przycisków 
menu_buttons = [
    {"text": "Wzów grę", "function": "game"},
    {"text": "Wróć do Menu", "function": "main_menu"},
    {"text": "Tablica Wyników", "function": "scoreboard"},
    {"text": "Opuść grę", "function": "quit_game"}
]
    # atrybuty przycisków
button_color = (38, 38, 37)
button_text_color = (255, 255, 255)
button_font = "Comics Sans"
buttons_width = 300
buttons_height = 100
buttons_font_size = 40
buttons_x = (SCREEN_WIDTH-buttons_width)/2
buttons_y = (SCREEN_HEIGHT - 370)
buttons_spacing =buttons_height + 30



def Draw_Settings():
    settings_title_font = pygame.font.SysFont("Comics Sans", 130)
    text = settings_title_font.render("Ustawienia", False, fontcolor)
    screen.blit(text, ((SCREEN_WIDTH-text.get_width())/2,50))
    
    #sliders text
    deafoult_text_font = pygame.font.SysFont("Comics Sans", 50)
    text = deafoult_text_font.render("Głośność muzyki: " + f"{volumeMusic:.2f}" , False, fontcolor)
    screen.blit(text, ((SCREEN_WIDTH-text.get_width())/2,SCREEN_HEIGHT - 350))


    text = deafoult_text_font.render("Głośność efektów: "+ f"{volumeEffects:.2f}" , False, fontcolor)
    screen.blit(text, ((SCREEN_WIDTH-text.get_width())/2,SCREEN_HEIGHT - 250))

    #buttons drawing
    a = 0
    for i in menu_buttons:
        a +=1
        but = pu.button(button_color,buttons_x,buttons_y - (a*buttons_spacing),buttons_width,buttons_height,
        i["text"], (255, 255, 255), button_font, buttons_font_size)
        but.draw(screen)

    #draw sliders
    volumeMusicSlider.draw(screen)
    volumeEffectsSlider.draw(screen)
    pygame.display.flip()




clock = pygame.time.Clock()
running = True


while running:
    screen.fill(background_colour) 
    Draw_Settings()
    # mouse = pygame.mouse.get_pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    if pygame.mouse.get_pressed()[0] and volumeMusicSlider.conteiner_rect.collidepoint(pygame.mouse.get_pos()):
            volumeMusicSlider.move_slider(screen,pygame.mouse.get_pos())
            volumeMusicSlider.draw(screen)
            volumeMusic = volumeMusicSlider.get_value()
            mixer.music.set_volume(volumeMusic)
    if pygame.mouse.get_pressed()[0] and volumeEffectsSlider.conteiner_rect.collidepoint(pygame.mouse.get_pos()):
            volumeEffectsSlider.move_slider(screen,pygame.mouse.get_pos())
            volumeEffectsSlider.draw(screen)
            volumeEffects = volumeEffectsSlider.get_value()
    pygame.display.update()
pygame.quit()