import Gui.Pygame_Util as pu
import sys
import pygame
from pygame import mixer, init

pygame.init()
pygame.display.set_caption('Tablica Wyników')

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BACKGROUND_COLOR = (200, 232, 232)
text_color = (19, 38, 87)

class scoreboard():
    def __init__(self,s):
        self.screen = s
        # do tytułu
        self.font = pygame.font.SysFont("arial",80, bold=True)
        self.title_text = "Tablica Wyników"
        self.title_text_width = self.font.size(self.title_text)[0]
        self.title_text_x = (SCREEN_WIDTH - self.title_text_width) // 2

        #do wyjasnien
        self.fonts = pygame.font.SysFont("arial", 40, bold=True)

        # exit button
        self.exit_button_color = (200, 0, 0)
        self.exit_button_hover_color = (150, 0, 0)
        self.exit_button = pu.button(self.exit_button_color,SCREEN_WIDTH - 60,10,50,50,"X",(0,0,0),"monospace",30)

        # menu button
        self.menu_button_color = (128, 128, 128)
        self.menu_button_hover_color = (128, 128, 200)
        self.menu_button = pu.button(self.menu_button_color,SCREEN_WIDTH - 220,10,150,50,"Menu",(0,0,0),"monospace",30)

        # Wczytywanie inicjalizacja
        self.file_path = "Gui/nicks.txt"
        self.file_content = self.load_file_content(self.file_path)

        self.fileW_path = "Gui/winrate.txt"
        self.fileW_content = self.load_file_content(self.fileW_path)

        self.fileG_path = "Gui/games.txt"
        self.fileG_content = self.load_file_content(self.fileG_path)

        self.fileS_path = "Gui/score.txt"
        self.fileS_content = self.load_file_content(self.fileS_path)

        self.lines_nicks = self.file_content.split('\n')
        self.lines_winrate = self.fileW_content.split('\n')
        self.lines_games = self.fileG_content.split('\n')
        self.lines_score = self.fileS_content.split('\n')

    # Rysowanie tytułu
    def draw_text(self,text,font,text_color,x,y):
        img = font.render(text,True,text_color)
        self.screen.blit(img,(x,y))

        # Wczytywanie wyników z pliku
    def load_file_content(self,file_path):
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
            return file_content
        except FileNotFoundError:
            print(f"Nie można odnaleźć pliku: {file_path}")
            sys.exit()

    
    def use_draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        # rysowanie tytułu
        self.draw_text(self.title_text,self.font,text_color,self.title_text_x,50)

        # rysowanie przycisku wyjścia
        self.draw_exit_button()
        self.draw_menu_button()

        # rysowanie "wyjasnien"
        self.draw_text("Nazwa",self.fonts, text_color,150, 250)
        self.draw_text("% Zwycięstw", self.fonts, text_color, 350, 250)
        self.draw_text("Rozegrane gry", self.fonts, text_color, 650, 250)
        self.draw_text("Całkowity wynik", self.fonts, text_color, 950, 250)

        # rysowanie zawartości plików
        for i, line in enumerate(self.lines_nicks):
            self.draw_text(line, self.fonts, text_color, 150, 300 + i * 2 * 40)

        for i, line in enumerate(self.lines_winrate):
            self.draw_text(line, self.fonts, text_color, 350, 300 + i * 2 * 40)

        for i, line in enumerate(self.lines_games):
            self.draw_text(line, self.fonts, text_color, 650, 300 + i * 2 * 40)

        for i, line in enumerate(self.lines_score):
            self.draw_text(line, self.fonts, text_color, 950, 300 + i * 2 * 40)

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
