import random

import click

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]


def computer_choice():
    player = random.randint(0, 2)
    second_computer = random.randint(0, 2)
    return player, second_computer


def interpretation(player, computer):
    if player == 0 and computer == 2:
        print('First player win!')
    elif computer == 0 and player == 2:
        print('Second player win!')
    elif player > computer:
        print('First player win!')
    elif computer > player:
        print('Second player win!')
    elif computer == player:
        print('It\'s a draw')
    print(f" First player", game_images[player], "Second player", game_images[computer])


@click.group
def cli():
    pass

@cli.command
def computer():
    while True:
        first_move = random.randint(0, 2)
        second_move = random.randint(0, 2)
        interpretation(first_move, second_move)
        question = input('Do you want to play again? Write "yes" to continue.'
                         ).lower()
        if question != 'yes':
            break

@cli.command
def player():
    while True:
        gamer_choose = int(input('What do you want to choice? Type 0 for rock, 1 for paper, \n 2 for scissors.\n'))
        computer_choice = random.randint(0, 2)
        interpretation(gamer_choose, computer_choice)
        question = input('Do you want to play again? Write "yes" to continue.'
                         ).lower()
        if question != 'yes':
            break

if __name__ == "__main__":
    cli()
