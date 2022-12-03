import pygame
from sudoku_generator import *
from constants import *
import sys

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen


  def set_cell_value(self, value):
    self.value = value
    
#draws the cell
  def draw(self):
      #1. define a surface, #2. define location of text
    num_font = pygame.font.Font(None, NUM_FONT)
    
    if self.value != 0:
      num_surf = num_font.render(str(self.value), 0, NUM_COLOR)
      num_rect = num_surf.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      self.screen.blit(num_surf, num_rect)