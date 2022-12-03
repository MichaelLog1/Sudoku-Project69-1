import pygame
from sudoku_generator import *
from constants import *
import sys

#draws the game start screen
def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    start_rules_font = pygame.font.Font(None, 50)

    button_font = pygame.font.Font(None, 50)
    # Color background
    screen.fill(BG_COLOR)
    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 190))
    screen.blit(title_surface, title_rectangle)

    rules1_surface = start_rules_font.render("Press Space to start over.", 0, LINE_COLOR)
    rules1_rectangle = rules1_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 85))
    screen.blit(rules1_surface, rules1_rectangle)

    rules2_surface = start_rules_font.render("Press R to to reset board.", 0, LINE_COLOR)
    rules2_rectangle = rules2_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 135))
    screen.blit(rules2_surface, rules2_rectangle)

    rules3_surface = start_rules_font.render("Press Q to quit.", 0, LINE_COLOR)
    rules3_rectangle = rules3_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 35))
    screen.blit(rules3_surface, rules3_rectangle)



    # Initialize buttons
    # Initialize text first

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    med_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(LINE_COLOR)
    med_surface.blit(med_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    med_rectangle = med_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))   
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        #returns correct difficulty level to sudoku generator
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif med_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50

        pygame.display.update()    

#draws the game over screen 
def draw_game_over(win_state, screen):
    font = pygame.font.Font(None, GAME_OVER_FONT)
    screen.fill(BG_COLOR)
    # tells you if you won
    if win_state == 1:
        end_text = "You correctly solved it!"
    elif win_state == 0:
        end_text = "Incorrect solution!"
    end_surf = font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)
    restart_text = "Press space to play the game again..."
    restart_surf = font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2,
                                                 HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)