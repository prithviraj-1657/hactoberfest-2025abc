import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Dream big and dare to fail. – Norman Vaughan",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Success is not in what you have, but who you are. – Bo Bennett",
        "Start where you are. Use what you have. Do what you can. – Arthur Ashe"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n✨ Your Motivational Quote ✨\n")
    print(get_random_quote())
    print("\nKeep Going! 💪\n")
