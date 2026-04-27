session_history = []

def add_to_session(user_text, ai_reply):
    session_history.append({
        "user": user_text,
        "ai": ai_reply
    })

def get_session():
    return session_history

def clear_session():
    session_history.clear()
