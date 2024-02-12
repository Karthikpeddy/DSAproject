import json
import time

# Load words from a JSON file into a Python dictionary
def load_words_from_json():
    with open('words.json', 'r') as f:
        words = json.load(f)
    return words

# Capture user input from the terminal
def get_user_input(prompt):
    return input(prompt)

# Update and sort the leaderboard stored in a JSON file
def update_leaderboard(username, wpm):
    try:
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = {}

    leaderboard[username] = wpm

    # Sort the leaderboard by WPM
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f)

# Display the leaderboard from the JSON file
def show_leaderboard():
    try:
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        print("No leaderboard data found.")
        return

    for username, wpm in leaderboard.items():
        print(f"{username}: {wpm} WPM")

# Contains the main game logic
def main():
    username = get_user_input("Enter your username: ")
    while True:
        option = get_user_input("Choose an option: (1) Start the typing test, (2) Show the leaderboard, (3) Exit: ")
        if option == '1':
            words = load_words_from_json()
            start_time = time.time()
            for word in words:
                typed_word = get_user_input(f"Type this word: {word}")
                if typed_word != word:
                    print("Incorrect word. Try again.")
            end_time = time.time()
            time_taken = end_time - start_time
            words_per_minute = len(words) / time_taken * 60
            update_leaderboard(username, words_per_minute)
        elif option == '2':
            show_leaderboard()
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
