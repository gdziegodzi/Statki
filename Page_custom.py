import pygame 
import PygameUtils as pu

pygame.display.set_caption('Statki') 

background_colour = (135,206,235) 
screen = pygame.display.set_mode((1920, 1000)) 
screen.fill(background_colour) 

#Text overlay

pygame.font.init()
fonth1 = pygame.font.SysFont("arial.ttf", 70)
fonth2 = pygame.font.SysFont("arial.ttf", 50)
fonth3 = pygame.font.SysFont("arial.ttf", 20)
text = fonth1.render("Rozmiar planszy", False, (0,0,0))
screen.blit(text, (100,50))

text = fonth1.render("Special ability", False, (0,0,0))
screen.blit(text, (1200,300))


#Board Button overlay 
BoardSize1 = pu.checkbox((110,0,0), 115, 120, 30, 30)
BoardSize2 = pu.checkbox((110,0,0), 315, 120, 30, 30)
BoardSize3 = pu.checkbox((110,0,0), 515, 120, 30, 30)
BoardSize4 = pu.checkbox((110,0,0), 715, 120, 30, 30)

BoardSize1.draw(screen)
BoardSize2.draw(screen)
BoardSize3.draw(screen)
BoardSize4.draw(screen)

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
        Ships = pu.checkbox((0,0,0), 130+(i*100), 380+(j*150), 30, 30)
        Ships.draw(screen)

# shipOne1 = pu.checkbox((110,0,0), 150, 300, 75, 75)
# shipOne2 = pu.checkbox((110,0,0), 200, 300, 75, 75)
# shipOne3 = pu.checkbox((110,0,0), 200, 300, 75, 75)
# shipOne4 = pu.checkbox((110,0,0), 200, 300, 75, 75)

# shipTwo1 = pu.checkbox((110,0,0), 200, 300, 75, 75)
# shipTwo2 = pu.checkbox((110,0,0), 200, 300, 75, 75)
# shipTwo3 = pu.checkbox((110,0,0), 200, 300, 75, 75)
# shipTwo4 = pu.checkbox((110,0,0), 200, 300, 75, 75)

# shipThree1 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipThree2 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipThree3 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipThree4 = pu.checkbox((110,0,0), 200, 300, 100, 100)

# shipFour1 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipFour2 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipFour3 = pu.checkbox((110,0,0), 200, 300, 100, 100)
# shipFour4 = pu.checkbox((110,0,0), 200, 300, 100, 100)

# but.convert()
# but.draw(screen)

# but.convert()

# Update the display using flip 
pygame.display.flip() 

running = True
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        