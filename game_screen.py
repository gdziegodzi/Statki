import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#  ----------------------------------------------------------------------------------
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
game_board_1[3][2] = "."
game_board_1[5][7] = "."
game_board_1[7][4] = "."
game_board_1[7][7] = "X"
game_board_1[4][2] = "X"
game_board_1[4][4] = "X"

game_board_2 = [[" " for c in range(game_board_cols)] for r in range(game_board_rows)]
game_board_2[0][0] = "S"
game_board_2[1][0] = "S"
game_board_2[2][0] = "S"
game_board_2[3][0] = "X"
game_board_2[4][2] = "."
game_board_2[5][7] = "."
game_board_2[6][6] = "."
game_board_2[7][7] = "."
game_board_2[7][1] = "."
game_board_2[4][0] = "X"
game_board_2[1][3] = "X"
#  ------------------------------------------------------------------------- end mock

# title background
title_bg_color = (0, 192, 255)
title_bg_width = 1000
title_bg_height = 75
title_bg_x = (SCREEN_WIDTH // 2) - (title_bg_width // 2)
title_bg_y = 0
title_bg_rectangle = pygame.Rect((title_bg_x, title_bg_y, title_bg_width, title_bg_height))

# title text
title_text_string = "Lorem ipsum"
title_text_color = (64, 255, 32)
title_font_size = 50
my_font = pygame.font.SysFont("monospace", title_font_size, bold=True)
title_text = my_font.render(title_text_string, 1, title_text_color)
title_text_x = SCREEN_WIDTH // 2 - title_text.get_rect().width
title_text_y = title_bg_y + title_text.get_rect().height // 2
text_rect = title_text.get_rect(center=title_bg_rectangle.center)

# bottom ui background (footer)
bottom_ui_bg_color = (0, 192, 255)
bottom_ui_bg_width = SCREEN_WIDTH
bottom_ui_bg_height = 100
bottom_ui_bg_x = 0
bottom_ui_bg_y = 980
bottom_ui_bg_rectangle = pygame.Rect((title_bg_x, title_bg_y, title_bg_width, title_bg_height))


def prepare_board(game_board, tile_size, hide_ships=False):
    tile_color_empty = (255, 255, 255)
    tile_color_ship = (140, 70, 20)
    tile_color_shotted_empty = (128, 128, 128)
    tile_color_shotted_ship = (255, 0, 0)

    tile_color_border = (128, 255, 0)

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


# Game loop
# Press ESC to exit
pygame.display.set_caption("Statki: Bitwa trwa")

run = True
clock = pygame.time.Clock()

while run:
    screen.fill((0, 0, 0))

    # title background draw
    pygame.draw.rect(screen, title_bg_color, title_bg_rectangle)

    # title text draw
    screen.blit(title_text, text_rect)

    # draw boards
    draw_boards()

    # draw bottom ui (footer)
    pygame.draw.rect(screen, bottom_ui_bg_color,
                     (bottom_ui_bg_x, bottom_ui_bg_y, bottom_ui_bg_width, bottom_ui_bg_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
