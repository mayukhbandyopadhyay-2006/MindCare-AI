import datetime

JOURNAL_FILE = "journal_entries.txt"

def save_journal(entry):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"{date} - {entry}\n")

def read_journal():
    try:
        with open(JOURNAL_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["No journal entries found."]
