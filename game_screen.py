import pygame
from pygame import mixer
import tkinter as tk
from tkinter import Scale


volume = 0.5
pygame.init()

pygame.mixer.init()
mixer.music.load('background.mp3')
mixer.music.play(-1)
mixer.music.set_volume(volume)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def change_volume(new_volume):
    volume = float(new_volume)
    mixer.music.set_volume(volume)


def show_volume_settings():
    root = tk.Tk()
    root.title("Zmiana głośności")
    root.geometry("400x100")

    volume_scale = Scale(root, label="Głośność", from_=0.01, to=1.00, resolution=0.01, orient="horizontal", command=change_volume)
    volume_scale.set(mixer.music.get_volume())  # Ustaw aktualną głośność
    volume_scale.pack()
    root.mainloop()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ----------------------------------------------------------------------------------
# mocked game board to test
"""
    space - empty space
    S - ship
    . - shotted empty space
    X - shotted ship
"""

# rows should equal columns
# square board 8x8, 9x9, 10x10, 11x11, 12x12
game_board_rows = 10
game_board_cols = 10

game_board_1 = [[" " for c in range(game_board_cols)] for r in range(game_board_rows)]
game_board_1[0][0] = "S"
game_board_1[0][1] = "S"
game_board_1[0][2] = "S"
game_board_1[6][5] = "S"
game_board_1[7][5] = "S"
game_board_1[8][5] = "S"
game_board_1[3][6] = "."
game_board_1[5][7] = "."
game_board_1[7][4] = "."
game_board_1[7][7] = "X"
game_board_1[4][2] = "X"
game_board_1[4][3] = "X"

game_board_2 = [[" " for c in range(game_board_cols)] for r in range(game_board_rows)]
game_board_2[0][0] = "S"
game_board_2[1][0] = "S"
game_board_2[2][0] = "S"
game_board_2[4][0] = "X"
game_board_2[1][3] = "X"
game_board_2[1][4] = "X"
game_board_2[4][2] = "."
game_board_2[5][7] = "."
game_board_2[7][7] = "."
game_board_2[7][1] = "."

# -------------------------------------------------------------------------- end mock

