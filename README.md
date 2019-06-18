# Battle Dot

## How to run?

Simply run `python3 main.py` in terminal at current directory.

## What does it do?

It takes a number of players, puts them into a battle ship (or dot) battle. 

A group of players are of a circular linked list form, that is, 0 can only play against 1 (I use non-negative integers to represent players), 1 can only play against 2, 2 play against 3, etc. The last player, say n, plays against the very first player 0. 

## How to read the results?

After running the program, you will see some texts showed up in terminal.

The first line tells you who the players are. Below that each block of text gives info about each round of game, for example, which player wins the current round of game. The very last line tells you who the final winner is.

## Program structure

There are two classes: Player and PlayerList.

Player has info of each player's name, board, and play move, etc. 

PlayerList is an implementation of circular linked list that handles adding player, removing player, etc.

## How to change the number of players?

Inside `main()` function, you can change the value of the variable called `numOfPlayers`.

> The maximum number of players I've tested is 2000. It took about 1.5s to 2s to run the program.