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
volumeMusic = 0.20
volumeEffects = 0.20

# obiekty stron
game = gs.game_screen(screen)
menu = mm.main_menu(screen)
settings = st.settings(screen,choice,volumeMusic,volumeEffects)
custom = pc.page_custom(screen)
scoreboard = sb.scoreboard(screen)
SetShips = ss.SetShips(screen)



pygame.mixer.init()
mixer.music.load('Sounds/background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.01)

run = True

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
                    for b in menu.tab_but:
                        if b.but_rect.collidepoint(pygame.mouse.get_pos()):
                            for t in menu.menu_buttons:
                                if t["text"] == b.text:
                                    choice = t["function"]
                                    if choice == "settings":
                                        settings.prechoice = "main_menu"
    if choice == "setShips":
        SetShips.use_draw()
        SetShips.check_confirm_button_click()
        if SetShips.confirm_button_clicked == True:
            choice="game_screen"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "settings"
                settings.menu_buttons[3]["function"] = "setShips"
            
    if choice == "game_screen":
        game.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "settings"
                settings.menu_buttons[3]["function"] = "game_screen"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if game.legend_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "game_legend"
                        settings.prechoice = "game_screen"
                    if game.settings_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "settings"
                        settings.menu_buttons[3]["function"] = "game_screen"
                    if game.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
                        choice = "quit_game"
    if choice == "settings":
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
                                    if t["text"] == "Legenda":
                                        settings.prechoice = "settings"
            if pygame.mouse.get_pressed()[0] and settings.volumeMusicSlider.conteiner_rect.collidepoint(pygame.mouse.get_pos()):
                settings.volumeMusicSlider.move_slider(screen,pygame.mouse.get_pos())
                settings.volumeMusicSlider.draw(screen)
                settings.volumeMusic = settings.volumeMusicSlider.get_value()
                mixer.music.set_volume(settings.volumeMusic)
            if pygame.mouse.get_pressed()[0] and settings.volumeEffectsSlider.conteiner_rect.collidepoint(pygame.mouse.get_pos()):
                settings.volumeEffectsSlider.move_slider(screen,pygame.mouse.get_pos())
                settings.volumeEffectsSlider.draw(screen)
                settings.volumeEffects = settings.volumeEffectsSlider.get_value()
        
    if choice == "custom":
        custom.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "main_menu"
            if event.type == pygame.MOUSEBUTTONUP:
                # Sprawdź przyciski na planszy i statki
                for b in custom.BoardSize:
                    if b.isOver(pygame.mouse.get_pos()):
                        for p in custom.BoardSize:
                            if p.isChecked():
                                p.convert(custom.screen)
                        b.convert(custom.screen)
                        pygame.display.flip()
                for s in custom.Ships:
                    for z in s:
                        if z.isOver(pygame.mouse.get_pos()):
                            for d in s:
                                if d.isChecked():
                                    d.convert(custom.screen)
                            z.convert(custom.screen)
                            pygame.display.flip()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if custom.exit_button_rect.collidepoint(event.pos):
                #         mixer.music.stop()
                #         custom.exit_sound.play()
                #         pygame.time.delay(3000)
                #         run = False

            # Rysuj przyciski i tekst na ekranie
            # pygame.draw.rect(custom.screen, custom.exit_button_color if not custom.exit_button_rect.collidepoint(
            #     pygame.mouse.get_pos()) else custom.exit_button_hover_color, custom.exit_button_rect)
            # pygame.draw.rect(custom.screen,
            #                  custom.settings_button_color if not custom.settings_button_rect.collidepoint(
            #                      pygame.mouse.get_pos()) else custom.settings_button_hover_color,
            #                  custom.settings_button_rect)

            # Tekst na przyciskach
            # custom.screen.blit(custom.settings_button_text,
            #                    (custom.settings_button_x + 10, custom.settings_button_y + 10))
            # custom.screen.blit(custom.exit_button_text, (custom.exit_button_x + 10, custom.exit_button_y + 10))
    if choice == "scoreboard":
        scoreboard.use_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                choice = "main_menu"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scoreboard.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    run = False
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
    if choice == "quit_game":
        run = False
    pygame.display.flip()

pygame.quit()
