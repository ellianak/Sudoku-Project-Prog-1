from sudoku_gui import *
from sudoku_generator import *
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
    def draw(self):
        for i in range(9):
            pygame.draw.line(screen, 'white',(60+i*60,0),(60+i*60, 540))
        for i in range(9):
            pygame.draw.line(screen, 'white',(0,60+i*60),(540,60+i*60))
        for i in range(4):
            pygame.draw.line(screen, 'white', (0, i*180), (540, i*180), 5)
        for i in range(4):
            pygame.draw.line(screen, 'white', (i*180, 0), (i*180,540), 5)
        button_font = pygame.font.SysFont('Arial', 30)
        #exit stuff
        exit_text = button_font.render("Exit", 0, 'black')
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill('white')
        exit_surface.blit(exit_text, (10, 10))
        exit_rect = exit_surface.get_rect(
            center=(1* screen_width // 4, screen_height // 2 + 275)
        )
        screen.blit(exit_surface, exit_rect)
        #restart stuff:
        exit_text = button_font.render("restart", 0, 'black')
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill('white')
        exit_surface.blit(exit_text, (10, 10))
        exit_rect = exit_surface.get_rect(
            center=(2* screen_width // 4, screen_height // 2 + 275)
        )
        screen.blit(exit_surface, exit_rect)
        #reset stuff
        exit_text = button_font.render("restart", 0, 'black')
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill('white')
        exit_surface.blit(exit_text, (10, 10))
        exit_rect = exit_surface.get_rect(
            center=(3*screen_width // 4, screen_height // 2 + 275)
        )
        screen.blit(exit_surface, exit_rect)
    #add method to determine mouse click




class Cell:
    def __init__(self, value, row, col, screen):
        self.sketched_value = None
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = (self.col * 60) + 30
        y = (self.row*60) + 30

        #creates the font
        cell_font = pygame.font.SysFont('Arial', 20)

        if cell.sketched_value:
            cell_write = cell_font.render(str(self.sketched_value), True, "gray") #gray color for sketched value
        else:
            cell_write = cell_font.render(str(self.value), True, "white") # white for the actually true value
        # screen.blit(cell_write, (x, y))
        # make the number a rectangle, set the top left of the rectangle to the top left of the cell (which are 60x60 pixels big)
        self.screen.blit(cell_write, cell_write.get_rect(center=(x, y)))
