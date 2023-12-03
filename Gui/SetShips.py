import pygame
import Gui.game_screen as gs
import Gui.Pygame_Util as pu


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
pygame.init()


class SetShips():
    def __init__(self, s):
        self.screen = s
        """
            space - empty space
            S - ship
            . - shotted empty space
            X - shotted ship
        """

        # rows should equal columns
        # square self.board 8x8, 9x9, 10x10, 11x11, 12x12
        self.game_board_rows = 10
        self.game_board_cols = 10

        self.game_board_1 = [[" " for c in range(self.game_board_cols)] for r in range(self.game_board_rows)]


        # -------------------------------------------------------------------------- end mock

        # title background
        self.title_bg_color = (200, 232, 232)
        self.title_bg_width = 1000
        self.title_bg_height = 75
        self.title_bg_x = (SCREEN_WIDTH // 2) - (self.title_bg_width // 2)
        self.title_bg_y = 0
        self.title_bg_rectangle = pygame.Rect(
            (self.title_bg_x, self.title_bg_y, self.title_bg_width, self.title_bg_height))

        # title text
        self.title_text_string = "Ustaw swoje statki"
        self.title_text_color = (19, 38, 87)
        self.title_font_size = 50
        self.my_font = pygame.font.SysFont("monospace", self.title_font_size, bold=True)
        self.title_text = self.my_font.render(self.title_text_string, 1, self.title_text_color)
        self.title_text_x = SCREEN_WIDTH // 2 - self.title_text.get_rect().width
        self.title_text_y = self.title_bg_y + self.title_text.get_rect().height // 2
        self.text_rect = self.title_text.get_rect(center=self.title_bg_rectangle.center)

        # self.board colors
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

        #miejsce na statki
        self.ships_placement = (245, 245, 220)
        self.ships_placement_width = 650
        self.ships_placement_height = 650
        self.ships_placement_x = 1020
        self.ships_placement_y = 250
        self.ships_placement_rectangle = pygame.Rect(
            (self.ships_placement_x, self.ships_placement_y, self.ships_placement_width, self.ships_placement_height))



        # confirm button
        self.confirm_button_x = self.ships_placement_x + (self.ships_placement_width - 180) // 2
        self.confirm_button_y = self.ships_placement_y + self.ships_placement_height - 64
        self.confirm_button_color = (0, 255, 0)
        self.confirm_button_hover_color = (0, 200, 0)
        self.confirm_button = pu.button(self.confirm_button_color,self.confirm_button_x,self.confirm_button_y,180,50,"Zatwierdź",(255, 255, 255),"monospace",30,True)

        # exit button
        self.exit_button_color = (200, 0, 0)
        self.exit_button_hover_color = (150, 0, 0)
        self.exit_button = pu.button(self.exit_button_color,SCREEN_WIDTH - 60,10,50,50,"X",(0,0,0),"monospace",30)

        # settings button
        self.settings_button_color = (128, 128, 128)
        self.settings_button_hover_color = (128, 128, 200)
        self.settings_button = pu.button(self.settings_button_color,SCREEN_WIDTH - 220,10,150,50,"Settings",(0,0,0),"monospace",30)

        # Symboliczne statki w formie przycisków
            # Ilość statków
        ships_one = 4
        ships_two = 3
        ships_three = 2
        ships_four = 2
        self.tab_number_of_ship =[ships_one,ships_two,ships_three,ships_four]
        self.font_number_ship = pygame.font.SysFont("monospace", 20, bold=True)
        self.chosen_ship = 0
        self.rotation = 'v'
            # Tablica z wizualnymi statkami
        self.but_show_ship = []
        self.tile_size = 650//self.game_board_rows
        self.tile_color= (140, 70, 20)
        self.tile_color_hover= (100, 30, 00)
        for i in range(4):
            butship = pu.button(self.tile_color, self.ships_placement_x + 50 + i *(self.tile_size + 100),
                self.ships_placement_y + 100,self.tile_size,self.tile_size+(self.tile_size*i))
            self.but_show_ship.append(butship)
            # Tablica na której rozmieścimy statki
        self.board_content = [[" " for _ in range(self.game_board_cols)] for _ in range(self.game_board_rows)]
            # Tablica na której rozmieścimy kolizje statków
        self.board_rect = [[pygame.Rect(0,0,0,0) for _ in range(self.game_board_cols)] for _ in range(self.game_board_rows)]
            # Tablica do późniejszego przechowywania statków
        self.but_ships = []
        
    def toggle_rotation(self):
        if self.rotation == 'h':
            self.rotation = 'v'
        else:
            self.rotation = 'h'

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

    
    def draw_confirm_button(self):
        self.confirm_button.draw(self.screen)
        if self.confirm_button.but_rect.collidepoint(pygame.mouse.get_pos()):
            self.confirm_button.color = self.confirm_button_hover_color
        else:
            self.confirm_button.color = self.confirm_button_color 
    
    def draw_title_text(self):
        self.screen.blit(self.title_text, self.text_rect)

    def draw_title_background(self):
        pygame.draw.rect(self.screen, self.title_bg_color, self.title_bg_rectangle)

    def draw_ship_placement(self):
        pygame.draw.rect(self.screen,(0,0,0),
                         pygame.Rect(self.ships_placement_x-5, self.ships_placement_y-5, self.ships_placement_width+10, self.ships_placement_height+10))
        pygame.draw.rect(self.screen,self.ships_placement,self.ships_placement_rectangle)
    
    # def prepare_board(self, game_board, tile_size, hide_ships=False):
    #     tile_border_size = 1

    #     # Ustaw pozycję planszy w oknie gry
    #     start_x = 125
    #     start_y = 250

    #     for row in range(self.game_board_rows):
    #         for col in range(self.game_board_cols):
    #             marker_color = (255, 255, 255)

    #             #Pozycja myszy
    #             mouse_x, mouse_y = pygame.mouse.get_pos()

    #             mouse_x -= start_x
    #             mouse_y -= start_y

    #             rect = pygame.Rect(
    #                 row * tile_size + tile_border_size,
    #                 col * tile_size + tile_border_size,
    #                 tile_size - 2 * tile_border_size,
    #                 tile_size - 2 * tile_border_size)

    #             #Mysz nad kwadratem - hover efekt
    #             if rect.collidepoint(mouse_x, mouse_y) and self.board_content[row][col] == ' ':
    #                 marker_color = (200, 200, 200)
                    

    #             pygame.draw.rect(board, self.tile_color_border,
    #                              (row * tile_size, col * tile_size, tile_size, tile_size))

    #             pygame.draw.rect(board, marker_color, (
    #                 row * tile_size + tile_border_size, col * tile_size + tile_border_size,
    #                 tile_size - 2 * tile_border_size,
    #                 tile_size - 2 * tile_border_size))
        # return board
    def prepare_board(self, game_board, tile_size, hide_ships=False):
        tile_border_size = 1
        board = pygame.Surface(
            (tile_size * self.game_board_cols + 4 * tile_border_size,
             tile_size * self.game_board_rows + 4 * tile_border_size))
        

        # Ustaw pozycję planszy w oknie gry
        start_x = 125
        start_y = 250

        for row in range(self.game_board_rows):
            for col in range(self.game_board_cols):
                marker_color = (255, 255, 255)

                #Pozycja myszy
                # mouse_x, mouse_y = pygame.mouse.get_pos()

                # mouse_x -= start_x
                # mouse_y -= start_y

                rect = pygame.Rect(
                    row * tile_size + tile_border_size + start_x,
                    col * tile_size + tile_border_size + start_y,
                    tile_size - 2 * tile_border_size,
                    tile_size - 2 * tile_border_size)
                self.board_rect[row][col] = rect

                #Mysz nad kwadratem - hover efekt
                if rect.collidepoint(pygame.mouse.get_pos()) and self.board_content[row][col] == ' ':
                    marker_color = (200, 200, 200)
                elif self.board_content[row][col] == 'S':
                    marker_color = self.tile_color_ship

                pygame.draw.rect(board, self.tile_color_border,
                                 (row * tile_size, col * tile_size, tile_size, tile_size))

                pygame.draw.rect(board, marker_color, (
                    row * tile_size + tile_border_size, col * tile_size + tile_border_size,
                    tile_size - 2 * tile_border_size,
                    tile_size - 2 * tile_border_size))
        return board

    def draw_axis_description(self, tile_size, start_x, start_y):
        text_color = (12, 13, 13)
        font_size = 30
        offset = 15
        total_space = tile_size * self.game_board_cols

        font = pygame.font.SysFont("monospace", font_size, bold=True)

        for row in range(self.game_board_rows):
            text = font.render(chr(row + 65), 1, text_color)
            self.screen.blit(text, (start_x - tile_size, start_y + row * tile_size + offset))


        for col in range(self.game_board_cols):
            text = font.render(str(col + 1), 1, text_color)
            self.screen.blit(text, (start_x + col * tile_size + offset, start_y - tile_size))


    def draw_boards(self):
        start_x = 125
        start_y = 250

        # rows == columns
        tile_size = 650 // self.game_board_rows

        self.draw_axis_description(tile_size, start_x, start_y)

        self.board = self.prepare_board(self.game_board_1, tile_size)

        self.screen.blit(self.board, (start_x, start_y))


    def draw_bottom_ui(self):
        pygame.draw.rect(self.screen, self.bottom_ui_bg_color,
                         (self.bottom_ui_bg_x, self.bottom_ui_bg_y, self.bottom_ui_bg_width, self.bottom_ui_bg_height))

    def draw_numberships(self):
        for i,butship in enumerate(self.but_show_ship):
            if (butship.but_rect.collidepoint(pygame.mouse.get_pos())):
                butship.color = self.tile_color_hover
            else:
                butship.color = self.tile_color
            butship.draw(self.screen)
            count = "x" + str(self.tab_number_of_ship[i])
            text = self.my_font.render(count, 1, self.title_text_color)
            self.screen.blit(text,(self.ships_placement_x + 50 + i *(self.tile_size + 100),
                self.ships_placement_y + 50))
            
    def place_ship_on_board(self,x,y):
        
        ship_len = self.chosen_ship + 1
        r_max = self.game_board_rows
        c_max = self.game_board_cols

        rotation = self.rotation
        r = x
        c = y

        possible_to_place = True
        
        if rotation == "h":
            c_max -= ship_len
        else:
            r_max -= ship_len
        if self.board_content[r][c] == " ":
            if rotation == "v" and c+ship_len<=c_max:
                for j in range(ship_len):
                    if self.board_content[r][c + j] != " ":
                        possible_to_place = False
                        break
            elif rotation == "h" and r+ship_len<=r_max:
                for j in range(ship_len):
                    if self.board_content[r + j][c] != " ":
                        possible_to_place = False
                        break
            else:
                possible_to_place = False
        else:
            possible_to_place = False
        # mark adjacent fields
        if possible_to_place:
            if rotation == "v":
                for j in range(-1, ship_len + 1):
                    if 0 <= c + j < self.game_board_cols:
                        self.board_content[r][c + j] = "."
                        if r + 1 < self.game_board_rows:
                            self.board_content[r + 1][c + j] = "."
                        if r - 1 >= 0:
                            self.board_content[r - 1][c + j] = "."
            else:
                for j in range(-1, ship_len + 1):
                    if 0 <= r + j < self.game_board_rows:
                        self.board_content[r + j][c] = "."
                        if c + 1 < self.game_board_cols:
                            self.board_content[r + j][c + 1] = "."
                        if c - 1 >= 0:
                            self.board_content[r + j][c - 1] = "."

        # put ship
        if possible_to_place:
            if rotation == "v":
                for j in range(ship_len):
                    self.board_content[r][c + j] = "S"
            else:
                for j in range(ship_len):
                    self.board_content[r + j][c] = "S"
            self.tab_number_of_ship[self.chosen_ship] -=1
 
    def clear_empty_on_board(self):
        for r in range(self.game_board_rows):
            for c in range(self.game_board_cols):
                if self.board_content[r][c] == ".":
                    self.board_content[r][c] = " "
    def use_draw(self):
        self.draw_title_background()
        self.draw_title_text()
        self.draw_boards()
        self.draw_bottom_ui()
        self.draw_ship_placement()
        self.draw_confirm_button()
        self.draw_settings_button()
        self.draw_exit_button()
        self.draw_numberships()
