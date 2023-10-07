import time


questions = [
    "What is the capital of France?",
    "Which planet is known as the 'Red Planet'?",
    "Who painted the Mona Lisa?",
    "What is the tallest mountain in the world?",
    "Who is known as the 'Father of Computer Science'?"
]

answers = [
    "Paris",
    "Mars",
    "Leonardo da Vinci",
    "Mount Everest",
    "Alan Turing"
]
prize_pool = [1000, 2000, 3000, 4000, 5000]

def display_questions():
    total_prize = 0
    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}: {questions[i]}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answers[i].lower():
            print(f"Correct! You won ${prize_pool[i]}")
            total_prize += prize_pool[i]
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")
        time.sleep(1)
    return total_prize

def display_prize(total_prize):
    print("\nPrize Won:")
    print(f"You won a total of ${total_prize}")
def main():
    print("Welcome to the Quiz!")
    print("Answer the following questions:")

    total_prize = display_questions()
    display_prize(total_prize)

    time.sleep(0.5)
    print("Do you wish to play again?")
    print("If yes, enter 1 in choice.")
    choice = int(input("Enter your response: "))

    if choice == 1:
        play_game()
    else:
        print("Quitting quiz. Thank you for playing.")


def play_game():
    main()

if __name__ == "__main__":
    play_game()
