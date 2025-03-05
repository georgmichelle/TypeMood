import time
from data import mood_patterns

class MoodAnalyzer:
    def __init__(self):
        self.typing_speeds = []

    def analyze_speed(self, text, start_time, end_time):
        words = len(text.split())
        time_taken = end_time - start_time
        speed = words / time_taken if time_taken > 0 else 0
        self.typing_speeds.append(speed)
        avg_speed = sum(self.typing_speeds) / len(self.typing_speeds)

        if avg_speed > 3:
            return "Excited or Happy"
        elif avg_speed < 1:
            return "Tired or Sad"
        else:
            return "Neutral"

    def analyze_text(self, text):
        text = text.lower()
        for mood, keywords in mood_patterns.items():
            if any(word in text for word in keywords):
                return mood
        return "Neutral"

    def predict_mood(self, text, start_time, end_time):
        speed_mood = self.analyze_speed(text, start_time, end_time)
        text_mood = self.analyze_text(text)

        return text_mood if text_mood != "Neutral" else speed_mood