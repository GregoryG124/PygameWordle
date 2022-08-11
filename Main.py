from Class import *
import random

running = True
user_word = ''
guesses = 0
color = 'gray'
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption('Wordle')
font = pygame.font.Font('freesansbold.ttf', 32)
list_of_letter_containers = []
score = 0


def main():
    reset_screen()
    word_to_guess = assign_word().lower()
    global running, color, user_word, guesses, score
    while running:  # The game loop that keeps updates the screen and keeps track of game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT or pygame.K_LSHIFT:
                    pass
                if len(user_word) < 5 and chr(event.key).isalpha():
                    user_word += (chr(event.key))
                if event.key == pygame.K_BACKSPACE:
                    user_word = user_word[:-1]
                if event.key == pygame.K_RETURN and len(user_word) == 5:
                    correct_letters = check_word(user_word, word_to_guess)  # rewrite as function
                    for i in range(0, 5):
                        if correct_letters[i] == 'C':
                            list_of_letter_containers[i * 6 + guesses].draw_letter_container('Green', screen)
                        if correct_letters[i] == 'I':
                            list_of_letter_containers[i * 6 + guesses].draw_letter_container('Yellow', screen)
                        if correct_letters[i] == 'X':
                            list_of_letter_containers[i * 6 + guesses].draw_letter_container('Red', screen)
                        UserLetters(list_of_letter_containers[i * 6 + guesses].location, user_word[i],
                                    font, 'Black').print_letter(screen)
                    guesses += 1
                    user_word = ''
                    if correct_letters == ['C', 'C', 'C', 'C', 'C']:
                        reset_screen()
                        score += int(100 / guesses)
                        guesses = 0
                        word_to_guess = assign_word()
                        LetterContainer((300, 30), (100, 32)).draw_letter_container('Black', screen)
                        UserLetters((300, 30), str(score), font, 'White').print_letter(screen)
                    if guesses > 5:
                        print(word_to_guess)
                        reset_screen()
                        guesses = 0
                        word_to_guess = assign_word()

        final_index = 0
        for index, letter in enumerate(user_word):
            UserLetters(list_of_letter_containers[-5 + index].location, letter, font, 'Black').print_letter(screen)
            final_index = index + 1
        if final_index < 5:
            for i in list_of_letter_containers[-5 + final_index:]:
                i.draw_letter_container('white', screen)

        pygame.display.update()
        FPS.tick(60)


def reset_screen():
    for x in range(0, 5):
        for y in range(0, 6):
            list_of_letter_containers.append(LetterContainer((x * 38, y * 38), (32, 32)))
    for x in range(0, 5):
        list_of_letter_containers.append(LetterContainer((x * 38, 400), (32, 32)))
    for item in list_of_letter_containers[0:-5]:
        item.draw_letter_container('gray', screen)
    for item in list_of_letter_containers[-5:]:
        item.draw_letter_container('white', screen)


def assign_word():
    with open('Words') as file:
        word_list = file.read().splitlines()
    return random.choice(word_list)


def check_word(user_guess, answer):
    correct_letters = []
    letter_counter = {}
    for letter in answer:
        if letter in letter_counter.keys():
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    for index, letter in enumerate(user_guess):
        if letter == answer[index]:
            correct_letters.append('C')
            letter_counter[user_guess[index]] -= 1
        else:
            correct_letters.append('W')

    for index, letter in enumerate(user_guess):
        if correct_letters[index] == 'W' and letter in answer and letter_counter[letter] > 0:
            correct_letters[index] = 'I'
            letter_counter[letter] -= 1
        elif correct_letters[index] == 'W':
            correct_letters[index] = 'X'

    return correct_letters


if __name__ == '__main__':
    main()
