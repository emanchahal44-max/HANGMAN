Hangman Game — Python Project
Overview
This is a console-based Hangman game built in Python.
The game allows users to select categories (like animals, fruits, science, english) and guess words either letter-by-letter or by guessing the full word.
Each round’s result is saved automatically in a log file, making it easy to track game history, total score, and performance.

Features
Category selection — choose between Animals, Fruits, English, or Science.  
Word guessing modes — guess single letters, multiple letters, or the full word.  
Display updates — shows correct letters and remaining attempts.  
Score tracking — earn points for correct guesses and full-word guesses
Game statistics — tracks wins, losses, total score, and win rate.  
Automatic logging — creates a folder for each game round with a detailed log file.

Folder Structure
hangman_game/
│
├── main.py                    
│
├── game/
│   ├── engine.py                
│   ├── wordlist.py              
│  
│
├── ui/
│   ├── display.py               
│   
│
├── words/
│   └── categories/              
│       ├── animals.txt
│       ├── fruits.txt
│       ├── english_general.txt
│       └── science.txt
│
├── game_log/                   
│   ├── game1/log.txt
│   ├── game2/log.txt
│   └── ...
│
└── README.md  
                  
How to Play
1. The game will show a list of categories:
 
   Categories: animals, fruits, english, science
   Choose a category (or leave empty for random):
  

2. Guess letters, letter sequences, or full words:
   Single letter → earns 10 points  
   Multiple letters(like “ing”) → earns 20 points if matched  
   Full word guess → earns 100 points if correct  

3. One have 6 wrong attempts before losing.

4. At the end of each game, a detailed summary and log file are generated automatically.

Game Logging Example
Each game round is saved under:
game_log/game1/log.txt
Sample log.txt content:
Game 1 Log
Category: fruits
Word: banana
Word Length: 6
Guesses (in order):
1. a → Correct
2. b → Correct
3. n → Correct
Wrong Guesses List:
Wrong Guesses Count: 0
Remaining Attempts at End: 6
Result: Win
Points Earned: 180
Total Score (after this round): 180
Games Played: 1
Wins: 1
Losses: 0
Win Rate: 100.00%
Date & Time: 2025-10-30 12:45:23

Scoring System
Action, Points 
1.Correct single letter, +10 
2.Correct multiple letters, +20 
3.Correct full word guess, +100
Win bonus, +50 

Example Output
Welcome to Hangman!
Categories: animals, fruits, english, science
Choose a category (or leave empty for random): fruits
Word: _ _ _ _ _ _
Guessed letters:
Remaining wrong guesses: 6
Enter your guess: a
Correct sequence found!
Word: a _ a _ a _
Guessed so far: a
Remaining wrong guesses: 6

Log Files
Every time one play:
A new folder is made inside game_log named game1, game2, etc.
Each folder contains a file log.txt with complete game details.
logs can be used to analyze progress or debugging.


