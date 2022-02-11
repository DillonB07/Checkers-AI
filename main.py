import pygame

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE

from checkers.game import Game

from minimax.algorithm import minimax

import os

pygame.init()

FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')


def clear():

    # Check if Operating System is Mac and Linux or Windows

    _ = os.system('clear') if os.name == 'posix' else os.system('cls')


def get_row_col_from_mouse(pos):

    x, y = pos

    row = y // SQUARE_SIZE

    col = x // SQUARE_SIZE

    return row, col


def get_difficulty():

    try:

        difficulty = int(input(

            'Please enter how difficult you would like the AI to be. 1 is easy, and the larger the number, the harder the AI.\nFor safety reasons, the AI is capped at level 7: '))

        if difficulty == 0:

            print('Sorry, you can\'t use 0 as a level.')

            get_difficulty()

        elif difficulty > 7:

            confirm = input(

                f'Are you sure you want the AI to use level {difficulty}?\nGoing above level 7 may take a long time for the AI to decide, and put stress on your CPU. (y/N): ')

            if confirm == 'y':

                confirm = input(
                    'WARNING:\nAre you sure you want to proced?\nDoing this may take a long time for the AI to decide, and put stress on your CPU. (y/N): '
                )


                if confirm == 'y':

                    confirm = input(

                        f'CONFIRMATION:\nAre you sure you want to proceed with difficulty {difficulty}?\nThis could damage your CPU, or crash your computer. (y/N): ')

                    if confirm == 'y':

                        return difficulty

                    else:
                        get_difficulty()

                else:
                    get_difficulty()

            else:
                get_difficulty()

        return difficulty

    except Exception as e:

        print('That is not a possible difficulty level.')

        get_difficulty()


def cheats():

    try:

        cheats = int(input(

            'Please enter 1 for seeing possible moves and 2 for not seeing possible moves. '))

        if cheats == 1:

            cheat = True

        elif cheats == 2:

            cheat = False

        else:

            print('Sorry, that is not a valid option.')

            cheats()

        return cheat

    except Exception as e:
        cheats()


def main(difficulty, cheat):

    run = True

    clock = pygame.time.Clock()

    game = Game(WIN)

    while run:

        clock.tick(FPS)

        if game.turn == WHITE:

            value, new_board = minimax(

                game.get_board(), difficulty, WHITE, game)

            game.ai_move(new_board)

        if game.winner() != None:

            if game.winner() == RED:

                print('\n\n\nRed wins!')

            elif game.winner() == WHITE:

                print('\n\n\nWhite wins!')

            print(game.winner())

            run = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                row, col = get_row_col_from_mouse(pos)

                game.select(row, col)

        game.update(cheat)

    pygame.quit()


clear()

difficulty = get_difficulty()

cheat = cheats()

clear()

main(difficulty, cheat)
