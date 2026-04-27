def track_mood(text):

    sad_words = ["sad","depressed","lonely"]

    suicide_words = ["suicide","kill myself","die"]

    for w in suicide_words:
        if w in text.lower():
            return "suicidal"

    for w in sad_words:
        if w in text.lower():
            return "sad"

    return "normal"
