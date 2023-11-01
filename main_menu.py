import pygame
import Pygame_Util as pu
from pygame import mixer

pygame.init()
pygame.mixer.init()
mixer.music.load('startButton.mp3')
mixer.music.set_volume(1)

# Screen settings
SCREEN_WIDTH = 1620
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battleships: Battle in Progress")

# Colors
background_color = (0, 192, 255)  # Turquoise
button_color = (255, 0, 0)  # Red
button_text_color = (255, 255, 255)  # White

# Fonts
title_font_size = 50
button_font_size = 40
title_font = pygame.font.SysFont("Comics Sans", title_font_size, bold=True)
font = pygame.font.SysFont("Comics Sans", button_font_size, bold=True)

# Menu buttons
menu_buttons = [
    {"text": "Start Game", "function": "start_game"},
    {"text": "Options", "function": "options"},
    {"text": "Scoreboard", "function": "scoreboard"},
    {"text": "Quit", "function": "quit_game"}
]

# Function to draw the game interface
def draw_main_menu():
    screen.fill(background_color)

     # Draw title
    title_text = pygame.font.SysFont("monospace", title_font_size, bold=True)
    title_text = title_text.render("Battleships", 1, button_text_color)
    title_x = (SCREEN_WIDTH - title_text.get_width()) // 2
    title_y = 50  # Adjust the vertical position of the title
    screen.blit(title_text, (title_x, title_y))

    # Draw buttons
    button_height = 100
    button_spacing = 40
    total_button_height = (button_height + button_spacing) * len(menu_buttons)
    button_y = (SCREEN_HEIGHT - total_button_height) // 2

    for button in menu_buttons:
        button_text = font.render(button["text"], 1, button_text_color)
        button_width = button_text.get_width() + 20
        button_x = (SCREEN_WIDTH - button_width) // 2


        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect, border_radius=20)

        text_x = button_rect.centerx - button_text.get_width() // 2
        text_y = button_rect.centery - button_text.get_height() // 2

        screen.blit(button_text, (text_x, text_y))

        button_y += button_height + button_spacing

    pygame.display.update()

# Function to start a new game
def start_game():
    # Call the code from the previous program, e.g., the function draw_boards()
    #draw_boards()
    mixer.music.play()
    pygame.time.delay(1200)
    pygame.quit()
    quit()
    

# Function to display options
def options():
    # Call the code from the previous program, e.g., the function Custom_page_draw()
    #Custom_page_draw()
    mixer.music.play()
    pygame.time.delay(1200)
    pygame.quit()
    quit()

# Function to quit the game
def quit_game():
    mixer.music.play()
    pygame.time.delay(1200)
    pygame.quit()
    quit()

def scoreboard():
    mixer.music.play()
    pygame.time.delay(1200)
    pygame.quit()
    quit()

# Main game loop
run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for i, button in enumerate(menu_buttons):
                    button_width = font.render(button["text"], 1, button_text_color).get_width() + 20
                    button_height = 100
                    button_spacing = 40
                    button_x = (SCREEN_WIDTH - button_width) // 2
                    button_y = (SCREEN_HEIGHT - ((button_height + button_spacing) * len(menu_buttons))) // 2 + (
                            i * (button_height + button_spacing))

                    if button_x < event.pos[0] < button_x + button_width and \
                            button_y < event.pos[1] < button_y + button_height:
                        if button["function"] == "start_game":
                            start_game()
                        elif button["function"] == "options":
                            options()
                        elif button["function"] == "scoreboard":
                            scoreboard()
                        elif button["function"] == "quit_game":
                            quit_game()

    draw_main_menu()
    pygame.display.update()
    clock.tick(30)

pygame.quit()


