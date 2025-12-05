from game_logic import play_game


if __name__ == "__main__":
    while True:
        play_game()

        replay_game = input("Play again? (y/n):")
        if replay_game == "n":
            print("Thank you for playing!")
            break