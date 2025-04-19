import pygame, sys
from sudoku_generator import *
from extra_classes import *
#Im starting to work on user interface stuff
#pray pookie
#definining variables that will be necessary!!!

# cells are 60x60
# screen size is 540x600

screen_height = 600
screen_width = 540
num_rows = 9
text_color = (0,0,0) #"black"
line_color = (128, 0, 128) #"purple"
line_width = 15
win_line_width = 15
board_rows = 3
board_cols = 3
square_size = 200
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55
red = (255, 0, 0)
bg_color = (255, 255, 245)
circle_color = (155, 155, 155)
cross_color = (66, 66, 66)
chip_font = 400
game_over_font = 40




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

    while True:
        for event in pygame.event.get(): #quits program if they exit out window
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    generate_sudoku(81, 30)  #do i put backtracking here?
                    Board(9,9,screen,easy)
                    Board.draw(screen)
                elif medium_rectangle.collidepoint(event.pos):
                    generate_sudoku(81,40)
                    Board(9,9,screen,medium)
                    Board.draw(screen)
                elif hard_rectangle.collidepoint(event.pos):
                    generate_sudoku(81, 50)
                    Board(9,9,screen,hard)
                    Board.draw(screen)
            while event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos): #restart button must be initialized outside of game_over
                    break
                elif reset_rect.collidepoint(event.pos):#add when reset button is made
                    #connected to Board class
                    Board.draw(screen)  #not sure about this
                elif exit_rect.collidepoint(event.pos):
                    sys.exit()
                #elif a cell is pressed:
                    # call is_valid()  #check what False means in context
                    num = int(input("Enter number: "))
                    #use Cell class to fill in number and value
            pygame.display.update()

#game end screens:
#game over :( loser
def game_over_screen(screen):
    title_font = pygame.font.SysFont('Arial', 100)
    button_font = pygame.font.SysFont('Arial', 40)
    #
    screen.fill("pink")
    #
    # #initialize and draw title
    title_surface = title_font.render("Game Over", 0, text_color)
    title_rect = title_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 - 50)
    )
    screen.blit(title_surface, title_rect)
    #
    # #initialize but text
    restart_text = button_font.render("Restart", 0, text_color)

    # #button background box
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(line_color)
    restart_surface.blit(restart_text, (10, 10))

    # #initialize boxes shapes
    restart_rect = restart_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 + 100)
    )
    #
    # #draw restart button
    screen.blit(restart_surface, restart_rect)
    # while True:
    #     for event in pygame.event.get(): #quits program if they exit out window
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if restart_rect.collidepoint(event.pos):
    #                 return
    title_font = pygame.font.SysFont('Arial', 100)
    button_font = pygame.font.SysFont('Arial', 40)
    screen.fill("pink")
    title_surface = title_font.render("Game Over", 0, text_color)
    title_rect = title_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 - 50)
    )
    screen.blit(title_surface, title_rect)

    # initialize but text
    restart_text = button_font.render("Restart", 0, text_color)

    # button background box
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(line_color)
    restart_surface.blit(restart_text, (10, 10))

    # initialize boxes shapes
    restart_rect = restart_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 + 100)
    )

    # draw restart button
    screen.blit(restart_surface, restart_rect)


#game won YIPPPEE
def game_won(screen):
    title_font = pygame.font.SysFont('Arial', 100)
    button_font = pygame.font.SysFont('Arial', 40)
    screen.fill("pink")
    title_surface = title_font.render("Game Won", 0, text_color)
    title_rect = title_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 - 50)
    )
    screen.blit(title_surface, title_rect)

    # initialize but text
    exit_text = button_font.render("Exit", 0, text_color)

    # button background box
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(line_color)
    exit_surface.blit(exit_text, (10, 10))

    # initialize boxes shapes
    restart_rect = exit_surface.get_rect(
        center=(screen_width // 2, screen_height // 2 + 100)
    )

    # draw restart button
    screen.blit(exit_surface, restart_rect)

    #wow okie lets do this so NEXT
    #this loop will keep user in start page until they take action then act accordinly
    # while True:
    #     for event in pygame.event.get(): #quits program if they exit out window
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if restart_rect.collidepoint(event.pos):
    #                 return #need to make specified action so that we know how many boxes left open
    #             # elif medium_rectangle.collidepoint(event.pos):
    #             #     return #need to make specified action so that we know how many boxes left open
    #             # elif hard_rectangle.collidepoint(event.pos):
    #             #     return #need to make specified action so that we know how many boxes left open
    #         pygame.display.update()



def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sudoku Board :)")
    # draw_game_start(screen)
    Board.draw(screen)
    # game_over_screen(screen)

main()
