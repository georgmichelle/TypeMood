import time
from mood_analyzer import MoodAnalyzer

def main():
    analyzer = MoodAnalyzer()
    print("Type something, and I'll predict your mood! (Type 'exit' to stop)")

    while True:
        input("Press Enter and start typing...")
        start_time = time.time()
        user_input = input("You: ")
        end_time = time.time()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        mood = analyzer.predict_mood(user_input, start_time, end_time)
        print(f"AI: Based on your typing, I think you're feeling {mood}.\n")

if __name__ == "__main__":
    main()