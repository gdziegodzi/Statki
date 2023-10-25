import pygame 
import Pygame_Util as pu

pygame.display.set_caption('Statki') 

background_colour = (135,206,235) 
screen = pygame.display.set_mode((1920, 1080)) 
screen.fill(background_colour) 

BoardSize = []
Ships = [[],[],[],[]]

def Custom_page_draw():
    pygame.font.init()

    fonth1 = pygame.font.SysFont("arial.ttf", 70)
    fonth2 = pygame.font.SysFont("arial.ttf", 50)
    # fonth3 = pygame.font.SysFont("arial.ttf", 20)
    text = fonth1.render("Rozmiar planszy", False, (0,0,0))
    screen.blit(text, (100,50))

    #Ability overlay
    text = fonth1.render("Special ability", False, (0,0,0))
    screen.blit(text, (1200,300))
    text = fonth2.render("Coming soon", False, (0,0,0))
    screen.blit(text, (1250,400))

    #Board Button overlay 
    for x in range(0,4):
        BoardSize.append((pu.checkbox((110,0,0), 115 + (x*200), 120, 30, 30)))
        BoardSize[x].draw(screen)

    # but_tab.append(BoardSize1)


    #Board Text overlay 
    text = fonth2.render("9x9", False, (0,0,0))
    screen.blit(text, (100,150))
    text = fonth2.render("10x10", False, (0,0,0))
    screen.blit(text, (280,150))
    text = fonth2.render("11x11", False, (0,0,0))
    screen.blit(text, (485,150))
    text = fonth2.render("12x12", False, (0,0,0))
    screen.blit(text, (680,150))

    #Ships Text overlay

    text = fonth1.render("Ships", False, (0,0,0))
    screen.blit(text, (100,250))

    text = fonth2.render("Number of 1 block ship", False, (0,0,0))
    screen.blit(text, (130,320))
    text = fonth2.render("Number of 2 block ship", False, (0,0,0))
    screen.blit(text, (130,470))
    text = fonth2.render("Number of 3 block ship", False, (0,0,0))
    screen.blit(text, (130,620))
    text = fonth2.render("Number of 4 block ship", False, (0,0,0))
    screen.blit(text, (130,770))


    for j in range (0,4):
        for i in range (0,9):
            text = fonth2.render(str(i), False, (0,0,0))
            screen.blit(text, (135+(i*100),410+(j*150)))
    #Ships Button overlay 
            Ships[j].append((pu.checkbox((0,0,0), 130+(i*100), 380+(j*150), 30, 30)))
            Ships[j][i].draw(screen)


    # Update the display using flip 
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
Custom_page_draw()

while running: 

# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # with open("Page_test.py") as f:
            #     exec(f.read())
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for b in BoardSize:
                if b.isOver(pygame.mouse.get_pos()) == True:            
                    for p in BoardSize:
                        if p.isChecked():
                            p.convert(screen)
                    b.convert(screen)
                    pygame.display.flip()
            for s in Ships:
                for z in s:
                    if z.isOver(pygame.mouse.get_pos()) == True:
                        for d in s:
                            if d.isChecked():
                                d.convert(screen)
                        z.convert(screen)
                        pygame.display.flip()
    #Screen refresh
    # pygame.display.update()
    # clock.tick(30)