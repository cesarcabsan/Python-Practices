# Consider creating a text editor application and want to include an undo feature that lets revert changes made to a document. 
# The difficulty is in storing the document’s state at different times and restoring it when required without disclosing the document’s internal implementation.

# Originator class
class Document:
    def __init__(self, content):
        self._content = content 

    def write(self, text):
        """Append new text to the document."""
        self._content += text 

    def get_content(self):
        """Return current document content."""
        return self._content 
    
    def create_memento(self):
        """Create a memento containing the current state."""
        return DocumentMemento(self._content)
    
    def restore_from_memento(self, memento: "DocumentMemento"):
        """Restore content from a saved memento."""
        self._content = memento.get_saved_content()

# Memento class
class DocumentMemento:
    def __init__(self, content):
        self._content = content

    def get_saved_content(self):
        """Return the saved content."""
        return self._content 
    
# Caretaker class
class History:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: DocumentMemento):
        """Save a memento to history."""
        self._mementos.append(memento)

    def get_memento(self, index) -> DocumentMemento:
        """Retrieve a memento by index."""
        return self._mementos[index]


# Usage
document = Document("Initial content\n")
history = History()

# Write some content
document.write("Additional content\n")
history.add_memento(document.create_memento())

# Write more content
document.write("More content\n")
history.add_memento(document.create_memento())

# Restore to previous state
document.restore_from_memento(history.get_memento(1))

# Print document content
print(document.get_content())