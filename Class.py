import pygame

pygame.init()


class LetterContainer:
    def __init__(self, location, size):
        self.size = size
        self.surface = pygame.Surface(self.size)
        self.location = location

    def draw_letter_container(self, letter_container_color, screen):
        self.surface.fill(letter_container_color)
        screen.blit(self.surface, self.location)


class UserLetters:
    def __init__(self, location, letter, font, color):
        self.letter = font.render(letter, True, color)
        self.location = location
        self.letter_rect = self.letter.get_rect()

    def print_letter(self, screen):
        screen.blit(self.letter, self.location)
