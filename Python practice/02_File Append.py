print("Enter the note you want to save:")
user_note = input("> ")

# 'a' mode stands for Append (adds to the end of file)
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write(user_note + "\n")

print("Note saved successfully to notes.txt!")