# title background
title_bg_color = (0, 192, 255)
title_bg_width = 1000
title_bg_height = 75
title_bg_x = (SCREEN_WIDTH // 2) - (title_bg_width // 2)
title_bg_y = 0
title_bg_rectangle = pygame.Rect((title_bg_x, title_bg_y, title_bg_width, title_bg_height))

# title text
title_text_string = "Statki"
title_text_color = (64, 255, 32)
title_font_size = 50
my_font = pygame.font.SysFont("monospace", title_font_size, bold=True)
title_text = my_font.render(title_text_string, 1, title_text_color)
title_text_x = SCREEN_WIDTH // 2 - title_text.get_rect().width
title_text_y = title_bg_y + title_text.get_rect().height // 2
text_rect = title_text.get_rect(center=title_bg_rectangle.center)

# board colors
tile_color_empty = (255, 255, 255)
tile_color_ship = (140, 70, 20)
tile_color_shotted_empty = (128, 128, 128)
tile_color_shotted_ship = (255, 0, 0)
tile_color_border = (128, 255, 0)

# bottom ui background (footer)
bottom_ui_bg_color = (0, 192, 255)
bottom_ui_bg_width = SCREEN_WIDTH
bottom_ui_bg_height = 100
bottom_ui_bg_x = 0
bottom_ui_bg_y = 980
bottom_ui_bg_rectangle = pygame.Rect((title_bg_x, title_bg_y, title_bg_width, title_bg_height))

# legend button
legend_button_width = 150
legend_button_height = 50
legend_button_x = SCREEN_WIDTH - legend_button_width - 10
legend_button_y = 75
legend_button_rect = pygame.Rect((legend_button_x, legend_button_y, legend_button_width, legend_button_height))
legend_button_color = (0, 200, 0)
legend_button_hover_color = (0, 150, 0)
legend_button_font_size = 30
legend_button_font = pygame.font.SysFont("monospace", legend_button_font_size, bold=True)
legend_button_text = legend_button_font.render("Legenda", 1, (255, 255, 255))
legend_button_leave_text = legend_button_font.render("Powrót", 1, (255, 255, 255))

# legend
legend_bg_color = (0, 192, 255)
legend_bg_x = 50
legend_bg_y = 150
legend_bg_width = screen.get_width() - 2 * legend_bg_x
legend_bg_height = 775
legend_bg_rectangle = pygame.Rect((legend_bg_x, legend_bg_y, legend_bg_width, legend_bg_height))

# legend text
legend_text_color = (0, 0, 0)
legend_font_size = 32
legend_font = pygame.font.SysFont("monospace", legend_font_size, bold=True)
legend_padding = 50
legend_row_spacing = 100
legend_text_x = legend_bg_x + legend_padding
legend_text_y = legend_bg_y + legend_padding
legend_text_left_margin = 75

# exit button
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

# timer
timer_width = 150
timer_height = 50
timer_x = 10
timer_y = 10
timer_rect = pygame.Rect((timer_x, timer_y, timer_width, timer_height))
timer_color = (0, 0, 0)
timer_font_size = 30
timer_text_color = (255, 255, 255)
timer_font = pygame.font.SysFont("monospace", timer_font_size, bold=True)


def draw_title_text():
    screen.blit(title_text, text_rect)


def draw_title_background():
    pygame.draw.rect(screen, title_bg_color, title_bg_rectangle)


def prepare_board(game_board, tile_size, hide_ships=False):
    tile_border_size = 1

    board = pygame.Surface(
        (tile_size * game_board_cols + 4 * tile_border_size, tile_size * game_board_rows + 4 * tile_border_size))

    marker_color = tile_color_empty
    for row in range(game_board_rows):
        for col in range(game_board_cols):
            if game_board[row][col] == " ":
                marker_color = tile_color_empty
            elif game_board[row][col] == "S":
                marker_color = tile_color_ship
                if hide_ships:
                    marker_color = tile_color_empty
            elif game_board[row][col] == ".":
                marker_color = tile_color_shotted_empty
            elif game_board[row][col] == "X":
                marker_color = tile_color_shotted_ship

            # draw border
            pygame.draw.rect(board, tile_color_border, (row * tile_size, col * tile_size, tile_size, tile_size))

            # draw tile
            pygame.draw.rect(board, marker_color, (
                row * tile_size + tile_border_size, col * tile_size + tile_border_size,
                tile_size - 2 * tile_border_size,
                tile_size - 2 * tile_border_size))
    return board


def draw_axis_description(tile_size, space_between_boards, start_x, start_y):
    text_color = (255, 255, 255)
    font_size = 30
    offset = 15
    total_space = space_between_boards + tile_size * game_board_cols

    font = pygame.font.SysFont("monospace", font_size, bold=True)

    for row in range(game_board_rows):
        text = font.render(chr(row + 65), 1, text_color)
        screen.blit(text, (start_x - tile_size, start_y + row * tile_size + offset))
        screen.blit(text, (start_x - tile_size + total_space, start_y + row * tile_size + offset))

    for col in range(game_board_cols):
        text = font.render(str(col + 1), 1, text_color)
        screen.blit(text, (start_x + col * tile_size + offset, start_y - tile_size))
        screen.blit(text, (start_x + col * tile_size + offset + total_space, start_y - tile_size))


def draw_boards():
    start_x = 125
    start_y = 250
    space_between_boards = 400

    # rows == columns
    tile_size = 650 // game_board_rows

    draw_axis_description(tile_size, space_between_boards, start_x, start_y)

    board = prepare_board(game_board_1, tile_size)
    board2 = prepare_board(game_board_2, tile_size, True)

    screen.blit(board, (start_x, start_y))
    screen.blit(board2, (start_x + tile_size * game_board_cols + space_between_boards, start_y))


def draw_legend_button(is_legend_shown):
    pygame.draw.rect(screen, legend_button_color, legend_button_rect)

    if legend_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, legend_button_hover_color, legend_button_rect)

    if not is_legend_shown:
        screen.blit(legend_button_text, (legend_button_x + 10, legend_button_y + 10))
    else:
        screen.blit(legend_button_leave_text, (legend_button_x + 10, legend_button_y + 10))


