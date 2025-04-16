import pygame, sys
#Im starting to work on user interface stuff
#pray pookie
#definining variables that will be necessary!!!
screen_height = 600
screen_width = 600
num_rows = 9
text_color = (0,0,0) #"black"
line_color = (128, 0, 128) #"purple"



def draw_game_start(screen):
    start_title_font = pygame.font.SysFont('Arial', 100)
    button_font = pygame.font.SysFont('Arial', 40)

    screen.fill("pink")
    #initializing and 'drawing' title
    title_surface = start_title_font.render("Sudoku", 0, text_color)
    title_rect = title_surface.get_rect(
        center=(screen_width // 2, screen_height // 2-50)
    )
    screen.blit(title_surface, title_rect)
    # initializing text for our difficulty buttons
    easy_mode_text = button_font.render("Easy", 0, text_color)
    medium_mode_text = button_font.render("Medium", 0, text_color)
    hard_mode_text = button_font.render('Hard', 0, text_color
                                        )
    # Button background box shit
    easy_surface = pygame.Surface((easy_mode_text.get_size()[0] + 20, easy_mode_text.get_size()[1]+20))
    easy_surface.fill(line_color)
    easy_surface.blit(easy_mode_text, (10, 10))
    medium_surface = pygame.Surface((medium_mode_text.get_size()[0] + 20, medium_mode_text.get_size()[1]+20))
    medium_surface.fill(line_color)
    medium_surface.blit(medium_mode_text, (10, 10))
    hard_surface = pygame.Surface((hard_mode_text.get_size()[0] + 20, hard_mode_text.get_size()[1]+20))
    hard_surface.fill(line_color)
    hard_surface.blit(hard_mode_text, (10, 10))

    #initializing the button's rectangle shape
    easy_rectangle = easy_surface.get_rect(
        center=(1*(screen_width // 4), screen_height // 2+100)
    )
    medium_rectangle = medium_surface.get_rect(
        center=(2*(screen_width) // 4, screen_height // 2+100)

    )
    hard_rectangle = hard_surface.get_rect(
        center=(3*(screen_width // 4), screen_height // 2+100)
    )
    #drawing da buttons :3
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    #wow okie lets do this so NEXT
    #this loop will keep user in start page until they take action then act accordinly
    while True:
        for event in pygame.event.get(): #quits program if they exit out window
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return #need to make specified action so that we know how many boxes left open
                elif medium_rectangle.collidepoint(event.pos):
                    return #need to make specified action so that we know how many boxes left open
                elif hard_rectangle.collidepoint(event.pos):
                    return #need to make specified action so that we know how many boxes left open
            pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Board :)")

draw_game_start(screen)