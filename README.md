rock_paper_scissors.py

This script allows you to play Rock, Paper, Scissors against a computer opponent. You can choose to play against the computer or have the computer play against itself.

Installation

To use this script, you will need Python 3.6 or higher. You can install Python from https://www.python.org/downloads/

Usage

To play the game against the computer, run the following command:

python rock_paper_scissors.py player

To have the computer play against itself, run the following command:

python rock_paper_scissors.py computer

Commands

The script provides two commands:

    player: This command allows you to play the game against the computer. You will be prompted to choose rock, paper, or scissors. The computer will then choose a move and the results will be displayed.
    computer: This command allows you to watch the computer play against itself. The computer will choose a move randomly and the results of each round will be displayed.

Exiting the game

To exit the game, simply type quit at any time.

Example usage

$ python rock_paper_scissors.py player
Welcome to Rock, Paper, Scissors!
What do you want to choose? Type 0 for rock, 1 for paper, or 2 for scissors.
0
Computer chose scissors.
First player win!

Do you want to play again? Write "yes" to continue.
yes
What do you want to choose? Type 0 for rock, 1 for paper, or 2 for scissors.
2
Computer chose rock.
Second player win!

Do you want to play again? Write "yes" to continue.
no

-----------------------------------------------------------

To ensure the reliability and fairness of the rock-paper-scissors game, a robust testing suite is implemented using the pytest framework. 
Here's how the tests guarantee the expected behavior:

Test Coverage:

    Key Game Logic:
        test_interpretation: Validates the correctness of game outcome determination for player wins scenarios under various input combinations (rock vs. scissors, paper vs. rock).
        test_interpretation_second: Similar to test_interpretation, tests for a different player wins scenario (paper vs. rock).
        test_interpretation_third: Tests for second player wins scenario (rock vs. paper).
        test_interpretation_fourth: Ensures that the It's a draw case is handled correctly when both players choose the same option (tie).
    Error Handling:
        Additional tests could be added to verify how the code handles invalid inputs (outside the range of 0-2) or other potential edge cases.

Testing Process:

    Test File: Tests are located in the test.py file, separate from the game logic to maintain clarity and organization.
    Import and Setup: The pytest framework is imported, and test functions are defined.
    Test Implementation: Each test function uses assert statements to verify expected outcomes of the tested functions. For example, test_interpretation asserts that the interpretation function returns a string containing "First player win!" when the player's choice (0) wins against the computer's choice (2).
    Mocking and Redirection: The contextlib.redirect_stdout context manager captures the output of the tested function, allowing for comparison with expected results without affecting the actual console output.
    Execution and Verification: Running pytest test.py in the terminal executes the tests. If all assertions pass, the test suite is considered successful.

Benefits of Testing:

    Confident Gameplay: Rigorous testing helps you trust that the game functions as intended, providing a fair and enjoyable experience for players.
    Early Bug Detection: Tests catch potential issues before they impact users, leading to a more stable and polished game.
    Easy Maintenance: Well-structured tests make code modifications less risky, as changes can be quickly verified against existing test cases.

Continuous Improvement:

The testing suite can be constantly expanded to cover more scenarios and enhance the game's overall quality. Consider adding tests for:

    Advanced Game Modes: If you plan to implement features like best-of-three or multi-player modes, tailor tests to ensure their correct behavior.
    Error Handling: Write tests to confirm how the code handles invalid inputs, unexpected conditions, or resource limitations.
    Integration: If the game interacts with external components (databases, APIs), develop tests to validate their seamless integration.

By incorporating these improvements, you can solidify your rock-paper-scissors game as a well-tested and reliable application, fostering a positive user experience.
