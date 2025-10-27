import speech_recognition as sr
from datetime import datetime
import json

class To_do_list():

    def __init__(self):
        self.filename = "tasks.json"
        try:
            with open (self.filename, "r") as ace:
                self.data = json.load(ace)
        except FileNotFoundError:
            print("File doesn't exist or entered the wrong name")
            self.data = []

    def update(self):
        with open(self.filename, "w") as ace:
            json.dump(self.data, ace, indent=4)
        print("Update successfull")

    #Add a Note/Task: Append a new line to notes.txt.

    def add_note(self):
        note = input("Enter the note:")
        
        if any(note.lower() == n["note"].lower() for n in self.data):
            print("Note already exists")
        else:
            created_on = datetime.now().strftime("%d-%h-%Y %I:%M")
            entry = {"note": note, 
                        "created on": created_on,
                        "status": "Pending"}
            self.data.append(entry)
            self.update()

    #View All Notes: Read and display every note line by line.

    def view_notes(self):
        if not self.data:
            print("No notes available")
        else:
            for i, note in enumerate(self.data, start=1):
                print(f"{i}. {note['note']} ||| {note['created on']} ||| Staus: {note['status']}")

    #Search Notes: Enter a word → check if it exists in the notes.

    def search_notes(self):
        note = input("Enter the note: ").strip().lower()
        results = [n for n in self.data if note in n["note"].lower()]
        if results:
            print("Search Results:")
            for result in results:
                print(f"{result['note']} ||| {result['created on']} ||| Status: {result['status']}")
        else:
            print("Note doesn't exist")

    #Delete a Note: Remove specific note entered by user.

    def delete_note(self):
        self.view_notes()

        if self.data:
            try:
                serial_no = int(input("Enter the serial no. of note to delete: "))
                index = serial_no - 1
                if 0<=index < len(self.data):
                    deleted = self.data.pop(index)
                    self.update()
                    print(f"Note deleted: {deleted['note']}")
                else:
                    print("Invalid Serial Number")
            except ValueError:
                print("Please enter the valid serial number")
          

    #Statistics: Total notes count, longest note, number of words across all notes.

    def statistics(self):
        #Total note count
        
        note_count = len(self.data)
        print(f"Total Notes: {note_count}")

        #Longest Note

        longest_note = max(self.data, key=lambda n: len(n["note"]))
        print(f"Longest Note: {longest_note['note']}")

        #Number of words across notes

        total_words = 0
        for note in self.data:
            total_words+=len(note["note"].strip().split())

        print(f"Total words across the notes: {total_words}")

# --------------------------------------------------------------------------------------------------------------------------------------        

todo = To_do_list()

def voice_input():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak Command...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("Voice Input: ",command)
            return command.lower()    
        except sr.UnknownValueError:
            print("Sorry, could not understand your voice.")
        except sr.RequestError:
            print("Speech recognition service unavailable.")
        return ""

def get_command():
        command = voice_input()

        if not command:
            command = input("Enter the option(1/2/3/4/5/6): ")
        return command

command_map = {
    todo.add_note: ["1", "add", "add note", "note likho", "note add karo"],
    todo.view_notes: ["2", "view", "view all", "view notes", "notes dikhao"],
    todo.search_notes: ["3", "search", "find", "note search karo"],
    todo.delete_note: ["4", "delete", "remove", "note delete karo"],
    todo.statistics: ["5", "stats", "statistics", "note count"],
    "exit": ["6", "exit", "quit", "band karo"]
}

while True:
    print("\n1. Add a note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Delete note")
    print("5. Statistics")
    print("6. Exit")

    # Get command either by speech or typing
    command = get_command()

    # Handle choices
    
    for action, phrase in command_map.items():
        if command in phrase:
            if action == "exit":
                print("Exiting...")
                break
            else:
                print(f"Executing {action.__name__}()")
                action()
            break
    else:
        print("Invalid Input")