def draw_legend():
    legend_texts = ["- puste miejsce / niesprawdzone miejsce",
                    "- statek",
                    "- trafiony statek",
                    "- pudło / miejsce w którym na pewno nie ma statku"]

    legend_rendered_texts = [legend_font.render(legend_texts[0], 1, legend_text_color),
                             legend_font.render(legend_texts[1], 1, legend_text_color),
                             legend_font.render(legend_texts[2], 1, legend_text_color),
                             legend_font.render(legend_texts[3], 1, legend_text_color)]

    board_colors = [tile_color_empty, tile_color_ship, tile_color_shotted_ship, tile_color_shotted_empty]

    pygame.draw.rect(screen, legend_bg_color, legend_bg_rectangle)

    for i in range(4):
        pygame.draw.rect(screen, board_colors[i],
                         (legend_bg_x + legend_padding, legend_bg_y + legend_padding + i * legend_row_spacing, 50, 50))

        screen.blit(legend_rendered_texts[i],
                    (legend_text_x + legend_text_left_margin,
                     legend_text_y + i * legend_row_spacing + legend_rendered_texts[i].get_height() // 4))


def draw_exit_button():
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)

    if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, exit_button_hover_color, exit_button_rect)

    screen.blit(exit_button_text, (exit_button_x + 10, exit_button_y + 10))


def draw_bottom_ui():
    pygame.draw.rect(screen, bottom_ui_bg_color,
                     (bottom_ui_bg_x, bottom_ui_bg_y, bottom_ui_bg_width, bottom_ui_bg_height))


def draw_timer():
    # in ms
    current_time = pygame.time.get_ticks() - start_time

    hours = str(current_time // 3600_000).zfill(2)
    minutes = str((current_time // 60_000) % 60).zfill(2)
    seconds = str((current_time // 1_000) % 60).zfill(2)

    timer_text = exit_button_font.render(f"{hours}:{minutes}:{seconds}", 1, timer_text_color)

    pygame.draw.rect(screen, timer_color, timer_rect)
    screen.blit(timer_text, (timer_x + 10, timer_y + 10))


pygame.display.set_caption("Statki: Bitwa trwa")

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


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

# Utworzenie flagi do śledzenia, czy przycisk wyjścia został kliknięty
exit_button_clicked = False

run = True
show_legend = False

while run:
    screen.fill((0, 0, 0))

    # title background draw
    draw_title_background()

    # title text draw
    draw_title_text()


    # draw boards
    draw_boards()

    # draw button showing legend
    draw_legend_button(show_legend)

    # draw legend
    if show_legend:
        draw_legend()

    # draw bottom ui (footer)
    draw_bottom_ui()


    # Rysujemy przycisk wyjścia
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    pygame.draw.rect(screen, settings_button_color, settings_button_rect)
    if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, settings_button_hover_color, settings_button_rect)
    screen.blit(settings_button_text, (settings_button_x + 10, settings_button_y + 10))

    if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, exit_button_hover_color, exit_button_rect)
    screen.blit(exit_button_text, (exit_button_x + 10, exit_button_y + 10))

    # draw exit button
    draw_exit_button()

    # draw timer
    draw_timer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if settings_button_rect.collidepoint(event.pos):
                show_volume_settings()
            elif exit_button_rect.collidepoint(event.pos):
                exit_button_clicked = True
            elif legend_button_rect.collidepoint(event.pos):
                show_legend = not show_legend

    if exit_button_clicked:
        mixer.music.stop()
        exit_sound.play()
        pygame.time.delay(3000)
        run = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

