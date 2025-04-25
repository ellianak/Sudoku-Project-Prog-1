import pygame, sys
from sudoku_generator import *
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
    pygame.display.update()

    while True:
        for event in pygame.event.get(): #quits program if they exit out window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # game_run = Board(9,9,screen,"easy")
                    # return generate_sudoku(81, 30)  #do i put backtracking here?
                    difficulty = "easy"
                    return difficulty
                elif medium_rectangle.collidepoint(event.pos):
                    # game_run = Board(9, 9, screen, "medium")
                    # return generate_sudoku(81,40)
                    difficulty = "medium"
                    return difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    # game_run = Board(9, 9, screen, "hard")
                    # return generate_sudoku(81, 50)
                    difficulty = "hard"
                    return difficulty


#game end screens:
#game over :( loser
def game_over_screen(screen):
    while True:
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
        pygame.display.update()

#game won YIPPPEE
def game_won(screen):
    while True:
        title_font = pygame.font.SysFont('Arial', 100)
        button_font = pygame.font.SysFont('Arial', 40)
        screen.fill("pink")
        title_surface = title_font.render("Game Won!", 0, text_color)
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
        pygame.display.update()



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

        #clears a cell, adds flexibility if you wanna reset a cell during gameplay
    def clear(self):
        self.value = 0
        self.sketched_value = None

    def draw(self):
        x = (self.col * 60) + 30
        y = (self.row * 60) + 30

        #creates the font
        cell_font = pygame.font.SysFont('Arial', 20)

        if self.sketched_value:
            cell_write = cell_font.render(str(self.sketched_value), True, "gray") #gray color for sketched value
        else:
            if self.value != 0:
                cell_write = cell_font.render(str(self.value), True, "white")
            else:
                return
            # cell_write = cell_font.render(str(self.value), True, "white") # white for the actually true value
        # screen.blit(cell_write, (x, y))
        # make the number a rectangle, set the top left of the rectangle to the top left of the cell (which are 60x60 pixels big)
        self.screen.blit(cell_write, cell_write.get_rect(center=(x, y)))

        pygame.draw.rect(self.screen, "white", (self.col * 60, self.row * 60, 60, 60), 1)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if self.difficulty == "easy":
            remove = 30
        elif self.difficulty == "medium":
            remove = 40
        else:
            remove = 50

        self.board = generate_sudoku(9, remove)
        self.og_board = self.board.copy()
        self.instance = SudokuGenerator(9, remove)

        # makes a list of instances of the Cell class, these are what clear, sketch, and place_number should use
        self.cells = []
        for row in range(0,len(self.board)):
            for col in range(0, len(self.board[row])):
                self.cells.append(Cell(self.board[row][col], row, col, self.screen))

        """This code might make sense, but rn im about to leave, and dont wanna make more errors :("""
        # self.cells = [[None for _ in range(9)] for _ in range(9)] # a 9x9 grid of cells
        # self.selected = None   # stores the currently selected cell (row, col)


        #This initializes the 81 cells in the coard (implementing cell class for the structure to be better
        # for row in range(9):
        #     for col in range(9):
        #         self.cells[row][col] = Cell(row, col)


    def draw(self):
        while True:
            for i in range(9):
                pygame.draw.line(self.screen, 'white',(60+i*60,0),(60+i*60, 540))
            for i in range(9):
                pygame.draw.line(self.screen, 'white',(0,60+i*60),(540,60+i*60))
            for i in range(4):
                pygame.draw.line(self.screen, 'white', (0, i*180), (540, i*180), 5)
            for i in range(4):
                pygame.draw.line(self.screen, 'white', (i*180, 0), (i*180,540), 5)
# draws cell values
            for cell in self.cells:
                cell.draw()

            button_font = pygame.font.SysFont('Arial', 30)
            #exit stuff
            exit_text = button_font.render("Exit", 0, 'black')
            exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
            exit_surface.fill('white')
            exit_surface.blit(exit_text, (10, 10))
            exit_rect = exit_surface.get_rect(
                center=(1* screen_width // 4, screen_height // 2 + 275)
            )
            self.screen.blit(exit_surface, exit_rect)
            #restart stuff:
            exit_text = button_font.render("Restart", 0, 'black')
            exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
            exit_surface.fill('white')
            exit_surface.blit(exit_text, (10, 10))
            exit_rect = exit_surface.get_rect(
                center=(2* screen_width // 4, screen_height // 2 + 275)
            )
            self.screen.blit(exit_surface, exit_rect)
            #reset stuff
            exit_text = button_font.render("Return", 0, 'black')
            exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
            exit_surface.fill('white')
            exit_surface.blit(exit_text, (10, 10))
            exit_rect = exit_surface.get_rect(
                center=(3*screen_width // 4, screen_height // 2 + 275)
            )
            self.screen.blit(exit_surface, exit_rect)

            pygame.display.update()

    def select(self, row, col):
        self.selected = (row, col) # marks the cell as a selected cell
        # this function should also highlight the cell red. Elyse this is you

    """Returns the tuple of the cell that's clicked based on (X,Y)
           Cordinates"""
    def click(self, x, y):
        if x < 0 or x > 540 or y < 0 or y > 540:
            return None
        row = y // 60
        col = x // 60
        return row, col


    def clear(self):
        if self.selected:
            row, col = self.selected
            if self.cells[row][col] != self.og_board[row][col]:
                self.cells[row][col].clear()


    def sketch(self, value):
        if self.selected:
            row, col = self.selected
            if self.cells[row][col] != self.og_board[row][col]:
                self.cells[row][col].draw()


    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            if self.board[row][col] != self.og_board[row][col]:
                self.board[row][col] = value

    def reset_to_original(self):
        self.board = self.og_board
        # for row in self.board:
        #     for col in self.board[row]:
        #         self.cells = []
        #         self.cells.append(Cell(self.board[row][col], row, col, self.screen))
        for row in range(0,len(self.board)):
            for col in range(0, len(self.board[row])):
                self.cells.append(Cell(self.board[row][col], row, col, self.screen))

    def is_full(self):
        if 0 in self.board:
            return False
        return True

    # def update_board(self):
    #
    # def find_empty(self):
    #
    def check_board(self):
        if self.instance.fill_remaining:
            return True
        return False
#PUSHIT
class Boxy:
    def __init__(self, x, y, speed, color, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.size = size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
    def render(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
    def up(self):
        self.y = self.y - self.speed
    def down(self):
        self.y = self.y + self.speed
    def left(self):
        self.x = self.x - self.speed
    def right(self):
        self.x = self.x + self.speed



def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sudoku Board :)")
    screen.fill(bg_color)
    game_over = False

    box = Boxy(60, 60, 25,(255,0,0), 25)

    while True:
        for event in pygame.event.get(): #quits program if they exit out window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_UP]:
            box.up()
        if key_pressed[pygame.K_DOWN]:
            box.down()
        if key_pressed[pygame.K_LEFT]:
            box.left()
        if key_pressed[pygame.K_RIGHT]:
            box.right()

        draw_game_start(screen)
        difficulty = draw_game_start(screen)
        game_run = Board(9,9,screen,difficulty)
        screen.fill("black")
        # key_pressed = pygame.key.get_pressed()
        #
        # if key_pressed[pygame.K_UP]:
        #     box.up()
        # if key_pressed[pygame.K_DOWN]:
        #     box.down()
        # if key_pressed[pygame.K_LEFT]:
        #     box.left()
        # if key_pressed[pygame.K_RIGHT]:
        #     box.right()

        box.render()
        game_run.draw()

        pygame.display.flip()
        # board.draw()
    # game_won(screen)
# board.draw()
main()
