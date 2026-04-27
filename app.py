from ai_therapist import respond
from mood_tracker import track_mood

user_input = input("You: ")

emotion = track_mood(user_input)

reply = respond(user_input, emotion)

print("AI Therapist:", reply)
