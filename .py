from journal_manager import save_journal
from session_manager import add_to_session

user_input = input("You: ")

save_journal(user_input)

ai_reply = "I understand how you feel."

add_to_session(user_input, ai_reply)

print("AI:", ai_reply)
