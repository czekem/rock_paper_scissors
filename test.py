import io
import sys
import pytest
from contextlib import redirect_stdout


def interpretation(player, computer):
    if player ==  0 and computer ==  2:
        return 'First player win!'
    elif computer ==  0 and player ==  2:
        return 'Second player win!'
    elif player > computer:
        return 'First player win!'
    elif computer > player:
        return 'Second player win!'
    elif computer == player:
        return 'It\'s a draw'
    else:
        return '' 



def test_interpretation():
    player = 0
    computer = 2
    assert 'First player win!' in interpretation(player, computer)

def test_interpretation_second():
    player = 1
    computer = 0
    assert 'First player win!' in interpretation(player, computer)
    


def test_interpretation_third():
    player = 0
    computer = 1
    assert 'Second player win!' in interpretation(player, computer)


def test_interpretation_fourth():
    player = 1
    computer = 1
    assert 'It\'s a draw' in interpretation(player, computer)
