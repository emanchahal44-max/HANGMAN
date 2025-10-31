import os
import datetime
from game.engine import play_game
from ui.display import display_welcome

# Game statistics
total_games = 0
wins = 0
losses = 0
total_score = 0

# Log directory
LOG_DIR = "game_log"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

display_welcome()

while True:
    result = play_game()  # This should return a dictionary with full details of the game
    total_games += 1
    total_score += result["points"]

    if result["won"]:
        wins += 1
    else:
        losses += 1

    win_rate = (wins / total_games) * 100 if total_games > 0 else 0

    # --- Save log for this game ---
    game_dir = os.path.join(LOG_DIR, f"game{total_games}")
    os.makedirs(game_dir, exist_ok=True)

    log_path = os.path.join(game_dir, "log.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"Game {total_games} Log\n")
        f.write(f"Category: {result['category']}\n")
        f.write(f"Word: {result['word']}\n")
        f.write(f"Word Length: {len(result['word'])}\n")
        f.write("Guesses (in order):\n")
        for i, (guess, status) in enumerate(result["guesses"], start=1):
            f.write(f"{i}. {guess} → {status}\n")
        f.write(f"Wrong Guesses List: {', '.join(result['wrong_guesses'])}\n")
        f.write(f"Wrong Guesses Count: {len(result['wrong_guesses'])}\n")
        f.write(f"Remaining Attempts at End: {result['remaining_attempts']}\n")
        f.write(f"Result: {'Win' if result['won'] else 'Loss'}\n")
        f.write(f"Points Earned: {result['points']}\n")
        f.write(f"Total Score (after this round): {total_score}\n")
        f.write(f"Games Played: {total_games}\n")
        f.write(f"Wins: {wins}\n")
        f.write(f"Losses: {losses}\n")
        f.write(f"Win Rate: {win_rate:.2f}%\n")
        f.write(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"\nGame Summary:")
    print(f"Points earned this round: {result['points']}")
    print(f"Total score: {total_score}")
    print(f"Games played: {total_games} | Wins: {wins} | Losses: {losses} | Win rate: {win_rate:.2f}%")

    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing! Goodbye ")
        break







