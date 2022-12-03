import pygame
from constants import *
from board import Board
from cell import Cell
from game_states import draw_game_start, draw_game_over
from sudoku_generator import SudokuGenerator, generate_sudoku
import copy
import sys


#initialize game stats
pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
difficulty = draw_game_start(screen)
board = Board(WIDTH, HEIGHT, screen, difficulty)
original_cells = copy.deepcopy(board.original_cells())
screen.fill(BG_COLOR)
board.draw()
entered = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  # gives the position of the mouse
            row, col = board.click(x, y)  # x = row y = col
            curr_cell = board.select(row, col)
            board.draw()
            board.draw_select(curr_cell) #draws square around each box if selected

        if event.type == pygame.KEYDOWN:
            board.draw()
            #board.draw_select(curr_cell)
            pygame.display.update()
            # gets the keyboard number input
            if event.key == pygame.K_1:
                value = 1
                entered = True
            if event.key == pygame.K_2:
                value = 2
                entered = True
            if event.key == pygame.K_3:
                value = 3
                entered = True
            if event.key == pygame.K_4:
                value = 4
                entered = True
            if event.key == pygame.K_5:
                value = 5
                entered = True
            if event.key == pygame.K_6:
                value = 6
                entered = True
            if event.key == pygame.K_7:
                value = 7
                entered = True
            if event.key == pygame.K_8:
                value = 8
                entered = True
            if event.key == pygame.K_9:
                value = 9
                entered = True

            #checks if a key has been pressed, and there is not already a number in the box, and then updates box with number the player selected
            if entered == True:
                if curr_cell.value == 0:
                    board.place_number(value, curr_cell)
                    board.draw()
                    board.draw_select(curr_cell)
                    pygame.display.update()

            if event.key == pygame.K_BACKSPACE: #removes number from currently selected cell
                if curr_cell.value != 0:
                    cell_row = curr_cell.row
                    cell_column = curr_cell.col
                    if original_cells[cell_row][cell_column] == 0:
                        board.clear(curr_cell)
                        screen.fill(BG_COLOR)
                        board.draw()
                        board.draw_select(curr_cell)
                        pygame.display.update()

            if event.key == pygame.K_r: #resets board to original numbers
                board.reset_to_original(original_cells)
                screen.fill(BG_COLOR)
                board.draw()
                pygame.display.update()

            if board.is_full(): #checks if board is full
                #checks if board is correctly completed
                if board.solved_correct():
                    draw_game_over(1, screen)
                else:
                    draw_game_over(0, screen)

            if event.key == pygame.K_SPACE: #returns user to start screen and initializes new game
                difficulty = draw_game_start(screen)
                board = Board(WIDTH, HEIGHT, screen, difficulty)
                original_cells = copy.deepcopy(board.original_cells())
                screen.fill(BG_COLOR)
                board.draw()

            if event.key == pygame.K_q:
                sys.exit()

    pygame.display.update()
