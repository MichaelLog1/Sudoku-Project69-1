import pygame
from sudoku_generator import *
from constants import *
from cell import Cell
import sys

class Board: 
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.board = generate_sudoku(BOARD_ROWS, difficulty)
    self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(9)]
    for i in range(9)]

  #used in beginning to validate user input when trying to remove data
  def original_cells(self):
    return self.board

    #draws board on screen
  def draw(self):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for j in range(1, BOARD_COLS):
        pygame.draw.line(self.screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, WIDTH), LINE_WIDTH)
    for i in [0,3,6,9]:
        pygame.draw.line(self.screen, BOX_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), BOX_WIDTH)
    for j in [0,3,6,9]:
        pygame.draw.line(self.screen, BOX_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, WIDTH), BOX_WIDTH)
    

          #draw cells
    for i in range(9):
        for j in range(9):
            self.cells[i][j].draw()

#selects a cell based on user input
  def select(self, row, col):
    for i in self.cells:
      for j in i:
        if j.row == row and j.col == col:
          return j
          
#gets row and column of a cell the user wants to change
  def click(self, x, y):
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

#clears cell value when user enters backspace
  def clear(self, curr_cell):
    curr_cell.value = 0
  
#changes value based on user input
  def place_number(self, value, curr_cell):
    curr_cell.value = value

#draws a circle around box that user selected
  def draw_select(self, curr_cell):
    row = curr_cell.row
    col = curr_cell.col
    x = row * SQUARE_SIZE
    y = col * SQUARE_SIZE
    select_rect = pygame.Rect(y, x, SQUARE_SIZE + 2, SQUARE_SIZE + 2)
    pygame.draw.rect(self.screen, SELECT_COLOR, select_rect,  2)
  
  #resets game to original state
  def reset_to_original(self, original_list):   
    for index, item in enumerate(self.cells):
      for index1, item1, in enumerate(item):
        item1.value = original_list[index][index1]


  def is_full(self): # checks if board full
    count = 0
    for i in self.cells:
      for j in i:
        if j.value != 0:
          count += 1
    if count == 81:
      return True
    return False  


#the next 3 methods are used to check if the board is solved correctly
  @staticmethod
  def solved_correct_row(solved_list):
    # checks rows
    for i in solved_list:
      test_set = set()
      for j in i:
        test_set.add(j)
      if len(test_set) < 9:
        return False
    return True

  @staticmethod
  def solved_correct_col(solved_list):
    for i in range(9):
      test_set = set()
      for j in range(9):
        test_set.add(solved_list[j][i])
      if len(test_set) < 9:
        return False
    return True
    
  @staticmethod
  def solved_box(solved_list):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box_set = set()
            for i in range(3):
                for j in range(3):
                    box_set.add(solved_list[box_row + i][box_col + j])
            if len(box_set) < 9:
              return False
    return True

#uses the last 3 methods together to determine if the board is solved correctly
  def solved_correct(self):
    solved_list = []
    for i in self.cells:
      sublist = []
      for j in i:
        sublist.append(j.value)
      solved_list.append(sublist)
    if self.solved_correct_row(solved_list) and self.solved_correct_col(solved_list) and self.solved_box(solved_list):
        return True
    return False
    