import Gui.Pygame_Util as pu
import pygame
from pygame import mixer
import tkinter as tk

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()
pygame.font.init()

class page_custom():
    def __init__(self,s,vol1,vol2):
        self.screen = s
        self.volume = 0.05

        self.fontcolor = (19, 38, 87)

        #Volume SLiders

        self.volumeMusic = vol1
        self.volumeEffects = vol2
        self.slidersWidth = 600
        self.slidersHeight = 40
        self.volumeMusicSlider = pu.slider((255,125,0),1100 ,SCREEN_HEIGHT - 300,self.slidersWidth,self.slidersHeight,self.volumeMusic,0,1)
        self.volumeEffectsSlider = pu.slider((255,125,0),1100 ,SCREEN_HEIGHT - 200,self.slidersWidth,self.slidersHeight,self.volumeEffects,0,1)

        #background color
        self.background_colour = (200, 232, 232)

        # Tab declaration
        self.BoardSize = []
        self.Ships = [[],[],[],[]]

        # Inicjalizacja przycisku wyjścia
        self.exit_button_color = (200, 0, 0)
        self.exit_button_hover_color = (150, 0, 0)
        self.exit_button = pu.button(self.exit_button_color,SCREEN_WIDTH - 60,10,50,50,"X",(0,0,0),"monospace",30)

        # menu button
        self.menu_button_color = (128, 128, 128)
        self.menu_button_hover_color = (128, 128, 200)
        self.menu_button = pu.button(self.menu_button_color,SCREEN_WIDTH - 220,10,150,50,"Menu",(0,0,0),"monospace",30)

        #Board tab
        for x in range(0,4):
            self.BoardSize.append((pu.checkbox((110,0,0), 115 + (x*200), 120, 30, 30)))

        #Checkbox tab
        for j in range (0,4):
            for i in range (0,9):
                self.Ships[j].append((pu.checkbox((0,0,0), 130+(i*100), 380+(j*150), 30, 30)))

    def Custom_page_draw(self):

        self.screen.fill(self.background_colour)
        self.fonth1 = pygame.font.SysFont("arial.ttf", 70)
        self.fonth2 = pygame.font.SysFont("arial.ttf", 50)
        # fonth3 = pygame.font.SysFont("arial.ttf", 20)
        text = self.fonth1.render("Rozmiar planszy", False, (0,0,0))
        self.screen.blit(text, (100,50))

        #Ability overlay
        text = self.fonth1.render("Umiejętności specjalne", False, (0,0,0))
        self.screen.blit(text, (1200,100))
        text = self.fonth2.render("Zostaną dodane wkrótce!", False, (0,0,0))
        self.screen.blit(text, (1250,200))

        #sliders text
        deafoult_text_font = pygame.font.SysFont("Comics Sans", 50)
        text = deafoult_text_font.render("Głośność muzyki: " + f"{self.volumeMusic:.2f}" , False, self.fontcolor)
        self.screen.blit(text, (1200,SCREEN_HEIGHT - 350))


        text = deafoult_text_font.render("Głośność efektów: "+ f"{self.volumeEffects:.2f}" , False, self.fontcolor)
        self.screen.blit(text, (1200,SCREEN_HEIGHT - 250))


        #Board Button overlay 
        for x in range(0,4):
            self.BoardSize[x].draw(self.screen)

        #Board Text overlay 
        text = self.fonth2.render("9x9", False, (0,0,0))
        self.screen.blit(text, (100,150))
        text = self.fonth2.render("10x10", False, (0,0,0))
        self.screen.blit(text, (280,150))
        text = self.fonth2.render("11x11", False, (0,0,0))
        self.screen.blit(text, (485,150))
        text = self.fonth2.render("12x12", False, (0,0,0))
        self.screen.blit(text, (680,150))

        #self.Ships Text overlay

        text = self.fonth1.render("Statki", False, (0,0,0))
        self.screen.blit(text, (100,250))

        text = self.fonth2.render("Liczba statków o wielkości 1", False, (0,0,0))
        self.screen.blit(text, (130,320))
        text = self.fonth2.render("Liczba statków o wielkości 2", False, (0,0,0))
        self.screen.blit(text, (130,470))
        text = self.fonth2.render("Liczba statków o wielkości 3", False, (0,0,0))
        self.screen.blit(text, (130,620))
        text = self.fonth2.render("Liczba statków o wielkości 4", False, (0,0,0))
        self.screen.blit(text, (130,770))


        #Checkbox draw
        for j in range (0,4):
            for i in range (0,9):
                text = self.fonth2.render(str(i), False, (0,0,0))
                self.screen.blit(text, (135+(i*100),410+(j*150)))
                self.Ships[j][i].draw(self.screen)

        #draw exit button
        self.draw_exit_button()
        #draw menu button
        self.draw_menu_button()


        #update volume
        self.volumeMusicSlider.newButPos(self.volumeMusic)
        self.volumeEffectsSlider.newButPos(self.volumeEffects)
        
        #draw sliders
        self.volumeMusicSlider.draw(self.screen)
        self.volumeEffectsSlider.draw(self.screen)
    
    def draw_exit_button(self):
        self.exit_button.draw(self.screen)

        if self.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.exit_button.color = self.exit_button_hover_color
        else:
            self.exit_button.color = self.exit_button_color
    
    def draw_menu_button(self):
        self.menu_button.draw(self.screen)

        if self.menu_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.menu_button.color = self.menu_button_hover_color
        else:
            self.menu_button.color = self.menu_button_color

    def use_draw(self):
        self.Custom_page_draw()
 