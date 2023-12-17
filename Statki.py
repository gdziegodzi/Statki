import atexit

import pygame
from pygame import mixer
import Gui.game_screen as gs
import Gui.main_menu as mm
import Gui.Settings as st
import Gui.Page_custom as pc
import Gui.scoreboard as sb
import Gui.SetShips as ss

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# wybór okna startowego
choice = "main_menu"

# Głośność
volumeMusic = 0.05
volumeEffects = 0.20
try:
    with open("Gui/sound.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            volumeMusic = float(lines[0].strip())
            volumeEffects = float(lines[1].strip())
except FileNotFoundError:
    print("Plik sound.txt nie istnieje. Używam domyślnych wartości.")

# Muzyka w tle
pygame.mixer.init()
mixer.music.load('Sounds/background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(volumeMusic)

# Dźwięki
startButtonclick = pygame.mixer.Sound("Sounds/startButton.mp3")
checkclick = pygame.mixer.Sound("Sounds/checkbox.mp3")
buttonclick = pygame.mixer.Sound("Sounds/checkbox.mp3")

# Delays
delay_leave = 2100

buttonclick.set_volume(volumeEffects)


# Funkcja do nadpisywania głośności efektów dzwiękowych
def setVolumeEffects(vol):
    checkclick.set_volume(vol)
    startButtonclick.set_volume(vol)


setVolumeEffects(volumeEffects)

# obiekty stron
game = gs.game_screen(screen)
menu = mm.main_menu(screen)
settings = st.settings(screen, choice, volumeMusic, volumeEffects)
custom = pc.page_custom(screen, volumeMusic, volumeEffects)
scoreboard = sb.scoreboard(screen)
SetShips = ss.SetShips(screen)

run = True

try:
    with open("Gui/sound.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            volumeMusic = float(lines[0].strip())
            volumeEffects = float(lines[1].strip())
except FileNotFoundError:
    print("Plik sound.txt nie istnieje. Używam domyślnych wartości.")


def save_game_board_size_to_file(filename, rows, cols):
    with open(filename, 'w') as file:
        file.write(f"{rows}\n{cols}")


def save_ships_number_to_file(filename, number1, number2, number3, number4):
    with open(filename, 'w') as file:
        file.write(f"{number1}\n{number2}\n{number3}\n{number4}")


# Rejestracja funkcji przy wyjściu z programu
atexit.register(save_game_board_size_to_file, 'Gui/gameboard.txt', 10, 10)
atexit.register(save_ships_number_to_file, 'Gui/ships.txt', 4, 3, 2, 2)

while run:
    screen.fill((200, 232, 232))
    if choice == "main_menu":
        pygame.display.set_caption("Statki: Bitwa trwa")
        menu.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    buttonclick.play()
                    for b in menu.tab_but:
                        if b.but_rect.collidepoint(pygame.mouse.get_pos()):
                            for t in menu.menu_buttons:
                                if t["text"] == b.text:
                                    choice = t["function"]
                                    if choice == "settings":
                                        settings.prechoice = "main_menu"
                                    if choice == "setShips":
                                        SetShips.set_new_value()

    if choice == "setShips":
        SetShips.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "settings"
                settings.menu_buttons[3]["function"] = "setShips"
                buttonclick.play()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                SetShips.toggle_rotation()
            if event.type == pygame.MOUSEBUTTONUP:
                if SetShips.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "quit_game"
                if SetShips.settings_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "settings"
                    settings.menu_buttons[3]["function"] = "setShips"
                    buttonclick.play()
                if SetShips.confirm_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    if SetShips.all_ships_placed:
                        choice = "game_screen"
                        startButtonclick.play()
                        SetShips.clear_empty_on_board()
                        game.game_board_1 = SetShips.game_board_1
                if SetShips.reset_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    SetShips.reset_board()
                for i, ship in enumerate(SetShips.but_show_ship):
                    if ship.but_rect.collidepoint(pygame.mouse.get_pos()):
                        SetShips.chosen_ship = i
                for a, row in enumerate(SetShips.board_rect):
                    for b, rect in enumerate(row):
                        if rect.collidepoint(pygame.mouse.get_pos()) and SetShips.tab_number_of_ship[
                            SetShips.chosen_ship] > 0:
                            SetShips.place_ship_on_board(a, b)
            for a, row in enumerate(SetShips.board_rect):
                for b, rect in enumerate(row):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        SetShips.mark_hover_tile(a, b)
    if choice == "game_screen":
        game.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "settings"
                settings.menu_buttons[3]["function"] = "game_screen"
                buttonclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game.legend_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "game_legend"
                        settings.prechoice = "game_screen"
                        buttonclick.play()
                    if game.settings_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "settings"
                        settings.menu_buttons[3]["function"] = "game_screen"
                        buttonclick.play()
                    if game.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "quit_game"
                        buttonclick.play()
                    if game.turn == "player":
                        for a, row in enumerate(game.board_rect_AI):
                            for b, rect in enumerate(row):
                                if rect.collidepoint(pygame.mouse.get_pos()):
                                    game.player_shoot(a,b)
            for a, row in enumerate(game.board_rect_AI):
                for b, rect in enumerate(row):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        game.mark_hover_tile(a,b)

        game.check_end()
        if game.turn == "cpu" and game.is_end is False:
            game.use_draw()
            game.cpu_move()
        game.check_end()

    if choice == "settings":
        settings.volumeMusic = volumeMusic
        settings.volumeEffects = volumeEffects
        settings.use_draw()
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for b in settings.tab_but:
                        if b.but_rect.collidepoint(pygame.mouse.get_pos()):
                            for t in settings.menu_buttons:
                                if t["text"] == b.text:
                                    choice = t["function"]
                                    buttonclick.play()
                                    if t["text"] == "Legenda":
                                        settings.prechoice = "settings"
            if pygame.mouse.get_pressed()[0] and settings.volumeMusicSlider.conteiner_rect.collidepoint(
                    pygame.mouse.get_pos()):
                settings.volumeMusicSlider.move_slider(pygame.mouse.get_pos())
                settings.volumeMusicSlider.draw(screen)
                volumeMusic = settings.volumeMusicSlider.get_value()
                mixer.music.set_volume(volumeMusic)
            if pygame.mouse.get_pressed()[0] and settings.volumeEffectsSlider.conteiner_rect.collidepoint(
                    pygame.mouse.get_pos()):
                settings.volumeEffectsSlider.move_slider(pygame.mouse.get_pos())
                settings.volumeEffectsSlider.draw(screen)
                volumeEffects = settings.volumeEffectsSlider.get_value()
                setVolumeEffects(volumeEffects)

    if choice == "custom":
        custom.volumeMusic = volumeMusic
        custom.volumeEffects = volumeEffects
        custom.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "main_menu"
                buttonclick.play()

            if event.type == pygame.MOUSEBUTTONUP:
                # Sprawdź przyciski na planszy i statki
                for b in custom.BoardSize:
                    if b.isOver(pygame.mouse.get_pos()):
                        for p in custom.BoardSize:
                            if p.isChecked():
                                p.convert(custom.screen)
                        b.convert(custom.screen)
                        checkclick.play()
                        pygame.display.flip()
                for s in custom.Ships:
                    for z in s:
                        if z.isOver(pygame.mouse.get_pos()):
                            for d in s:
                                if d.isChecked():
                                    d.convert(custom.screen)
                            z.convert(custom.screen)
                            checkclick.play()
                            pygame.display.flip()
                if custom.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "quit_game"
                if custom.menu_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "main_menu"
                    buttonclick.play()
                if custom.play_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    SetShips.set_new_value()
                    choice = "setShips"
                    buttonclick.play()

                    buttonclick.play()
            if pygame.mouse.get_pressed()[0] and custom.volumeMusicSlider.conteiner_rect.collidepoint(
                    pygame.mouse.get_pos()):
                custom.volumeMusicSlider.move_slider(pygame.mouse.get_pos())
                custom.volumeMusicSlider.draw(screen)
                volumeMusic = custom.volumeMusicSlider.get_value()
                mixer.music.set_volume(custom.volumeMusic)
            if pygame.mouse.get_pressed()[0] and custom.volumeEffectsSlider.conteiner_rect.collidepoint(
                    pygame.mouse.get_pos()):
                custom.volumeEffectsSlider.move_slider(pygame.mouse.get_pos())
                custom.volumeEffectsSlider.draw(screen)
                volumeEffects = custom.volumeEffectsSlider.get_value()
                setVolumeEffects(volumeEffects)
    if choice == "scoreboard":
        scoreboard.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "main_menu"
                buttonclick.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scoreboard.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "quit_game"
                if scoreboard.menu_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = "main_menu"
                    buttonclick.play()
    if choice == "game_legend":
        game.draw_legend()
        game.legend_button.text = "Powrót"
        game.draw_legend_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = settings.prechoice
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.legend_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                    choice = settings.prechoice
                    game.legend_button.text = "Legenda"
                    buttonclick.play()
    if choice == "quit_game":
        startButtonclick.play()
        pygame.time.delay(delay_leave)
        run = False
    pygame.display.flip()

pygame.quit()
