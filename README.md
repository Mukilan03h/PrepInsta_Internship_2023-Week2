# Puzzle Game Frog Leap

## Summary
This Python script implements the text-based puzzle game Frog Leap. 
The game pits two groups of frogs (Green and Brown) on opposing banks of a river. 
The goal is to make valid moves to alter the positions of the two groups of frogs.


## Gameplay Guidelines
1. Only green frogs can go to the right, whereas only brown frogs can move to the left.
2. Frogs can advance one place forward or two spaces forward by jumping over another frog from the opposite side.
3. The riddle is solved when the two groups of frogs trade places.


## Playing Instructions
1. Execute the Python script provided ('main.py').
2. The first screen shows the positions of Green ('G') and Brown ('B') frogs, as well as an empty leaf designated by '-'. 
3. Enter the frog's location to move or press 'q' to exit the game.
4. Input moves by following the suggestions. After each move, the script will update the game state.
5. Keep making movements until you win the game or opt to stop.

## Executing the Script
1. Make sure Python is installed on your PC.
2. Launch a command prompt or terminal.
3. Go to the directory that contains the script ('main.py').
4. Execute the script using the following command.
5. Follow the on-screen instructions to play the game.

## Example
python main.py
[ 0 , 1 , 2 , 3 , 4 , 5 , 6 ]
['G', 'G', 'G', '-', 'B', 'B', 'B']
Press q to quit
Enter position of piece: 2
[ 0 , 1 , 2 , 3 , 4 , 5 , 6 ]
['G', 'G', '-', 'G', 'B', 'B', 'B']
...
You Win

Note:
The game cycle continues until you win or exit by pressing 'q'.
The script uses the console for input and output, and the results may differ depending on the environment.

Feel free to change and expand the README as needed to include any new instructions, hints, or game information.
