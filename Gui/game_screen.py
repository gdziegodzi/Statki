import random
import pygame
from pygame import mixer
import Gui.Pygame_Util as pu

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()


class game_screen():
    def __init__(self, s):
        self.screen = s
        # ----------------------------------------------------------------------------------
        """
            space - empty space
            S - ship
            . - shotted empty space
            X - shotted ship
        """

        # rows should equal columns
        # square board 8x8, 9x9, 10x10, 11x11, 12x12
        self.ships_to_place = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.game_board_rows = 10
        self.game_board_cols = 10

        self.game_board_1 = [[" " for _ in range(self.game_board_cols)] for _ in range(self.game_board_rows)]

        self.game_board_2 = self.generate_ship_board()
        # --------------------------------------------------------------------------

        # title background
        self.title_bg_color = (200, 232, 232)
        self.title_bg_width = 1000
        self.title_bg_height = 75
        self.title_bg_x = (SCREEN_WIDTH // 2) - (self.title_bg_width // 2)
        self.title_bg_y = 0
        self.title_bg_rectangle = pygame.Rect(
            (self.title_bg_x, self.title_bg_y, self.title_bg_width, self.title_bg_height))

        # title text
        self.title_text_string = "Statki"
        self.title_text_color = (19, 38, 87)
        self.title_font_size = 50
        self.my_font = pygame.font.SysFont("monospace", self.title_font_size, bold=True)
        self.title_text = self.my_font.render(self.title_text_string, 1, self.title_text_color)
        self.title_text_x = SCREEN_WIDTH // 2 - self.title_text.get_rect().width
        self.title_text_y = self.title_bg_y + self.title_text.get_rect().height // 2
        self.text_rect = self.title_text.get_rect(center=self.title_bg_rectangle.center)

        # board colors
        self.tile_color_empty = (255, 255, 255)
        self.tile_color_ship = (140, 70, 20)
        self.tile_color_shotted_empty = (128, 128, 128)
        self.tile_color_shotted_ship = (255, 0, 0)
        self.tile_color_border = (200, 232, 232)

        # bottom ui background (footer)
        self.bottom_ui_bg_color = (200, 232, 232)
        self.bottom_ui_bg_width = SCREEN_WIDTH
        self.bottom_ui_bg_height = 100
        self.bottom_ui_bg_x = 0
        self.bottom_ui_bg_y = 980
        self.bottom_ui_bg_rectangle = pygame.Rect(
            (self.title_bg_x, self.title_bg_y, self.title_bg_width, self.title_bg_height))

        
        # exit button
        self.exit_button_color = (255, 0, 0)
        self.exit_button_hover_color = (150, 0, 0)
        self.exit_button = pu.button(self.exit_button_color,
                                  SCREEN_WIDTH - 60, 10,
                                  50, 50 , "X", (255, 255, 255), "monospace", 30
                                  )

        # timer
        self.timer_width = 150
        self.timer_height = 50
        self.timer_x = 10
        self.timer_y = 10
        self.timer_rect = pygame.Rect((self.timer_x, self.timer_y, self.timer_width, self.timer_height))
        self.timer_color = (200, 232, 232)
        self.timer_font_size = 30
        self.timer_text_color = (12, 13, 13)
        self.timer_font = pygame.font.SysFont("monospace", self.timer_font_size, bold=True)

        # legend button
        self.legend_button_color = (0, 200, 0)
        self.legend_button_hover_color = (0, 150, 0)
        self.legend_button = pu.button(self.legend_button_color,
                                  SCREEN_WIDTH - 220, 10,
                                  150, 50 , "Legenda", (255, 255, 255), "monospace", 30
                                  )

        # legend
        self.legend_bg_color = (189, 189, 189)
        self.legend_bg_x = 50
        self.legend_bg_y = 150
        self.legend_bg_width = self.screen.get_width() - 2 * self.legend_bg_x
        self.legend_bg_height = 775
        self.legend_bg_rectangle = pygame.Rect(
            (self.legend_bg_x, self.legend_bg_y, self.legend_bg_width, self.legend_bg_height))
        self.show_legend = True
        

        # legend text
        self.legend_text_color = (0, 0, 0)
        self.legend_font_size = 32
        self.legend_font = pygame.font.SysFont("monospace", self.legend_font_size, bold=True)
        self.legend_padding = 50
        self.legend_row_spacing = 100
        self.legend_text_x = self.legend_bg_x + self.legend_padding
        self.legend_text_y = self.legend_bg_y + self.legend_padding
        self.legend_text_left_margin = 75

        self.legend_texts = ["- puste miejsce / niesprawdzone miejsce",
                        "- statek",
                        "- trafiony statek",
                        "- pudło / miejsce w którym na pewno nie ma statku"]

        self.legend_rendered_texts = [self.legend_font.render(self.legend_texts[0], 1, self.legend_text_color),
                                 self.legend_font.render(self.legend_texts[1], 1, self.legend_text_color),
                                 self.legend_font.render(self.legend_texts[2], 1, self.legend_text_color),
                                 self.legend_font.render(self.legend_texts[3], 1, self.legend_text_color)]
        # legend ships
        self.board_colors = [self.tile_color_empty, self.tile_color_ship, self.tile_color_shotted_ship,
                        self.tile_color_shotted_empty]
        
        # Settings button
        self.settings_button_color = (128, 128, 128)
        self.settings_button_hover_color = (128, 128, 200)
        self.settings_button = pu.button(self.settings_button_color,
                                  SCREEN_WIDTH - 380, 10,
                                  150, 50 , "Settings", (255, 255, 255), "monospace", 30
                                  )

    def draw_title_text(self):
        self.screen.blit(self.title_text, self.text_rect)

    def draw_title_background(self):
        pygame.draw.rect(self.screen, self.title_bg_color, self.title_bg_rectangle)

    def prepare_board(self, game_board, tile_size, hide_ships=False):
        tile_border_size = 1

        board = pygame.Surface(
            (tile_size * self.game_board_cols + 4 * tile_border_size,
             tile_size * self.game_board_rows + 4 * tile_border_size))

        marker_color = self.tile_color_empty
        for row in range(self.game_board_rows):
            for col in range(self.game_board_cols):
                if game_board[row][col] == " ":
                    marker_color = self.tile_color_empty
                elif game_board[row][col] == "S":
                    marker_color = self.tile_color_ship
                    if hide_ships:
                        marker_color = self.tile_color_empty
                elif game_board[row][col] == ".":
                    marker_color = self.tile_color_shotted_empty
                elif game_board[row][col] == "X":
                    marker_color = self.tile_color_shotted_ship

                # draw border
                pygame.draw.rect(board, self.tile_color_border,
                                 (row * tile_size, col * tile_size, tile_size, tile_size))

                # draw tile
                pygame.draw.rect(board, marker_color, (
                    row * tile_size + tile_border_size, col * tile_size + tile_border_size,
                    tile_size - 2 * tile_border_size,
                    tile_size - 2 * tile_border_size))
        return board

    def draw_axis_description(self, tile_size, space_between_boards, start_x, start_y):
        text_color = (12, 13, 13)
        font_size = 30
        offset = 15
        total_space = space_between_boards + tile_size * self.game_board_cols

        font = pygame.font.SysFont("monospace", font_size, bold=True)

        for row in range(self.game_board_rows):
            text = font.render(chr(row + 65), 1, text_color)
            self.screen.blit(text, (start_x - tile_size, start_y + row * tile_size + offset))
            self.screen.blit(text, (start_x - tile_size + total_space, start_y + row * tile_size + offset))

        for col in range(self.game_board_cols):
            text = font.render(str(col + 1), 1, text_color)
            self.screen.blit(text, (start_x + col * tile_size + offset, start_y - tile_size))
            self.screen.blit(text, (start_x + col * tile_size + offset + total_space, start_y - tile_size))

    def draw_boards(self):
        start_x = 125
        start_y = 250
        space_between_boards = 400

        # rows == columns
        tile_size = 650 // self.game_board_rows

        self.draw_axis_description(tile_size, space_between_boards, start_x, start_y)

        board = self.prepare_board(self.game_board_1, tile_size)
        board2 = self.prepare_board(self.game_board_2, tile_size, True)

        self.screen.blit(board, (start_x, start_y))
        self.screen.blit(board2, (start_x + tile_size * self.game_board_cols + space_between_boards, start_y))

    def draw_legend_button(self):

        self.legend_button.draw(self.screen)

        if self.legend_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.legend_button.color = self.legend_button_hover_color
        else:
            self.legend_button.color = self.legend_button_color
        
    def draw_legend(self):
        
        pygame.draw.rect(self.screen, self.legend_bg_color, self.legend_bg_rectangle)

        for i in range(4):
            pygame.draw.rect(self.screen, self.board_colors[i],
                             (self.legend_bg_x + self.legend_padding,
                              self.legend_bg_y + self.legend_padding + i * self.legend_row_spacing, 50, 50))

            self.screen.blit(self.legend_rendered_texts[i],
                             (self.legend_text_x + self.legend_text_left_margin,
                              self.legend_text_y + i * self.legend_row_spacing + self.legend_rendered_texts[
                                  i].get_height() // 4))

    def draw_exit_button(self):
        self.exit_button.draw(self.screen)

        if self.exit_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.exit_button.color = self.exit_button_hover_color
        else:
            self.exit_button.color = self.exit_button_color
    def draw_settings_button(self):

        self.settings_button.draw(self.screen)

        if self.settings_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.settings_button.color = self.settings_button_hover_color
        else:
            self.settings_button.color = self.settings_button_color

    def draw_bottom_ui(self):
        pygame.draw.rect(self.screen, self.bottom_ui_bg_color,
                         (self.bottom_ui_bg_x, self.bottom_ui_bg_y, self.bottom_ui_bg_width, self.bottom_ui_bg_height))

    def draw_timer(self):
        # in ms
        current_time = pygame.time.get_ticks() - self.start_time

        hours = str(current_time // 3600_000).zfill(2)
        minutes = str((current_time // 60_000) % 60).zfill(2)
        seconds = str((current_time // 1_000) % 60).zfill(2)

        timer_text = self.exit_button_font.render(f"{hours}:{minutes}:{seconds}", 1, self.timer_text_color)

        pygame.draw.rect(self.screen, self.timer_color, self.timer_rect)
        self.screen.blit(timer_text, (self.timer_x + 10, self.timer_y + 10))

    def use_draw(self):

        self.draw_title_background()
        self.draw_title_text()
        self.draw_boards()
        self.draw_legend_button()
        self.draw_settings_button()
        self.draw_exit_button()
        self.draw_bottom_ui()

    # clock = pygame.time.Clock()
    # start_time = pygame.time.get_ticks()

    # Add the Settings button
    settings_button_width = 160
    settings_button_height = 50
    settings_button_x = SCREEN_WIDTH - settings_button_width - 200
    settings_button_y = 10  # Adjust the vertical position
    settings_button_rect = pygame.Rect(
        (settings_button_x, settings_button_y, settings_button_width, settings_button_height))
    settings_button_color = (128, 128, 128)  # Green button color
    settings_button_hover_color = (128, 128, 200)  # Green hover color
    settings_button_font_size = 30
    settings_button_font = pygame.font.SysFont("monospace", settings_button_font_size, bold=True)
    settings_button_text = settings_button_font.render("Głośność", 1, (255, 255, 255))

    # Utworzenie flagi do śledzenia, czy przycisk wyjścia został kliknięty
    exit_button_clicked = False

    # run = True
    # show_legend = False

    # draw_title_background()
    # draw_title_text()
    # draw_boards()
    # draw_legend_button(show_legend)
    # if show_legend:
    #     draw_legend()
    # draw_bottom_ui()
    # while run:
    #     screen.fill((200, 232, 232))

    #     # title background draw
    #     draw_title_background()

    #     # title text draw
    #     draw_title_text()

    #     # draw boards
    #     draw_boards()

    #     # draw button showing legend
    #     draw_legend_button(show_legend)

    #     # draw legend
    #     if show_legend:
    #         draw_legend()

    #     # draw bottom ui (footer)
    #     draw_bottom_ui()

    #     # Rysujemy przycisk wyjścia
    #     pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    #     pygame.draw.rect(screen, settings_button_color, settings_button_rect)
    #     if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
    #         pygame.draw.rect(screen, settings_button_hover_color, settings_button_rect)
    #     screen.blit(settings_button_text, (settings_button_x + 10, settings_button_y + 10))

    #     if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
    #         pygame.draw.rect(screen, exit_button_hover_color, exit_button_rect)
    #     screen.blit(exit_button_text, (exit_button_x + 10, exit_button_y + 10))

    #     # draw exit button
    #     draw_exit_button()

    #     # draw timer
    #     draw_timer()

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #             run = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if settings_button_rect.collidepoint(event.pos):
    #                 show_volume_settings()
    #             elif exit_button_rect.collidepoint(event.pos):
    #                 exit_button_clicked = True
    #             elif legend_button_rect.collidepoint(event.pos):
    #                 show_legend = not show_legend

    #     if exit_button_clicked:
    #         mixer.music.stop()
    #         exit_sound.play()
    #         pygame.time.delay(3000)
    #         run = False

    #     pygame.display.flip()
    #     clock.tick(30)

    # pygame.quit()
    def generate_ship_board(self):
        board = [[" " for _ in range(self.game_board_cols)] for _ in range(self.game_board_rows)]

        for i in range(len(self.ships_to_place)):
            ship_len = self.ships_to_place[i]
            r_max = self.game_board_rows - 1
            c_max = self.game_board_cols - 1

            rotation = "h"
            r = 0
            c = 0

            possible_to_place = False
            while not possible_to_place:
                rotation = random.choice(("v", "h"))
                if rotation == "h":
                    c_max -= ship_len
                else:
                    r_max -= ship_len

                is_cell_free = False
                while not is_cell_free:
                    r = random.randint(0, r_max)
                    c = random.randint(0, c_max)
                    if board[r][c] == " ":
                        is_cell_free = True

                possible_to_place = True
                if rotation == "h":
                    for j in range(ship_len):
                        if board[r][c + j] != " ":
                            possible_to_place = False
                            break
                else:
                    for j in range(ship_len):
                        if board[r + j][c] != " ":
                            possible_to_place = False
                            break

            # mark adjacent fields
            if possible_to_place:
                if rotation == "h":
                    for j in range(-1, ship_len + 1):
                        if 0 <= c + j < self.game_board_cols:
                            board[r][c + j] = "."
                            if r + 1 < self.game_board_rows:
                                board[r + 1][c + j] = "."
                            if r - 1 >= 0:
                                board[r - 1][c + j] = "."
                else:
                    for j in range(-1, ship_len + 1):
                        if 0 <= r + j < self.game_board_rows:
                            board[r + j][c] = "."
                            if c + 1 < self.game_board_cols:
                                board[r + j][c + 1] = "."
                            if c - 1 >= 0:
                                board[r + j][c - 1] = "."

            # put ship
            if possible_to_place:
                if rotation == "h":
                    for j in range(ship_len):
                        board[r][c + j] = "S"
                else:
                    for j in range(ship_len):
                        board[r + j][c] = "S"

        # TODO delete after develop
        # draw board for simple test
        for r in range(self.game_board_rows):
            print(board[r])
        print()
            
        for r in range(self.game_board_rows):
            for c in range(self.game_board_cols):
                if board[r][c] == ".":
                    board[r][c] = " "
            
        # TODO delete after develop
        # draw board after preparing
        for r in range(self.game_board_rows):
            print(board[r])
        print()

        return board