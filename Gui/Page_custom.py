import Gui.Pygame_Util as pu
import pygame
from pygame import mixer
import tkinter as tk

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()
pygame.font.init()

class page_custom():
    def __init__(self, s, vol1, vol2):
        self.screen = s
        self.volume = 0.05

        self.fontcolor = (19, 38, 87)

        # Volume Sliders
        self.volumeMusic = vol1
        self.volumeEffects = vol2
        self.slidersWidth = 600
        self.slidersHeight = 40
        self.volumeMusicSlider = pu.slider((255,125,0),1100, SCREEN_HEIGHT - 300, self.slidersWidth, self.slidersHeight, self.volumeMusic, 0, 1)
        self.volumeEffectsSlider = pu.slider((255,125,0),1100, SCREEN_HEIGHT - 200, self.slidersWidth, self.slidersHeight, self.volumeEffects, 0, 1)

        # Background color
        self.background_colour = (200, 232, 232)

        # Tab declaration
        self.BoardSize = []
        self.Ships = [[],[],[],[]]

        # Inicjalizacja przycisku wyjścia
        self.exit_button_color = (200, 0, 0)
        self.exit_button_hover_color = (150, 0, 0)
        self.exit_button = pu.button(self.exit_button_color, SCREEN_WIDTH - 60, 10, 50, 50, "X", (0,0,0), "monospace", 30)

        # Menu button
        self.menu_button_color = (128, 128, 128)
        self.menu_button_hover_color = (128, 128, 200)
        self.menu_button = pu.button(self.menu_button_color, SCREEN_WIDTH - 220, 10, 150, 50, "Menu", (0,0,0), "monospace", 30)

        # Board tab
        for x in range(0,4):
            self.BoardSize.append((pu.checkbox((110,0,0), 115 + (x*200), 120, 30, 30)))

        # Checkbox tab
        for j in range(0,4):
            for i in range(0,9):
                self.Ships[j].append((pu.checkbox((0,0,0), 130+(i*100), 380+(j*150), 30, 30)))

    def Custom_page_draw(self):
        self.screen.fill(self.background_colour)
        self.fonth1 = pygame.font.SysFont("arial.ttf", 70)
        self.fonth2 = pygame.font.SysFont("arial.ttf", 50)

        text = self.fonth1.render("Rozmiar planszy", False, (0,0,0))
        self.screen.blit(text, (100,50))

        text = self.fonth1.render("Umiejętności specjalne", False, (0,0,0))
        self.screen.blit(text, (1200,100))

        text = self.fonth2.render("Zostaną dodane wkrótce!", False, (0,0,0))
        self.screen.blit(text, (1250,200))

        deafoult_text_font = pygame.font.SysFont("Comics Sans", 50)

        text = deafoult_text_font.render("Głośność muzyki: " + f"{self.volumeMusic:.2f}" , False, self.fontcolor)
        self.screen.blit(text, (1200, SCREEN_HEIGHT - 350))

        text = deafoult_text_font.render("Głośność efektów: "+ f"{self.volumeEffects:.2f}" , False, self.fontcolor)
        self.screen.blit(text, (1200, SCREEN_HEIGHT - 250))

        for x in range(0,4):
            self.BoardSize[x].draw(self.screen)

        text = self.fonth2.render("9x9", False, (0,0,0))
        self.screen.blit(text, (100, 150))

        text = self.fonth2.render("10x10", False, (0,0,0))
        self.screen.blit(text, (280, 150))

        text = self.fonth2.render("11x11", False, (0,0,0))
        self.screen.blit(text, (485, 150))

        text = self.fonth2.render("12x12", False, (0,0,0))
        self.screen.blit(text, (680, 150))

        text = self.fonth1.render("Statki", False, (0,0,0))
        self.screen.blit(text, (100, 250))

        text = self.fonth2.render("Liczba statków o wielkości 1", False, (0,0,0))
        self.screen.blit(text, (130, 320))

        text = self.fonth2.render("Liczba statków o wielkości 2", False, (0,0,0))
        self.screen.blit(text, (130, 470))

        text = self.fonth2.render("Liczba statków o wielkości 3", False, (0,0,0))
        self.screen.blit(text, (130, 620))

        text = self.fonth2.render("Liczba statków o wielkości 4", False, (0,0,0))
        self.screen.blit(text, (130, 770))

        # Checkbox tab
        checkbox_configuration = {
            '9x9': {4: 4, 3: 3, 2: 2, 1: 1},
            '10x10': {4: 5, 3: 4, 2: 3, 1: 2},
            '11x11': {4: 6, 3: 5, 2: 4, 1: 3},
            '12x12': {4: 7, 3: 6, 2: 5, 1: 4}
        }

        for j in range(4):
            for i in range(9):
                if not any(bs.isChecked() for bs in self.BoardSize):
                    self.Ships[j][i].draw(self.screen)
                else:
                    selected_board = None
                    if self.BoardSize[0].isChecked():
                        selected_board = '9x9'
                    elif self.BoardSize[1].isChecked():
                        selected_board = '10x10'
                    # Dodaj warunki dla 11x11 i 12x12
                    elif self.BoardSize[2].isChecked():
                        selected_board = '11x11'
                    elif self.BoardSize[3].isChecked():
                        selected_board = '12x12'

                    if selected_board:
                        clickable_count = checkbox_configuration[selected_board].get(4 - j, 0)
                        if i < clickable_count:
                            self.Ships[j][i].draw(self.screen)

        for i in range(4):
            text = self.fonth2.render(str(i + 1), False, (0,0,0))
            self.screen.blit(text, (135 + (i * 100), 770))

        for j in range(4):
            for i in range(9):
                text = self.fonth2.render(str(i + 1), False, (0,0,0))
                self.screen.blit(text, (135 + (i * 100), 410 + (j * 150)))

        self.draw_exit_button()
        self.draw_menu_button()

        self.volumeMusicSlider.newButPos(self.volumeMusic)
        self.volumeEffectsSlider.newButPos(self.volumeEffects)

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
