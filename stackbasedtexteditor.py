# Stack-based Text Editor in Python

class Stack:
    def __init__(self):  #creating an empty list in which everything is performed
        self.items = []

    def push(self, item):
        self.items.append(item)   # append the values using this func

    def pop(self):
        if not self.is_empty():       #for pop operation
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0   #check empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # for peek -1 fro last element
        return None

    def size(self):
        return len(self.items) # returning length as a size


class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()     #two more stack are created for keeping the functionality of redo and undo
        self.redo_stack = Stack()

    def insert(self, char):
        # Save current state to undo stack
        self.undo_stack.push(self.text)
        # Clear redo stack when a new action is performed
        self.redo_stack = Stack()
        # Update text
        self.text += char

    def delete(self):
        if self.text:
            # Save current state to undo stack
            self.undo_stack.push(self.text)
            # Clear redo stack
            self.redo_stack = Stack()
            # Remove last character
            self.text = self.text[:-1]

    def undo(self):
        if not self.undo_stack.is_empty():
            # Save current state to redo stack
            self.redo_stack.push(self.text)
            # Revert to previous state
            self.text = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack.is_empty():
            # Save current state to undo stack
            self.undo_stack.push(self.text)
            # Reapply the undone action
            self.text = self.redo_stack.pop()

    def display(self):
        print("Current Text:", self.text)


def main():
    editor = TextEditor()

    while True:
        editor.display()
        print("1. Insert")
        print("2. Delete")
        print("3. Undo")
        print("4. Redo")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            char = input("Enter a character: ")
            editor.insert(char)
        elif choice == "2":
            editor.delete()
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            editor.redo()
        elif choice == "5":
            print("Exiting the text editor. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()