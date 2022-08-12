import pygame

pygame.init()


class LetterContainer:  # these are all the squares that are presented on the game board
    def __init__(self, location : tuple, size  : tuple):
        self.size = size
        self.surface = pygame.Surface(self.size)
        self.location = location

    def draw_letter_container(self, letter_container_color : str, screen : object):  # method to draw the letter container to the screen
        self.surface.fill(letter_container_color)
        screen.blit(self.surface, self.location)


class UserLetters:  # the text objects that will be drawn to the screen when called apon
    def __init__(self, location : tuple, letter : str, font : object, color : str):
        self.letter = font.render(letter, True, color)
        self.location = location
        self.letter_rect = self.letter.get_rect()

    def print_letter(self, screen : object):  # draws the letter to the screen
        screen.blit(self.letter, self.location)
