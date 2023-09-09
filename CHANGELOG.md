# 0.0.10 - 2023 - 09 - 09
### [ADDED]
- More functions to player turn method
- Game state attribute to ScrabbleGame(Game ongoing, game over)
- Method that ends and starts the game.
- Name attribute to the player class

###[FIXED]
- Minor fixes to structure

### [WIP]
- Method to display the board
- Better word scores

# 0.0.9 - 2023 - 09 - 08
### [ADDED]
- Player turn method, play, pass or draw tiles

### [FIXED]
- Squares now show their contents even when empty
- Player turn updates score
- Player tiles are now updated when they place tiles
# 0.0.8 - 2023 - 09 - 0
### [ADDED]
- A class that works as interface between the player and the game logic

### [FIXED]
- Several functions that weren't working as expected (see commits)

### [WIP]
- Player turn takes input from player and places a word where the player
wants, doesn't add score YET.

# 0.0.7 - 2023 - 09 - 04
### [FIXED]
- Methods for the square class, renamed them for better clarity
- Refactored references to old method names to use the improved ones
### [ADDED]
- A method that allows printing of each Square
- WIP method to print the whole board
# 0.0.6 - 2023 - 09 - 01
### [ADDED]
- Method that checks if a certain player has the tiles neccesary to make the word they intendo to make
- WIP player turn function
# 0.0.5 - 2023-08-28
### [FIXED]:
- Methods from the board class
### [ADDED]:
- Another method to the board class that returns the tile inside a certain square.
- A method that will place a word into the board to the ScrabbleGame class.
# 0.0.4 - 2023-08-23
### [FIXED]:
- Rearranged files
### [ADDED]:
- Added methods to the Square class
- Added a Scrabble class WIP
# 0.0.3 - 2023-08-21
### [ADDED]:
- Player class
- Score for players
- The tiles that each player has in possession
- Players can swap pieces they don't want with a random one from the bag
- Board class 
- The board is a grid of squares
- You can place tiles on the board
### [FIXED]:
- Square class now has a default multiplier of x1
- Tiles were given a custom comparison operator
- Changed structure of the project, the dictionary is now in a separate folder
- structure of the dictionary class
# 0.0.2 - 2023-08-19
### [ADDED]:
- List of words in Spanish considered legal for this version of Scrabble. 
- Function that checks if a given word is part of said list.
- Square class for future implementation of a Board class.
# 0.0.1 - 2023-08-18
### [ADDED]:
- List of letters to the Tilebag class. The amount of letters is now Fixed, as well as their score.
### [FIXED]:
- Fixed tests in order to stay relevant and evaluate the new format of the Tilebag class
